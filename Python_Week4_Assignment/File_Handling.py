def read_and_write_file():
    """
    Reads a file, modifies its content, and writes the modified content to a new file.
    Includes error handling for file access issues.
    """
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Open and read the file
        with open(input_filename, "r") as infile:
            content = infile.readlines()

        # Modify the content (e.g., append a line number to each line)
        modified_content = [f"{idx + 1}: {line}" for idx, line in enumerate(content)]

        # Ask the user for the output filename
        output_filename = input("Enter the name of the new file to write: ")

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content has been written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print("Error: The file you entered does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: There was a problem reading or writing the file. Please check your file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Call the function
read_and_write_file()
