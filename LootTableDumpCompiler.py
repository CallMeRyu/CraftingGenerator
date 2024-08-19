# The DUMPS FOLDER, you will need to place this file inside it. The SAME location where loot_tables is at.
# When ran, it will create a file called generated_apply_calls.txt 
# That txt will generate codes for my dungeonloot.zs preset



import os
import json

def generate_apply_coin_entries_calls(root_dir):
    apply_calls = []
    
    # Walk through all directories and files from the root directory
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(subdir, file)
                
                # Read the JSON file
                with open(file_path, 'r') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON in file: {file_path}")
                        continue
                    
                    # Extract the id
                    loot_table_id = data.get('loottweaker:dump_info', {}).get('id')
                    
                    # Extract all pool names
                    pools = data.get('pools', [])
                    for pool in pools:
                        pool_name = pool.get('name')
                        if loot_table_id and pool_name:
                            call = f'applyCoinEntriesToTable("{loot_table_id}", "{pool_name}");'
                            apply_calls.append(call)
    
    return apply_calls

def write_to_file(calls, output_file):
    with open(output_file, 'w') as f:
        for call in calls:
            f.write(call + '\n')

if __name__ == "__main__":
    # Root directory where the script is located
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate the applyCoinEntriesToTable calls
    apply_calls = generate_apply_coin_entries_calls(root_dir)
    
    # Output file to write the generated code
    output_file = os.path.join(root_dir, "generated_apply_calls.txt")
    
    # Write the calls to the output file
    write_to_file(apply_calls, output_file)
    
    print(f"Generated {len(apply_calls)} applyCoinEntriesToTable calls.")
    print(f"Output written to: {output_file}")
