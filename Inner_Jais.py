def outer_function(greeting, *args, **kwargs):
    def inner_function():
        print(f"{greeting}, das sind deine Argumente:")

    inner_function()

    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

outer_function("Hallo", 1, 2, 3, name="Alice", age=25)
