# Program Name: Assignment1.py
# Course: IT3883/Section XXX
# Student Name: John Doe
# Assignment Number: Lab#
# Due Date: xx/xx/20XX
# Purpose: This program implements a text-based menu that allows the user to append data to an input buffer, clear the buffer, display the buffer, or exit the program.
# List Specific resources used to complete the assignment: Python documentation, online tutorials.

def main():
    # Initialize an empty input buffer
    input_buffer = ""

    while True:
        # Display the menu
        print("\nText-Based Menu")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit the program")

        # Prompt the user to make a choice
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        # Process the user's choice
        if choice == 1:
            # Append data to the input buffer
            data = input("Enter a string to append to the input buffer: ")
            input_buffer += data
            print("Data appended successfully.")
        elif choice == 2:
            # Clear the input buffer
            input_buffer = ""
            print("Input buffer cleared.")
        elif choice == 3:
            # Display the input buffer
            print("Current input buffer:")
            print(input_buffer if input_buffer else "[Buffer is empty]")
        elif choice == 4:
            # Exit the program
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()