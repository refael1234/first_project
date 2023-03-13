import pytest
from function import get_user_value
from coins import USD, ILS, EUR

# Test 1: inserting a number
def test_convert_value():
  x = USD()
  m = x.calculate(1)
  assert m == 3.52

  # Test 2: Asserting Result is valid
  assert isinstance(m, float)
  assert m > 0

 # Test 3: Checking the content of the results file
 #    with open("result.txt", "r") as f:
 #        contents = f.read()
 #    assert f"{'1.0 dollars = 3.52 shekels'} -> {m}" in contents