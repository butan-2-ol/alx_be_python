def main():
    shopping_list = []

    while True:
        print("\n=== SHOPPING LIST MENU ===")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # ==============================
        # ADD ITEM
        # ==============================
        if choice == "1":
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
            else:
                print("Invalid item name.")

        # ==============================
        # REMOVE ITEM
        # ==============================
        elif choice == "2":
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        # ==============================
        # VIEW LIST
        # ==============================
        elif choice == "3":
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")

        # ==============================
        # EXIT PROGRAM
        # ==============================
        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        # ==============================
        # INVALID INPUT
        # ==============================
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# run program
if __name__ == "__main__":
    main()
