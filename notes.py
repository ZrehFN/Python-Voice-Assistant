def notes():
    def print_menu():
        print('1. Print all notes.')
        print('2. Add a note.')
        print('3. Remove a note')
        print('4. Lookup a note.')
        print('5. Quit notes.')
        print()

    numbers = {}
    menu_choice = 0
    print_menu()
    while menu_choice != 5:
        menu_choice = int(input("Type in a number (1-5): "))
        if menu_choice == 1:
            print("Notes:")
            for x in numbers.keys():
                print("Name: ", x, "\tContent:", numbers[x])
            print()
        elif menu_choice == 2:
            print("Add note")
            name = input("Name: ")
            phone = input("Content: ")
            numbers[name] = phone
        elif menu_choice == 3:
            print("Remove note")
            name = input("Name of note: ")
            if name in numbers:
                del numbers[name]
            else:
                print(name, "was not found")
        elif menu_choice == 4:
            print("Lookup note")
            name = input("Name: ")
            if name in numbers:
                print(numbers[name])
            else:
                print(name, "was not found")
        elif menu_choice != 5:
            print_menu()
