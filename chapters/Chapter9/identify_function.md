# Identify Function or Structure

#### What type of function or structure we're using—like a loop, conditional, or function call—is a key skill in Python. Here's how we can identify them clearly:

## 🔍 Common Python Code Structures
| Code | Type | How to Recognize|
| --- | --- | --- |
| `for i in range(5):` | `for` loop | Starts with `for` — repeats code a specific number of times |
| `while condition:` | `while` loop | Starts with `while` — keeps repeating as long as the condition is `True` |
| `if condition:` | `if` statement | Starts with `if` — used for decisions |
| `def my_function():` | Function definition | Starts with `def` — defines a reusable block of code |
| `my_function()` | Function call | Calls a function (usually by name followed by `()`) |
| `with open("file.txt") as f:` | Context manager | Starts with `with` — used for resource management like file or database access |
| `print(...)` | Built-in function | A function call — here, `print` is Python's built-in function |

## 🧠 Identify Structures in Real Code

```python

for i in range(3):     # 🔁 for loop
    print(i)           # 📞 function call (print)

while x < 5:           # 🔁 while loop
    x += 1             # Statement inside loop

def greet():           # 📦 function definition
    print("Hi")

greet()                # 📞 function call

if x == 5:             # 🔀 if condition
    print("x is 5")
```


## ✅ Quick Identification Tips:
- `for` and `while` → loops

- `if`, `elif`, `else` → conditionals (decision-making)

- def → defining your own function

- Anything ending in `()` is usually a function call

- `with` → special construct for managing resources

