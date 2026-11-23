def safe_divide(a, b):
    """Divide a by b and return the result, or return an error message if b is zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def safe_number(text):
    """Convert text into an integer and return it, or return an error message if conversion fails."""
    try:
        return int(text)
    except ValueError:
        return "Not a number"

def get_field(learner, key):
    """Return the value for a given key in the learner dictionary, or return an error message if missing."""
    try:
        return learner[key]
    except KeyError:
        return "Field not found"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))
