print("PROGRAM INI MENGEMBALIKAN INPUTAN STRING KE BENTUK KEBALIKAN")

def reverse_string (string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string

word = input("Enter your string: ")

print(f"Original string: {word}")
print(f"Reversed string: {reverse_string(word)}")