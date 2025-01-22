def number_generator():
    num = 1
    while True:  # Infinite generator
        yield num
        num += 1

def get_first_n_numbers(max):
    gen = number_generator()  # Create the generator once
    for _ in range(max):
        print(next(gen))  # Get the next value from the generator

get_first_n_numbers(10)
