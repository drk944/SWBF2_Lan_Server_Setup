# Simple script to generate a Bat file from the options selected using the Star Wars Battlefront II Dedicated Service Management
# The Dedicated server exe is 'DSManager.exe'. MFC71.dll and msvcr71.dll are needed for the executable

# Instructions:
# 1. Choose settings using the server manager, click 'START' to generate the settings file (DSManager.ini)
# 2. Run this script. It will generate a new .bat file with those settings in the current directory
# 3. Run the bat file and a simple server version of the game will pop up, you can then launch a new instance
# of the game and join from there.

# *Note: The bat file needs to be in the same directory as the cracked SWBF2. I've tested it, it doesn't
# work with the original CD version, nor the official Steam or GOG games, it needs to be the cracked one.

### Known issues ###
# Units: The argument -u for units is a blanket statement and each game in the queue will have the
#        same value. Can be changed with the '*' flag and adding functionality to parse through the list

# hrrespawn: I couldn't deduce what this setting does nor how it's changed. Currently hard coded to 2

# Default directory: Implementation is needed to move the bat file to a different directory.
import configparser
import argparse

parser = argparse.ArgumentParser()


parser.add_argument(
    "-u", "--units", help="Number of units on a side (default 200)", nargs='?')
parser.add_argument(
    "-t", "--tps", help="Set Server TPS (default 60)", nargs='?')
parser.add_argument(
    'filename', help="Name of Bat file to be generated", nargs='+')

args = parser.parse_args()

filename = args.filename[0]

if args.units == None:
    units = 200
else:
    units = args.units

if args.tps == None:
    tps = 60
else:
    tps = args.tps

config = configparser.ConfigParser()
config.read('DSManager.ini')
bat = [None] * 18
c = config['SESSION1']
cl_basic = '/win /nosound /autonet dedicated /resolution 640 480'

exec = c['APP_FILENAME'] + ' ' + cl_basic + ' /gamename ' + c['SESSION_NAME'] + ' /tps ' + tps + ' /playerlimit ' + c['MAX_PLAYERS'] \
    + ' /playercount ' + c['START_PLAYERS'] + ' /bots ' + c['AI_UNITS'] + '/sideselect' + ' /difficulty ' + str(int(c['AI_DIFFICULTY'])+1) \
    + ' /heroes ' + c['HEROES'] + ' /hrunlock ' + c['HERO_UNLOCK_RULE'] + ' /hrplayer ' + c['HERO_ASSIGN_RULE'] \
    + ' /hrteam ' + c['HERO_UNLOCK_TEAM'] + ' /hrrespawn 2' + ' /hrrespawnvalue ' + c['HERO_RESPAWN_TIMER'] \
    + ' /pregametime ' + c['WARMUP_TIMER'] + \
    ' /throttle 6144' + ' /lan' + ' /spawn ' + c['SPAWN_INVIC']

# Now to add the maps
maps = c['MAPS'].split()
map_string = ""
for i in maps:
    map_string += (' ' + i + ' ' + str(units) + ' ' + str(units))
exec += map_string

filename += '.bat'
with open(filename, 'w') as f:
    f.write(exec)
