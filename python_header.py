import os
import datetime

# Path to your Python file (with correct backslashes)
file_path = r"E:\Learning\Python\Python_Projects\FizzBuzz\fizz_buzz.py"  # Modify with the actual file path

# Get current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Get user input for project details
project_name = input("Enter the project name: ")
description = input("Enter a short description of the project: ")
author = "ziqkimi308"
version = input("Enter the version (optional): ")

# Header comment template with space at the end
header_template = f"""
\"""
********************************************************************************
* Project Name:  {project_name}
* Description:   {description}
* Author:        {author}
* Created:       <Created Date Placeholder>
* Updated:       {current_date}
* Version:       {version if version else '<Not specified>'}
********************************************************************************
\"""

"""  # Add a newline after the header to separate it from the code

def update_header():
    # Open the file with UTF-8 encoding to handle non-ASCII characters
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Check if the header exists (for example, by checking if the first line starts with '*')
    if lines and lines[0].startswith("* Project Name:"):
        # Replace the header with the new one, but do not change the Created date
        lines[0:7] = header_template.strip().split("\n")
    else:
        # Insert the Created date (if it's not there yet)
        created_date = "<Created Date Placeholder>"
        lines.insert(0, header_template.replace("<Created Date Placeholder>", current_date).strip() + "\n")

    # Write the updated lines back to the file, also using UTF-8 encoding
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Run the function to update the header
update_header()

print(f"Header for '{project_name}' has been updated successfully!")
