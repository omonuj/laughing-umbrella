def equal_strings(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = equal_strings(string1, string2)

if result:
    print("The strings are equal in characters and length:", result)
else:
    print("The strings are not equal in characters and length:", result)