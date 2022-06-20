# SWBF2_Lan_Server_Setup
Simple script to change options flags for running Star Wars Battlefront 2 Lan server as a .bat

Simple script to generate a Bat file from the options selected using the Star Wars Battlefront II Dedicated Service Management
The Dedicated server exe is 'DSManager.exe'. MFC71.dll and msvcr71.dll are needed for the executable

# Instructions:
1. Choose settings using the server manager, click 'START' to generate the settings file (DSManager.ini)
2. Run this script. It will generate a new .bat file with those settings in the parent directory
3. Launch the bat file from the same directory as the game* and a simple server version of the game will pop up
4. To play, launch a new instance** of the game and join from there.
    
*Note: The bat file needs to be in the same directory as the cracked SWBF2. I've tested it, it doesn't
    work with the original CD version, nor the official Steam or GOG games, it needs to be the cracked one.

**Note: If you are launching the cracked version to play, create a copy in another directory and launch from there
    If not, after the server playlist is over and you want to launch a new server, you'd need to exit out of the cracked version
    To reiterate, after starting the server, launch a Steam or GOG version, or a cracked version from a different directory to play

# Known issues/ Needed features
Units: The argument -u for units is a blanket statement and each game in the queue will have the
        same value. Can be changed with the '*' flag and adding functionality to parse through the list

hrrespawn: I couldn't deduce what this setting does nor how it's changed. Currently hard coded to 2

Default directory: Implementation is setup that the bat file is saved in the above directory, flags can be added to change that.