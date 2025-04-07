def read_and_modify_file(input_filename, output_filename):
    """
    Reads the content of a file, modifies it, and writes it to a new file.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()
        
        # Example modification: Add line numbers to each line
        modified_content = [f"{i + 1}: {line}" for i, line in enumerate(content)]
        
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        
        print(f"File '{input_filename}' has been successfully modified and saved as '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read or written.")

def main():
    """
    Main function to handle user input and execute file operations.
    """
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to save the modified content: ")
    
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()

