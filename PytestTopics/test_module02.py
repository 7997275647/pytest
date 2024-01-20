#Class is a blueprint
class TestClass():
    def testType(self):
        assert type(1)== int
    def testStr(self):
        assert str.upper("pytest")== "PYTEST"
        assert "pytest".capitalize() =="Pytest"