Digital Library Program

This repository contains a simple command-line interface (CLI) application for managing a digital library. It demonstrates basic CRUD (Create, Read, Update, Delete) operations on a collection of book records.
Features

-  Create Data: Add new book records (title, author, publication year).

-  Read Data: Display all existing book records in a formatted table.

-  Update Data: Modify details of an existing book record.

-  Delete Data: Remove a book record from the library.

-  Cross-Platform Compatibility: Clears the console screen based on the operating system (posix for Linux/macOS, nt for Windows).
  

What I Learned

Building this digital library program helped me solidify my understanding of several fundamental Python concepts:

- Modular Programming: Organizing code into separate modules (e.g., os for system interactions, CRUD.Database for database operations) promotes cleaner, more maintainable code.

- Basic I/O Operations: Taking user input (input()) and printing formatted output (print()).

- Conditional Logic (match statement): Efficiently handling different user options and adapting to different operating systems.

- Loops (while True): Creating a persistent menu-driven application.

- Data Structures: Although not explicitly shown in this main.py, the Database module likely uses dictionaries or lists to store book records.

- String Formatting: Using f-strings and string methods (<, center) for creating well-aligned and readable console output.

- Error Handling (Implicit): The get("key", "N/A") pattern for dictionary access demonstrates a basic way to prevent errors if a key is missing.
