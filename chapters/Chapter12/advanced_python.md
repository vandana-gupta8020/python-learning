# ADVANCED PYTHON 1

## **NEWLY ADDED FEATURES IN PYTHON**
Following are some of the newly added features in Python programming language.

## **WALRUS OPERATOR**
The walrus operator (:-), introduced in Python 3.8, allows you to assign values to variables as part of an expression. This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the **`"assignment expression."`**

### ***Using walrus operator***
```python
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long (({n} elements, expected <= 3)")

# Output: List is too long (5 elements, expected <= 3)
```

In this example, `n` is assigned the value of `len([1, 2, 3, 4, 5])` and then used in the comparison within the if statement.

## **TYPES DEFINITIONS IN PYTHON**
Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.

```python
# variable type hint
age int = 25

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Usage
print(greeting("Alice")) # Output: Hello, Alice!
```

## **ADVANCED TYPE HINTS**
- Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.
- You can import List, Tuple and Dict types from the typing module like this:
```python
from typing import List, Tuple, Dict, Union
```

The syntax of types looks something like this:

```python
from typing import List, Tuple, Dict, Union.

# List of integers 
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer 
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values 
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union [int, str] = "ID123"
identifier = 12345     # Also valid
```

These annotations help in making the code self-documenting and allow developers to understand the data structures used at a glance.
