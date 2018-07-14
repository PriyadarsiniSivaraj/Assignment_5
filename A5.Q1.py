def my_function():
    try:
        x = 5/0
        print(x)
    except ZeroDivisionError:
        print("A number cannot be divided by Zero")

my_function()
