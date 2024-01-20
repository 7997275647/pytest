#Function to convert centigrade fahrenheit
import sys

import pytest

pytestmark = pytest.mark.skipif(sys.platform != "win32",reason="will work only on windows platform")

factor = 9/5
def centi_to_fah(centi=0):
    fah = centi*factor+32
    return fah
print(centi_to_fah(60))
#@pytest.mark.skip(" skipped for no reason")
@pytest.mark.skipif(centi_to_fah() == 32,reason="Default value test , so skipping")
def test01():
    assert centi_to_fah()==32
def test02():
    assert centi_to_fah(60)==140
@pytest.mark.skipif(sys.version_info > (3,8),reason="Does not work for versions above 3.8")
def test03():
    assert centi_to_fah(50)==122

