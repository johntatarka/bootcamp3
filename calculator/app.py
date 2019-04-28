from chalice import Chalice, BadRequestError

app = Chalice(app_name='calculator')

app.debug = True


def add(a, b): return a + b


def subtract(a, b): return a - b


def multiply(a, b): return a * b


def divide(a, b): return a / b


@app.route('/calculate/{function}/{a}/{b}')
def calc(function, a, b):
    try:
        return {'Hello': 'CS124 comper!', 'You requested the following function': function, "You requested the following parameters": (a, b), 'Your result is': globals()[function](int(a), int(b))}
    except KeyError:
        raise BadRequestError(
            "Unknown function '%s'. Valid options are 'add', 'subtract', 'multiply', and 'divide'." % function)
    except ZeroDivisionError:
        raise BadRequestError("Error: division by zero.")
