def modify_content(content):
    """Modify the file content (example: convert to uppercase)."""
    return content.upper()  # You can change this modification as needed.

def read_and_modify_file():
    """Reads a file, modifies its content, and writes to a new file."""
    filename = input("Enter the filename to read: ")

    try:
        # Read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been saved in '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for reading '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
