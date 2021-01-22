def reverse_string(str):
    reverse = ""
    for char in str:
        if char.islower():
            char=char.upper()
        else:
            char=char.lower()

        reverse = char + reverse
    return reverse


str = input("Enter your string: ")
result = reverse_string(str)
print(result)