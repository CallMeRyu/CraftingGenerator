# This Python script is designed to help you generate code snippets for a Minecraft mod setup.
# The script will scan through all JSON files in your "dumps" directory and its subdirectories,
# looking for loot table information. It will then generate lines of code that you can use
# in your CraftTweaker or LootTweaker scripts, specifically to apply coin entries to those loot tables.

# To use this script, place it in the "dumps" folder, which is at the same level as the "loot_tables" folder.
# When you run this script, it will create a file called "generated_apply_calls.txt" in the same directory.
# This text file will contain the generated code lines that you can copy and paste into your `dungeonloot.zs` script.

import os  # Import the OS module to interact with the file system.
import json  # Import the JSON module to parse JSON files.

def generate_apply_coin_entries_calls(root_dir):
    """
    This function scans all directories and files starting from 'root_dir'.
    It looks for JSON files, extracts relevant information, and generates code snippets.
    
    Parameters:
        root_dir (str): The directory where the script is located and where the scanning starts.
    
    Returns:
        apply_calls (list): A list of code strings that can be used in your Minecraft mod scripts.
    """
    apply_calls = []  # Create an empty list to store the generated code lines.
    
    # Walk through all directories and files from the root directory.
    # os.walk() allows us to navigate through the directory tree, one folder at a time.
    for subdir, _, files in os.walk(root_dir):
        for file in files:  # Iterate through each file in the current directory.
            if file.endswith(".json"):  # Check if the file is a JSON file.
                file_path = os.path.join(subdir, file)  # Get the full path to the file.
                
                # Read the JSON file
                with open(file_path, 'r') as f:
                    try:
                        data = json.load(f)  # Load the JSON data from the file.
                    except json.JSONDecodeError:  # Handle errors in case the JSON is not properly formatted.
                        print(f"Error decoding JSON in file: {file_path}")
                        continue  # Skip to the next file if there's an error.
                    
                    # Extract the loot table ID from the JSON data.
                    loot_table_id = data.get('loottweaker:dump_info', {}).get('id')
                    
                    # Extract all pool names from the JSON data.
                    pools = data.get('pools', [])
                    for pool in pools:
                        pool_name = pool.get('name')  # Get the name of the pool.
                        if loot_table_id and pool_name:  # Check if both the ID and pool name exist.
                            # Generate the code line to add the coin entries to this specific pool.
                            call = f'applyCoinEntriesToTable("{loot_table_id}", "{pool_name}");'
                            apply_calls.append(call)  # Add the generated line to our list.
    
    return apply_calls  # Return the list of generated code lines.

def write_to_file(calls, output_file):
    """
    This function writes the generated code lines to a text file.
    
    Parameters:
        calls (list): A list of code strings to be written to the file.
        output_file (str): The name of the file to write the code lines into.
    """
    with open(output_file, 'w') as f:  # Open the file in write mode ('w').
        for call in calls:  # Iterate over each generated code line.
            f.write(call + '\n')  # Write the line to the file, followed by a newline.

if __name__ == "__main__":
    """
    This is the main part of the script that runs when you execute the script.
    It sets up the root directory, calls the function to generate code lines, 
    and writes those lines to a text file.
    """
    
    # Set the root directory to the location where the script is placed.
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate the applyCoinEntriesToTable calls by scanning the directories and files.
    apply_calls = generate_apply_coin_entries_calls(root_dir)
    
    # Set the name of the output file where the generated code will be saved.
    output_file = os.path.join(root_dir, "generated_apply_calls.txt")
    
    # Write the generated code lines to the output file.
    write_to_file(apply_calls, output_file)
    
    # Print some information to the screen so you know the script has completed successfully.
    print(f"Generated {len(apply_calls)} applyCoinEntriesToTable calls.")
    print(f"Output written to: {output_file}")
