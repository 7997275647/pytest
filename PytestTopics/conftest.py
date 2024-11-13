import pytest
import Source.Shapes as shapes
#################################################################
########These Fixures can be used anywhere in this directory#####
#################################################################
@pytest.fixture
def  my_rectangle():
    return shapes.rectangle(10,20)
@pytest.fixture
def other_rectangle():
    return shapes.rectangle(5,6)