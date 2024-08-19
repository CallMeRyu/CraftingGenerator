// This is a script for adding coins to various loot tables in Minecraft. 
// The script is written using CraftTweaker and LootTweaker, mods for Minecraft that allow you to modify loot tables and item stacks.
// This script specifically adds 4 different types of coins (Copper, Iron, Silver, Gold) to various loot pools in the game.

// --------------------------------------------------------------
// If you use this with LootTableDumpCompiler.py and read the instructions on it, you will thank me. 
// --------------------------------------------------------------

// If you know how to edit code, feel free to use this script! 
// All that I ask is that you give me some credit, as this took longer than it should have to figure out. 
// Currently, as mentioned before, it adds 4 different coins into loot tables.

// Import necessary libraries and classes for the script to work.
import crafttweaker.item.IItemStack;        // Handles item stacks in Minecraft.
import loottweaker.LootTweaker;             // Main class to interact with loot tables.
import loottweaker.LootTable;               // Represents a loot table.
import loottweaker.LootPool;                // Represents a pool within a loot table.
import loottweaker.Functions;               // Allows you to apply functions to loot entries (e.g., setting item count).

// #ignoreBracketErrors is a special directive that tells the script to ignore certain errors, 
// specifically related to item brackets, which can happen if the items are not correctly referenced.
#modloaded loottweaker

// This is the main function where coins are added to a given loot pool.
// A function in programming is a reusable block of code that performs a specific task.
function addCoinEntries(pool as LootPool) {

    // Define the item stacks. This is where we specify the coins we want to add to the loot tables.
    // 'val' is short for 'value'. It's used to declare a variable that can't be changed later.
    // In this context, we're defining the specific coins using their mod:item syntax.
    val teCoinCopper = <thermalfoundation:coin:64>;   // Copper Coin
    val teCoinIron   = <thermalfoundation:coin>;      // Iron Coin
    val teCoinSilver = <thermalfoundation:coin:66>;   // Silver Coin
    val teCoinGold   = <thermalfoundation:coin:1>;    // Gold Coin

    // Define the rarity values for each coin type.
    // Rarity values are set using the Functions.setCount() method, which defines the min and max count of items.
    // This effectively determines how many of each coin can spawn in a loot chest.
    val CopperRarity = Functions.setCount(1, 5);      // Copper can appear in stacks of 1 to 5.
    val IronRarity   = Functions.setCount(1, 4);      // Iron can appear in stacks of 1 to 4.
    val SilverRarity = Functions.setCount(0, 3);      // Silver can appear in stacks of 0 to 3 (0 means it may not appear at all).
    val GoldRarity   = Functions.setCount(0, 2);      // Gold can appear in stacks of 0 to 2.

    // Now we add these items to the loot pool.
    // The numbers (150, 80, 40, 10) represent the weight of each item. 
    // A higher weight means the item is more likely to appear in the loot chest.
    pool.addItemEntry(teCoinCopper, 150, 0, [CopperRarity], [], "thermal_coin_entryCopper");
    pool.addItemEntry(teCoinIron,   80, 0, [IronRarity],   [], "thermal_coin_entryIron");
    pool.addItemEntry(teCoinSilver, 40, 0, [SilverRarity], [], "thermal_coin_entrySilver");
    pool.addItemEntry(teCoinGold,   10, 0, [GoldRarity],   [], "thermal_coin_entryGold");

    // Finally, we set the number of times the loot pool is rolled. 
    // This determines how many items from the pool will actually be chosen when the chest is opened.
    pool.setRolls(1, 3);  // The pool will roll between 1 and 3 times.
}

// This is a helper function to simplify the process of applying the coin entries to a specific loot table and pool.
// When you have multiple loot tables and pools, instead of rewriting the same code multiple times, 
// you can just call this function with the specific loot table and pool names.
function applyCoinEntriesToTable(lootTableName as string, poolName as string) {
    // This gets the specific loot pool from the given loot table.
    val pool = LootTweaker.getTable(lootTableName).getPool(poolName);
    // This then calls the addCoinEntries function we defined earlier to add the coins to this pool.
    addCoinEntries(pool);
}

// The following section is where you actually apply the coins to various loot tables and pools in the game.
// If you want to add the coins to additional loot tables, you can simply add more calls to applyCoinEntriesToTable().
// You can get the list of available loot tables by running the command "/ct loottables all" in-game.
// This will give you a link where you can view all the loot tables that you can modify.

// The following are examples of how to apply the coins to various loot tables and pools in the game:

// Vanilla Minecraft Loot Tables
applyCoinEntriesToTable("minecraft:chests/simple_dungeon", "main");
applyCoinEntriesToTable("minecraft:chests/nether_bridge", "main");
applyCoinEntriesToTable("minecraft:chests/jungle_temple", "main");
applyCoinEntriesToTable("minecraft:chests/desert_pyramid", "main");
applyCoinEntriesToTable("minecraft:chests/abandoned_mineshaft", "main");
applyCoinEntriesToTable("minecraft:chests/village_blacksmith", "main");
applyCoinEntriesToTable("minecraft:chests/stronghold_crossing", "main");
applyCoinEntriesToTable("minecraft:chests/stronghold_corridor", "main");
applyCoinEntriesToTable("minecraft:chests/woodland_mansion", "main");

// Dungeon Tactics Mod Loot Tables
applyCoinEntriesToTable("dungeontactics:loot_bags/arbour_bag", "main");
applyCoinEntriesToTable("dungeontactics:loot_bags/book_bag", "main");
applyCoinEntriesToTable("dungeontactics:loot_bags/food_bag", "main");
applyCoinEntriesToTable("dungeontactics:loot_bags/magic_bag", "main");
applyCoinEntriesToTable("dungeontactics:loot_bags/mystery_bag", "pools");
applyCoinEntriesToTable("dungeontactics:loot_bags/potion_bag", "main");
applyCoinEntriesToTable("dungeontactics:loot_bags/solstice_bag", "main");

// Treasures2 Mod Loot Tables
applyCoinEntriesToTable("treasure2:chests/common/general_chest", "treasure");
applyCoinEntriesToTable("treasure2:chests/epic/general_chest", "treasure");
applyCoinEntriesToTable("treasure2:chests/legendary/general_chest", "treasure");
applyCoinEntriesToTable("treasure2:chests/mythical/general_chest", "treasure");
applyCoinEntriesToTable("treasure2:chests/rare/general_chest", "treasure");
applyCoinEntriesToTable("treasure2:chests/scarace/general_chest", "treasure");
applyCoinEntriesToTable("treasure2:chests/special/general_chest", "treasure");
applyCoinEntriesToTable("treasure2:chests/uncommon/general_chest", "treasure");

// If you want to add the coins to additional mods or custom loot tables, just follow this format:
// applyCoinEntriesToTable("modid:loot_table_name", "pool_name");
// Where "modid" is the mod ID, "loot_table_name" is the specific loot table, and "pool_name" is the pool within that loot table.
