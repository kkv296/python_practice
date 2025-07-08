import pytest

from employee import Employee
@pytest.fixture
def employee():
    def _create(first,last,salary):
        return Employee(first,last,salary)
    return _create

def test_give_default_raise(employee):
    shili1=employee('key','sun',1000)
    shili1.give_raise()
    assert shili1.salary == 6000

def test_give_custom_raise(employee):
    shili2=employee('red','sun',4000)
    shili2.give_raise(400)
    assert shili2.salary == 4400