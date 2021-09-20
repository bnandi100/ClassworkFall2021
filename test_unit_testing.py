import pytest

@pytest.mark.parametrize("input, expected", [([(3,2),(4,5),1],-4),([(3,2),(4,5),2],-1)])
def test_exercise(input,expected):
    from unit_testing import exercise
    #input = [(3,2),(4,5),1]
    #expected = -4 
    answer = exercise(input[0],input[1],input[2])
    assert answer == expected