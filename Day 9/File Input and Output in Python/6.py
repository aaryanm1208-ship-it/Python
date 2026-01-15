with open("user_data.txt", "w") as file:
    name = input("Enter your name: ")
    file.write(name)
