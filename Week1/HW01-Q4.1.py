def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return False

def t():
    print(1)

def f():
    print(2)