while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        note = input("Enter note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note saved")

    elif choice == "2":
        with open("notes.txt", "r") as file:
            print(file.read())

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
