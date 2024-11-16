import pytest
from unittest.mock import Mock

# Assuming your classes are imported from a module named classroom_module
from Source.school import classroom, teachers, students, TooManyStudents


@pytest.fixture
def default_classroom():
    """Fixture to provide a default classroom setup."""
    teacher = teachers("Mr. Smith")
    student_list = [students(f"Student{i}") for i in range(5)]
    course = "Mathematics"
    return classroom(teacher, student_list, course)


def test_add_a_student(default_classroom):
    """Test adding a student."""
    new_student = students("New Student")
    default_classroom.add_a_student(new_student)
    assert len(default_classroom.students) == 6
    assert default_classroom.students[-1].name == "New Student"


def test_add_a_student_too_many(default_classroom):
    """Test adding a student when the classroom is full."""
    # Fill the classroom to the limit
    for i in range(6):
        default_classroom.add_a_student(students(f"ExtraStudent{i}"))

    with pytest.raises(TooManyStudents):
        default_classroom.add_a_student(students("OneTooMany"))


def test_remove_student(default_classroom):
    """Test removing a student."""
    initial_count = len(default_classroom.students)
    student_to_remove = default_classroom.students[0]
    default_classroom.remove_student(student_to_remove.name)
    assert len(default_classroom.students) == initial_count - 1
    assert student_to_remove not in default_classroom.students


def test_remove_nonexistent_student(default_classroom):
    """Test removing a student who is not in the classroom."""
    initial_count = len(default_classroom.students)
    default_classroom.remove_student("Nonexistent Student")
    assert len(default_classroom.students) == initial_count


def test_change_teacher(default_classroom):
    """Test changing the teacher."""
    new_teacher = teachers("Mrs. Johnson")
    default_classroom.change_teacher(new_teacher)
    assert default_classroom.teacher.name == "Mrs. Johnson"


@pytest.mark.parametrize(
    "teacher_name, student_count, course_name",
    [
        ("Ms. Green", 3, "Science"),
        ("Mr. Brown", 0, "History"),
        ("Dr. Blue", 10, "Physics"),
    ],
)
def test_classroom_initialization(teacher_name, student_count, course_name):
    """Test classroom initialization with different parameters."""
    teacher = teachers(teacher_name)
    student_list = [students(f"Student{i}") for i in range(student_count)]
    cls = classroom(teacher, student_list, course_name)
    assert cls.teacher.name == teacher_name
    assert len(cls.students) == student_count
    assert cls.course == course_name


def test_mocked_teacher():
    """Test using a mocked teacher."""
    mock_teacher = Mock()
    mock_teacher.name = "Mock Teacher"
    cls = classroom(mock_teacher, [], "Mock Course")
    assert cls.teacher.name == "Mock Teacher"
