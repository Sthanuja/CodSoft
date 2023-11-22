import random
import string

def Generate_Password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "hard":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Choose complexity (easy, medium, hard): ")

    password = Generate_Password(length, complexity)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
