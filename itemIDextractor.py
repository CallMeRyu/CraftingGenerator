# Place this script in the same path as quest_organizer.py 
# From there, it will read from organized_quests folder and do the rest for you

import os  # This module lets us interact with the computer's file system, like finding and opening files.
import re  # This module helps us search for specific patterns of text within files, like finding a word in a document.

# Define the root directory to search
root_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'organized_quests')
# This line sets the starting point (root directory) where we will look for files.
# "os.path.dirname(os.path.abspath(__file__))" finds the folder where this script is located.
# Then we add 'organized_quests' to it, meaning we want to look inside a folder named 'organized_quests'.

# Define the output files
output_ids_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extracted_item_ids.txt')
output_full_items_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extracted_full_items.txt')
# These lines create the paths (locations) where we will save our results.
# "extracted_item_ids.txt" will store a list of item IDs.
# "extracted_full_items.txt" will store full descriptions of items.

# Function to extract item IDs and full item descriptions from a .snbt file
def extract_items(snbt_file):
    item_ids = []  # This list will hold the item IDs we find in the file.
    full_items = []  # This list will hold the full descriptions of items.
    try:
        # Open the .snbt file and read its contents
        with open(snbt_file, 'r') as file:
            content = file.read()  # We read everything in the file into the "content" variable.

            # Search for the "item:" field and extract the item ID
            items = re.findall(r'item:\s*"(.*?)"', content)
            # This line looks for patterns like 'item: "some_item_id"' in the content.
            # It finds and extracts the text that represents the item ID (the part inside the quotes).
            item_ids.extend(items)  # We add any found item IDs to our list.

            # Search for the full item description, capturing everything inside { }
            full_item_matches = re.findall(r'\{id:\".*?\".*?\}', content)
            # This line looks for full item descriptions that are inside curly braces { }.
            # It finds everything that starts with 'id:"some_id"' and includes everything that follows within the braces.
            full_items.extend(full_item_matches)  # We add any found full item descriptions to our list.

    except Exception as e:
        # If something goes wrong (like the file can’t be read), this block will handle the error.
        print(f"Error reading file {snbt_file}: {e}")
        # It will print an error message telling us which file caused the problem and what went wrong.
    
    return item_ids, full_items  # Finally, the function returns the lists of item IDs and full descriptions.

# Function to recursively scan directories and extract item IDs and full item descriptions
def scan_directories_and_extract_items(directory):
    all_item_ids = []  # This list will hold all the item IDs found in all files.
    all_full_items = []  # This list will hold all the full item descriptions found in all files.
    # This loop goes through every folder and file within the specified directory (and any subfolders).
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.snbt'):
                # If the file ends with '.snbt', we will process it.
                snbt_file_path = os.path.join(root, file)  # We create the full path to this file.
                item_ids, full_items = extract_items(snbt_file_path)  # We call the extract_items function to get data.
                all_item_ids.extend(item_ids)  # We add the found item IDs to our master list.
                all_full_items.extend(full_items)  # We add the found full item descriptions to our master list.
    return all_item_ids, all_full_items  # After processing all files, we return the collected data.

# Main function to perform the extraction and write to the text files
def main():
    # Scan directories and extract all item IDs and full item descriptions
    all_item_ids, all_full_items = scan_directories_and_extract_items(root_directory)
    # This line runs the function to search the root directory and extract the needed information.

    # Write the item IDs to the output file
    with open(output_ids_file, 'w') as f:
        # This opens the output file for item IDs so we can write to it.
        for item_id in all_item_ids:
            f.write(item_id + '\n')  # This writes each item ID on a new line in the file.

    # Write the full item descriptions to the other output file
    with open(output_full_items_file, 'w') as f:
        # This opens the output file for full item descriptions so we can write to it.
        for full_item in all_full_items:
            f.write(full_item + '\n')  # This writes each full item description on a new line in the file.
    
    # Print a message to let us know the extraction is done and where the files are saved.
    print(f"Extraction complete. Item IDs have been written to {output_ids_file}")
    print(f"Full item descriptions have been written to {output_full_items_file}")

# Run the main function
if __name__ == "__main__":
    main()
    # This line checks if this script is being run directly (not imported as a module).
    # If it is, it will run the main function to start the extraction process.
