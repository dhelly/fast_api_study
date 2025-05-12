import pytest

def test_equal_or_not_equal():
    assert 1 == 1
    assert 1 != 2
    
def test_is_instance():
    assert isinstance("Isto é uma string", str)
    assert not isinstance(1, str)
    
def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'word') is False
    
    
def test_type():
    assert type(1) is int
    assert type("Isto é uma string") is not int
    assert type([1, 2, 3]) is list
    assert type((1, 2, 3)) is not list
    
    
def test_greater_than():
    assert 2 > 1
    assert not (1 > 2)
    assert 3 >= 3
    assert not (2 >= 3)
    
def test_list():
    my_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert len(my_list) == 5
    assert my_list[0] == 1
    assert 7 not in my_list
    assert all(my_list) # a função all() retorna True se todos os elementos da lista forem verdadeiros (em Python, números diferentes de zero são considerados True). Como todos os números da lista são diferentes de zero, essa verificação passa.
    assert not any(any_list) # a função any() retorna True se algum elemento da lista for True. Como todos os elementos de any_list são False, any(any_list) é False, e o not inverte para True, então essa verificação também passa.


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years
        
@pytest.fixture
def default_student():
    return Student("John", "Doe", "Computer Science", 2)
    
def test_person_initialization(default_student):
    
    assert default_student.first_name == "John", 'First name should be John'
    assert default_student.last_name == "Doe", 'Last name should be Doe'
    assert default_student.major == "Computer Science"
    assert default_student.years == 2  
    