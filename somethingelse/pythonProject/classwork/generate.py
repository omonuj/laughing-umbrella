def process_input(input_str):
    num_list = [num.strip() for num in input_str.split(',')]
    num_tuple = tuple(num_list)

    return num_list, num_tuple

input_str = input("Enter comma-separated numbers: ")
list_result, tuple_result = process_input(input_str)


print("List:", list_result)
print("Tuple:", tuple_result)
