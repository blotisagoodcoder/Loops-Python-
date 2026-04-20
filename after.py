print("LIST ACP")

def squar_and_filter_even_odd(numbers):
    even_squares=[]
    odd_squares=[]

    for num in numbers:
        squared_value = num ** 2

        if squared_value % 2 == 0:
            even_squares.append(squared_value)
        else:
            odd_squares.append(squared_value)

    return even_squares, odd_squares
my_list=[1,2,3,4,5,6,7,8]
even_results, odd_results = squar_and_filter_even_odd(my_list)
print(f"ORIGINAL LIST: {my_list}")
print(f"SQUARED EVEN NUMBERS:{even_results}")
print(f"Squared Odd Numbers:{odd_results}")