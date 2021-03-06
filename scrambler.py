import argparse
import random
from os.path import exists

parser = argparse.ArgumentParser()
parser.add_argument('MapList', help='Path to the map list that you want to use with the scrambler')
parser.add_argument('ServerFile', help='Path to the server startup file or the file which contains the map list')
parser.add_argument('-PreArg', help='Arguments that go before the map list')
parser.add_argument('-PostArg', help='Arguments that go after the map list')
parser.add_argument('-p', '--prefix', help='Prefix for map names. E.g. mp [mapName]')
parser.add_argument('-v', '--verbose', help='Enables verbose output', action='store_true')

args = parser.parse_args()

maps = {}
mapList = {}

if not exists(args.MapList):
    print('Your map file ', args.MapFile, ' does not exist.')
else:
    mapFile = open(args.MapList, 'r').read()
    if not exists(args.ServerFile):
        print('Your server file', args.ServerFile, 'does not exist. Creating the file now.')
    serverFile = open(args.ServerFile, 'w')
    mapFile = mapFile.split('\n')
    size = len(mapFile)
    for currMap in mapFile:
        currMap = currMap.split(',')
        maps[currMap[1]] = currMap[0]
        index = random.randint(0, size)
        while index in mapList:
            index = random.randint(0, size)
        mapList[index] = currMap[1]
    print('Maps have been scrambled!')

