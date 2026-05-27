import os

def menuscreen():
    os.system("cls")
    print("1. Open File")
    print("2. Enter Data")
    print("3. Edit File")
    print("4. Delete File")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice