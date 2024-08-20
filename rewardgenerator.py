import os  # This is a module that allows us to interact with the operating system, such as creating folders.
import json  # This module helps us work with JSON data, which is a way to store information.
import random  # This module allows us to generate random numbers or pick random things, like flipping a coin.
import uuid  # This module is used for generating unique identifiers, which can help ensure that certain values are unique.

def generate_hex_id():
    """Generate a random 8-character hexadecimal string."""
    # This function creates a random string of 8 characters using numbers (0-9) and letters (a-f). 
    # A "hexadecimal string" is just a fancy way to say a sequence of characters that includes 0-9 and a-f.
    return ''.join(random.choice('0123456789abcdef') for _ in range(8))

def generate_quests(fragments, coin_start_id=100, output_dir="quests"):
    # This function is designed to create a series of quests. 
    # "fragments" is a list of different types of charm fragments (like "Zombie" or "Skeleton").
    # "coin_start_id=100" is a starting point for numbering coins (we’re not using this directly in this version).
    # "output_dir" is the name of the folder where we want to save the quests. 

    # The next line checks if the "output_dir" folder exists. 
    # If it doesn’t exist, it creates it. This is where our quest files will be saved.
    os.makedirs(output_dir, exist_ok=True)

    # This line starts a loop to go through each item in the "fragments" list one by one.
    for i, fragment in enumerate(fragments):
        # For each "fragment", we create a dictionary (a way to store key-value pairs, like a list of instructions).
        quest = {
            "title": fragment + " Charm [1 Enderium Coin]",  # This sets the "title" of the quest using the fragment name.
            "icon": f"xreliquary:mob_charm_fragment:{i}",  # This sets an icon for the quest, linking it to a game item.
            "x": i * 2.0,  # This determines where the quest will be positioned on a 2D grid (left-right axis).
            "y": 0.0,  # This determines the position on the up-down axis (y-axis is constant here).
            "optional": True,  # This indicates that this quest is optional, not required.
            "tasks": [{
                # Tasks are things the player needs to do. This task requires the player to collect an item.
                "uid": generate_hex_id(),  # We use the "generate_hex_id" function to create a unique ID for this task.
                "type": "item",  # The task type is "item", meaning the player needs to collect an item.
                "items": [{
                    "item": f"thermalfoundation:coin 103"  # This specifies the item the player needs to collect.
                }],
                "consume_items": True  # This means the item will be used up when completing the quest.
            }],
            "rewards": [{
                # Rewards are what the player gets after completing the tasks.
                "uid": generate_hex_id(),  # We generate another unique ID for this reward.
                "type": "item",  # The reward is also an item.
                "item": f"xreliquary:mob_charm_fragment:{i}"  # This specifies the reward item.
            }]
        }

        # The next step converts the quest dictionary into a format called SNBT, which is just a structured way to save this data.
        snbt_content = json.dumps(quest, indent=4)

        # Now we save the quest to a file. We give the file a random name using our "generate_hex_id" function.
        filename = f"{generate_hex_id()}.snbt"
        filepath = os.path.join(output_dir, filename)  # This creates the full path to where the file will be saved.
        with open(filepath, "w") as file:  # This opens the file to write our quest data into it.
            file.write(snbt_content)  # This writes the quest data to the file.

        # Finally, we print out a message telling us the quest file was generated successfully.
        print(f"Generated {filepath}")

# Below is the list of different "fragments" or charm types that we want to make quests for.
fragments = [
    "Zombie",  # A charm for zombies
    "Skeleton",  # A charm for skeletons
    "Wither Skeleton",  # A charm for wither skeletons
    "Creeper",  # A charm for creepers
    "Witch",  # A charm for witches
    "Zombie Pigman",  # A charm for zombie pigmen
    "Cave Spider",  # A charm for cave spiders
    "Spider",  # A charm for spiders
    "Enderman",  # A charm for endermen
    "Ghast",  # A charm for ghasts
    "Slime",  # A charm for slimes
    "Magma Cube",  # A charm for magma cubes
    "Blaze",  # A charm for blazes
    "Guardian"  # A charm for guardians
]

# Now we call the function to actually create the quests using our list of fragments.
generate_quests(fragments)
