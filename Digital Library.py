import os
import CRUD.Database as Database # Import the Database module from the CRUD package

if __name__=="__main__":
    system_os = os.name # Get the operating system name

    # Clear the console screen at the beginning
    match system_os:
        case "posix": os.system("clear") # For Linux/macOS
        case "nt": os.system("cls")    # For Windows

    print("WELCOME TO DIGITAL LIBRARY PROGRAM")
    print("LIBRARY DATABASE")
    print("="*60) # Print a line of 60 equals signs

    # Check and initialize the database (if not found, it will create the first record)
    Database.init_console()

    # Main program loop to display the menu and get user options
    while True:
        # Clear the console screen at the start of each menu iteration
        match system_os:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("WELCOME TO DIGITAL LIBRARY PROGRAM")
        print("LIBRARY DATABASE")
        print("="*60)

        # Display menu options
        print(f"1. Read data")
        print(f"2. Create data")
        print(f"3. Update data")
        print(f"4. Delete data")

        user_option = input("Enter your option: ") # Prompt user for input

        print("\n","="*60,"\n") # Print separator lines

        # Handle user's chosen option
        match user_option:
            case "1":
                # --- Read Function Implementation ---
                all_records = Database.read_all_data() # Call function to read all data
                if all_records:
                    # Print table header
                    print(f"{'No.':<5} {'PK':<8} {'Title':<30} {'Author':<20} {'Year':<6}")
                    print(f"{'-'*5:<5} {'-'*8:<8} {'-'*30:<30} {'-'*20:<20} {'-'*6:<6}")
                    # Print each record in a formatted way
                    for i, record in enumerate(all_records):
                        pk = record.get("pk", "N/A") # Get PK, default to "N/A" if not found
                        title = record.get("title", "N/A")
                        author = record.get("author", "N/A")
                        year = record.get("year", "N/A")
                        print(f"{i+1:<5} {pk:<8} {title:<30} {author:<20} {year:<6}")
                else:
                    print("No data in the database.")
                # --- End Read Function Implementation ---

            case "2":
                Database.create_new_record() # Call function to create new data
            case "3":
                Database.update_record()     # Call function to update existing data
            case "4":
                Database.delete_record()     # Call function to delete data
            case _: # Default case for invalid options
                print("Invalid option. Please choose 1-4.")

        print("\n","="*60,"\n") # Print separator lines
        is_done = input("Are you done (y/n)? ").lower() # Ask if user wants to quit, convert to lowercase
        if is_done == "y": # If user types 'y' or 'Y', break the loop
            break

print("\n","===PROGRAM END===".center(60)) # Print program end message, centered