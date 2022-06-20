# SWBF2_Lan_Server_Setup
Simple script to change options flags for running Star Wars Battlefront 2 Lan server as a .bat

Simple script to generate a Bat file from the options selected using the Star Wars Battlefront II Dedicated Service Management
The Dedicated server exe is 'DSManager.exe'. MFC71.dll and msvcr71.dll are needed for the executable

# Instructions:
1. Choose settings using the server manager, click 'START' to generate the settings file (DSManager.ini)
2. Run this script. It will generate a new .bat file with those settings in the current directory
3. Run the bat file and a simple server version of the game will pop up, you can then launch a new instance
of the game and join from there.

*Note: The bat file needs to be in the same directory as the cracked SWBF2. I've tested it, it doesn't
 work with the original CD version, nor the official Steam or GOG games, it needs to be the cracked one.

# Known issues/ Needed features
Units: The argument -u for units is a blanket statement and each game in the queue will have the
        same value. Can be changed with the '*' flag and adding functionality to parse through the list

hrrespawn: I couldn't deduce what this setting does nor how it's changed. Currently hard coded to 2

Default directory: Implementation is needed to move the bat file to a different directory.
