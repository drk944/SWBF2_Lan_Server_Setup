# Simple script to generate a Bat file from the options selected using the Star Wars Battlefront II Dedicated Service Management
# The Dedicated server exe is 'DSManager.exe'
# View README for instructions
# Author: drk944
#
# How to run: python3 bat_generator.py <new_filename (don't include.bat)> --tps <ticks per second> --units <number of units per side>

import configparser
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-u", "--units", help="Number of units on a side (default 200)", nargs='?')
parser.add_argument(
    "-t", "--tps", help="Set Server Ticks Per Second (TPS) (default 60)", nargs='?')
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

exec = c['APP_FILENAME'] + ' ' + cl_basic + ' /gamename ' + c['SESSION_NAME'] + ' /tps ' + str(tps) + ' /playerlimit ' + c['MAX_PLAYERS'] \
    + ' /playercount ' + c['START_PLAYERS'] + ' /bots ' + c['AI_UNITS'] + '  /sideselect' + ' /difficulty ' + str(int(c['AI_DIFFICULTY'])+1) \
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
filename = "../" + filename
with open(filename, 'w') as f:
    f.write(exec)
