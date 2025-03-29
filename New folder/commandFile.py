import callfunctions as mine
import os
# Clear screen

# Display menu options in a table format


while True:
    mine.cls()
    print("=" * 50)
    print("{:<10} {:<20}".format("Command", "Description"))
    print("=" * 50)
    print("{:<10} {:<20}".format("C", "Create a file"))
    print("{:<10} {:<20}".format("W", "Write to a file"))
    print("{:<10} {:<20}".format("R", "Read content"))
    print("{:<10} {:<20}".format("D", "Delete a file"))
    print("{:<10} {:<20}".format("E", "Exit Program"))
    print("=" * 50)
    
    command = input("\nEnter Command: ").lower()
   

    if command == "c":
        mine.cls()
        print("=" * 50)
        print(" " * 10, "Type of a file")
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Employee"))
        print("{:<10} {:<20}".format("D", "Deduction"))
        print("=" * 50)

        comms = input("Enter Command: ").lower()
        if comms == "e":
            mine.create_file("employee.txt")
        elif comms == "d":
            mine.create_file("deductions.txt")

    elif command == "w":
        mine.cls()
        print("=" * 50)
        print(" " * 10, "Write a File to ")
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Employee"))
        print("{:<10} {:<20}".format("D", "Deduction"))
        print("=" * 50)
        comms = input("Enter Command: ").lower()

        if comms == "e":
            # Get employee data from the employee_Data function
            content = mine.employee_Data()

            # Convert the employee data to a string format (e.g., JSON-like or plain text)
            content_str = f"First Name: {content['First Name']}\nLast Name: {content['Last Name']}\nAge: {content['Age']}\nGender: {content['Gender']}"
            
            # Write the content to the file
            mine.write_to_file('employee.txt', content_str)

        elif comms == "d":
            content = mine.deduction_List()

            content_str = f"SSS Contribution: {content['SSS']}\nPag-IBIG Contribution: {content['Pag-IBIG']}\nPhilHealth Contribution: {content['PhilHealth']}\nBIR Tax: {content['BIR Tax']}"
      

            mine.write_to_file('deductions.txt', content_str)
    

    elif command == "r":
        mine.cls()
        print("=" * 50)
        print(" " * 10, "Read a File to ")
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Employee"))
        print("{:<10} {:<20}".format("D", "Deduction"))
        print("=" * 50)
        comms = input("Enter Command: ").lower()
        if comms == "e":
            mine.cls()
            print("=" * 50)
            file_content = mine.read_file('employee.txt')
            print("\nFile Content:\n" + "-" * 50)
            print(file_content)
            print("-" * 50)

        elif comms == "d":
            mine.cls()
            print("=" * 50)
            file_content = mine.read_file('deductions.txt')
            print("\nFile Content:\n" + "-" * 50)
            print(file_content)
            print("-" * 50)
      

    elif command == "d":
        confirm = input("Proceed to Delete: (y/n)").lower()
        if confirm == "y":
            mine.cls()
            print("=" * 50)
            print(" " * 10, "Read a File to ")
            print("=" * 50) 
            mine.delete_file('output.txt')
        elif confirm == "n":
            print("File has not deleted")
        else:
            print("Invalid Command")

    elif command == "e":
        mine.cls()
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Exiting a Program"))
        print("=" * 50)
        exit_confirm = input("\nAre u sure u want to exit? (y/n): ").lower()
        if exit_confirm != 'n':
            print("\nExiting the program. Goodbye!")
            break

        

    else:
        print("Invalid command. Please enter a valid command.")

    # Ask if the user wants to continue or exit
    continue_prompt = input("\nDo you want to continue? (y/n): ").lower()
    if continue_prompt != 'y':
        print("\nExiting the program. Goodbye!")
        break
