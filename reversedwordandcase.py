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



C:\Users\Rahul\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/Rahul/PycharmProjects/pythonProject/reverseword.py
Enter your string: hello worlD
dLROW OLLEH

Process finished with exit code 0