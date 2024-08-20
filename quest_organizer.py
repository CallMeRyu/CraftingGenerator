# If this script can help you in some way, by all means, use it. I just ask for credit. 
# This script is to work with "/ftbquests generate_chapter_with_all_items_in_game" command.  *(1.12.2)*
# Place this file in the same directory as the dumped quests list, so that your quests will now be organized into mods.
# This way you can tell what mod is what, making it a little easier to then make quests, removing quests from mods you don't want more quickly. 



import os
import shutil
import re

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the source directory as the script's directory
source_directory = script_directory

# Define the destination directory as a subfolder named "organized_quests" in the script's directory
destination_directory = os.path.join(script_directory, 'organized_quests')

# Function to extract the mod name from a .snbt file using the item field
def get_mod_name(snbt_file):
    try:
        with open(snbt_file, 'r') as file:
            content = file.read()

            # Method 1: Search for the "item:" field and extract the mod name
            items = re.findall(r'item:\s*"(.*?)"', content)
            if items:
                for full_item in items:
                    mod_name = full_item.split(':')[0]
                    if mod_name:  # Ensure it's not an empty string
                        return mod_name

            # (Optional) Add additional methods if needed, but ensure no invalid identifiers are used

    except Exception as e:
        print(f"Error reading file {snbt_file}: {e}")
    
    return None  # Return None if no valid mod name is found

# Function to organize the .snbt files into folders by mod name
def organize_files():
    for snbt_file in os.listdir(source_directory):
        if snbt_file.endswith('.snbt'):
            mod_name = get_mod_name(os.path.join(source_directory, snbt_file))
            
            if mod_name:  # Only move the file if a valid mod name is found
                mod_folder = os.path.join(destination_directory, mod_name)

                # Create the mod folder if it doesn't exist
                if not os.path.exists(mod_folder):
                    os.makedirs(mod_folder)

                # Move the .snbt file into the mod folder
                shutil.move(os.path.join(source_directory, snbt_file), mod_folder)
                print(f'Moved {snbt_file} to {mod_folder}')
            else:
                print(f'Skipped {snbt_file} because no mod name was identified.')

# Ensure the destination directory exists
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Run the organization function
organize_files()
