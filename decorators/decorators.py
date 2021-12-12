def output_of_type(func):
    def inner(*args, **kwargs):
        output = func(*args, **kwargs)
        print(f"Output of function {func.__name__} is {type(output)}")
        return output
    return  inner

