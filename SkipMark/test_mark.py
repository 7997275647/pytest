import pytest
pytestmark = pytest.mark.full
def test01():
    str1 = "pytest marking of test cases"
    str2 = "!!"
    assert str1+str2 == "pytest marking of test cases!!"
@pytest.mark.sanity
def test02():
    str1 = "python pytest framework"
    assert str1.split() == ["python","pytest","framework"]
@pytest.mark.smoke
def test03():
    str1 = "python,pytest framework"
    assert str1.split(",") == ["python","pytest framework"]
@pytest.mark.sanity
def test04():
    str1 = "python,pytest framework"
    assert str1[:] == "python,pytest framework"
    assert str1[0] == "p"
@pytest.mark.sanity
@pytest.mark.smoke
def test05():
    str1 = "python,pytest framework"
    assert str1[7:] == "pytest framework"
# use pytest -v -m sanity on command window to run the test cases under the group sanity
# use pytest -v -m smoke on command window to run the test cases under the group smoke
# use pytest -v -m "sanity and not smoke" on command window to run the test cases under the group sanity and not smoke
# use pytest -v -m "smoke or sanity" on command window to run the test cases under the group smoke or sanity
# TO AVOID WARNINGS CREATE PYTEST CONFIG FILE pytest.ini IN ROOT FOLDER PytestProject