import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])

def test_capitalize_positive(input_str, expected):
  assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
  ("123abc", "123abc"),
  ("", ""),
  (" ", " "),
])
def test_capitalize_negative(input_str, expected):
  assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
  ("skypro", "skypro"),
  ("hello world", "hello world"),
  ("python", "python"),

])

def test_trim_positive(input_str, expected):
 assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
  ("skypro", "skypro"),
])

def test_trim_negative(input_str, expected):
  assert string_utils.trim(input_str) == expected

# Позитивные тесты
def test_contains_positive_cases():
  assert string_utils.contains("SkyPro", "S") == True
  assert string_utils.contains("Hello, World!", "H") == True
  assert string_utils.contains("banana", "a") == True
  assert string_utils.contains("12345", "3") == True
  assert string_utils.contains("abcXYZ", "X") == True

# Негативные тесты
def test_contains_negative_cases():
  assert string_utils.contains("SkyPro", ";U") == False
  assert string_utils.contains("Hello, World!", "Z") == False
  assert string_utils.contains("banana", "x") == False
  assert string_utils.contains("12345", "6") == False
  assert string_utils.contains("abcXYZ", "A") == False

if __name__ == "__main__":

 pytest.main()

# Позитивные тесты
def test_delete_symbol_positive_cases():
  assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
  assert string_utils.delete_symbol("Hello World", "o") == "Hell Wrld"
  assert string_utils.delete_symbol("banana", "a") == "bnn"
  assert string_utils.delete_symbol("12345", "3") == "1245"
  assert string_utils.delete_symbol("abcXYZ", "X") == "abcYZ"

# Негативные тесты
def test_delete_symbol_negative_cases():
  assert string_utils.delete_symbol("SkyPro", "U") == "SkyPro"
  assert string_utils.delete_symbol("Hello World","z") == "Hello World"
  assert string_utils.delete_symbol("banana", "x") == "banana"
  assert string_utils.delete_symbol("12345", "6") == "12345"
  assert string_utils.delete_symbol("abcXYZ", "A") == "abcXYZ"

if __name__ == "__main__":
 pytest.main()