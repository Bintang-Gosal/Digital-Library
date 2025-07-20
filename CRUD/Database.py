# perpustakaan_digital/CRUD/Database.py

from . import operation
from . import config
import json

# Function to initialize the database
def init_console():
    try:
        with open(config.DB_NAME, "r", encoding="utf-8") as file:
            print("Database available, initialization complete!")
    except FileNotFoundError:
        print("Database not found. Please create new data.")
        try:
            with open(config.DB_NAME, "w", encoding="utf-8") as file:
                new_record = operation.create_first_data()
                if new_record:
                    # Write the new record to the file without indentation
                    json.dump(new_record, file)
                    file.write("\n")
                    print("First data successfully saved to data.txt!")
                else:
                    print("Warning: Created data is empty, nothing written to file.")
        except Exception as e:
            print(f"Error creating new database: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during initialization: {e}")

# Function to read all data
def read_all_data():
    try:
        with open(config.DB_NAME, "r", encoding="utf-8") as file:
            data_list = []
            for i, line in enumerate(file): # Enumerate for line numbering (for potential debugging)
                # print(f"DEBUG: Processing line {i+1}: '{line.strip()}'") # Debug print (can be removed)
                if line.strip(): # Ensure the line is not empty after stripping whitespace
                    try:
                        data_list.append(json.loads(line))
                    except json.JSONDecodeError as e: # Catch specific JSON decoding errors
                        print(f"ERROR: Line {i+1} corrupted in database: '{line.strip()}'")
                        print(f"DETAIL ERROR: {e}") # Show detailed error message
                        continue # Continue to the next line even if there's an error on this one
                # else:
                    # print(f"DEBUG: Skipping line {i+1} (empty/whitespace).") # Debug print (can be removed)
            return data_list
    except FileNotFoundError:
        print("Database not found. Please create new data.")
        return []
    except Exception as e: # Catch any other general errors
        print(f"An general error occurred while reading the database: {e}")
        return []

# Function to create new data (will call operation.create_first_data() or similar)
def create_new_record():
    print("\n--- Creating New Data ---")
    new_data = operation.create_first_data() # Call function to get data
    if new_data:
        try:
            with open(config.DB_NAME, "a", encoding="utf-8") as file: # 'a' for append mode
                json.dump(new_data, file)
                file.write("\n")
            print("New data successfully added!")
        except Exception as e:
            print(f"Failed to save new data: {e}")
    else:
        print("Data creation cancelled or data is empty.")

# Function to update data (more complex, requires ID)
def update_record():
    print("\n--- Updating Data ---")
    data_list = read_all_data() # Read all existing data

    if not data_list:
        print("Database is empty. No data to update.")
        return

    # Display available data for user to see PKs
    print("Available data:")
    # Re-use display logic from read_all_data or make a separate display function
    print(f"{'No.':<5} {'PK':<8} {'Title':<30} {'Author':<20} {'Year':<6}")
    print(f"{'-'*5:<5} {'-'*8:<8} {'-'*30:<30} {'-'*20:<20} {'-'*6:<6}")
    for i, record in enumerate(data_list):
        pk = record.get("pk", "N/A")
        title = record.get("title", "N/A")
        author = record.get("author", "N/A")
        year = record.get("year", "N/A")
        print(f"{i+1:<5} {pk:<8} {title:<30} {author:<20} {year:<6}")

    pk_to_update = input("Enter the PK of the book to update (e.g., ABCDEF): ").strip()

    found_index = -1
    for i, record in enumerate(data_list):
        if record.get("pk") == pk_to_update:
            found_index = i
            break

    if found_index != -1:
        print(f"\nData found for PK: {pk_to_update}")
        print(f"Old Title: {data_list[found_index].get('title')}")
        print(f"Old Author: {data_list[found_index].get('author')}")
        print(f"Old Year: {data_list[found_index].get('year')}")

        new_title = input("Enter new title (leave blank to keep current): ").strip()
        new_author = input("Enter new author (leave blank to keep current): ").strip()
        new_year = input("Enter new year (leave blank to keep current): ").strip()

        if new_title:
            data_list[found_index]["title"] = new_title
        if new_author:
            data_list[found_index]["author"] = new_author
        if new_year:
            data_list[found_index]["year"] = new_year

        # Optional: Update modification date if applicable
        # import datetime
        # data_list[found_index]["date_modified"] = datetime.datetime.now().strftime("%Y-%m-%d")

        # Write all data back to the file (MODE "w" TO OVERWRITE)
        try:
            with open(config.DB_NAME, "w", encoding="utf-8") as file:
                for record in data_list:
                    json.dump(record, file)
                    file.write("\n")
            print("Data successfully updated!")
        except Exception as e:
            print(f"Failed to save updated data: {e}")
    else:
        print(f"Book with PK '{pk_to_update}' not found.")

# Function to delete data (more complex, requires ID)
def delete_record():
    print("\n--- Deleting Data ---")
    data_list = read_all_data() # Read all existing data

    if not data_list:
        print("Database is empty. No data to delete.")
        return

    # Display available data for user to see PKs
    print("Available data:")
    print(f"{'No.':<5} {'PK':<8} {'Title':<30} {'Author':<20} {'Year':<6}")
    print(f"{'-'*5:<5} {'-'*8:<8} {'-'*30:<30} {'-'*20:<20} {'-'*6:<6}")
    for i, record in enumerate(data_list):
        pk = record.get("pk", "N/A")
        title = record.get("title", "N/A")
        author = record.get("author", "N/A")
        year = record.get("year", "N/A")
        print(f"{i+1:<5} {pk:<8} {title:<30} {author:<20} {year:<6}")

    pk_to_delete = input("Enter the PK of the book to delete (e.g., ABCDEF): ").strip()

    found_index = -1
    for i, record in enumerate(data_list):
        if record.get("pk") == pk_to_delete:
            found_index = i
            break

    if found_index != -1:
        print(f"\nData found for PK: {pk_to_delete}")
        print(f"Title: {data_list[found_index].get('title')}")
        print(f"Author: {data_list[found_index].get('author')}")
        confirmation = input("Are you sure you want to delete this data? (y/n): ").lower()

        if confirmation == 'y':
            del data_list[found_index] # Remove item from the list in memory

            # Write all remaining data back to the file (MODE "w" TO OVERWRITE)
            try:
                with open(config.DB_NAME, "w", encoding="utf-8") as file:
                    for record in data_list:
                        json.dump(record, file)
                        file.write("\n")
                print("Data successfully deleted!")
            except Exception as e:
                print(f"Failed to save data after deletion: {e}")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Book with PK '{pk_to_delete}' not found.")