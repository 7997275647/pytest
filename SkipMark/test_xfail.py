import sys

import pytest
import sys
@pytest.mark.xfail(raises=AssertionError, reason= "Known Issue")
def test01():
    str1 = "pytest marking of test cases"
    str2 = "!!"
    assert str1+str2 == "pytest marking of test cases !!"
#@pytest.mark.xfail
def test02():
    str1 = "python pytest framework"
    assert str1.split() == ["python","pytest","framework"]
#@pytest.mark.smoke
def test03():
    str1 = "python,pytest framework"
    assert str1.split(",") == ["python","pytest framework"]
@pytest.mark.xfail(sys.platform =="win32", reason="works only on windows")
def test04():
    str1 = "python,pytest framework"
    assert str1[:] == "python,pytest framework"
    assert str1[1] == "p"    #make it fail intentionally
#@pytest.mark.sanity
@pytest.mark.xfail
def test05():
    str1 = "python,pytest framework"
    assert str1[6:] == "pytest framework"
# you can also mention a reason for your reference
# we can also use a condition inside of Xfail