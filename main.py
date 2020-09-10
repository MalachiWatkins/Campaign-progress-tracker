import re
import os
import math
from fractions import Fraction
# from tkinter import *
with open('log.txt') as logfile:
    reg = " ........ ......... ... .INFO Client ....] : You have entered (.*?)\\n"
    regDate = "2020.08.31"
    regex = r"" + regDate + reg
    Log = str(logfile.read())  # reads file
    # matches for current regex in file
    matches = re.findall(regex, Log, re.MULTILINE)
    matchLen = (len(matches))  # number of matches
    matchlen = matchLen - 1
    # percent = int(round(percent, 2))
    # if percent == 84:
    #     percent = percent + 16
Act1_2_3_4_5 = {
    1: "Lioneye's Watch",
    2: "The Coast.",
    3: "Mud Flats",
    4: "Tidal Island",
    5: "Submerged Passage",
    6: "The Ledge",
    7: "Flooded Depths",
    8: "The Climb",
    9: "The Lower Prison",
    10: "The Upper Prison",
    11: "Prisoner's Gate",
    12: "The Ship Graveyard",
    13: "The Cavern of Wrath",
    14: "The Cavern of Anger",
    15: "The Southern Forest",
    16: "The Old Fields",
    17: "The Crossroads",
    18: "The Chamber of Sins Level 1",
    19: "The Chamber of Sins Level 2",
    20: "Broken Bridge",
    21: "The Riverways",
    22: "The Western Forest",
    23: "Weavers Chambers",
    24: "The Wetlands",
    25: "The Vaal Ruins",
    26: "The Northern Forest",
    27: "The Caverns",
    28: "Ancient pyramid",
    29: "The City of Sarn",
    30: "The Slums",
    31: "The Crematorium",
    32: "The Sewers",
    33: "The Markteplace",
    34: "The Battlefront",
    35: "The Docks",
    36: "The Solaris Temple 1",
    37: "The Solaris Temple 2",
    38: "The Ebony Barracks",
    39: "Lunaris Temple 1",
    40: "Lunaris Temple 2",
    41: "Imperial Gardens",
    42: "The Sceptre of God",
    43: "Upper Sceptre of God",
    44: "The Aqueduct",
    45: "The Dried Lake",
    46: "The Mines 1",
    47: "The Mines 2",
    48: "The Crystal Veins",
    49: "Daresso's Dream",
    50: "The Grand Arena",
    51: "The Kaom's Dream",
    52: "The Kaom's Stronghold",
    53: "Belly of the Beast 1",
    54: "Belly of the Beast 2",
    55: "The Harvest",
    56: "The Ascent",
    57: "The Slave Pens",
    58: "The Control Blocks",
    59: "Oriath Square",
    60: "The Templar Courts",
    61: "Chamber of Innocence",
    62: "The Torched Courts",
    63: "The Ruined Square",
    64: "The Ossuary",
    65: "The Reliquary",
    66: "Cathedral Rooftop",
}


class Whileloops:
    def half1(self, x, length, act, percent):
        # global percent
        while x < length:
            for q in act:
                if matches[x] == act[q]:
                    # print('Match Found! ' + matches[x])

                    percent += 100 / 66
                    # percent = round(percent)
                    percent = round(percent, 1)
            x += 1
            if percent == 99.0:
                percent = percent + 1

        return percent


def firsthalf():
    firstmatch = Whileloops()
    firstmatch.half1(x=0, length=matchLen, act=Act1_2_3_4_5, percent=0)


firsthalf()


# Second half
Act_6 = {
    1: "The Twilight Strand",
    2: "The Coast",
    3: "The Mud Flats",
    4: "The Karui Forest",
    5: "The Ridge",
    6: "The Lower Prison",
    7: "Shavronne's Tower",
    8: "Prisoner's Gate",
    9: "The Western Forest",
    10: "The Riverways",
    11: "The Wetlands",
    12: "The Southern Forest",
    13: "The Cavern of Anger",
    14: "The Beacon",
    15: "The Brine Kings's Reef",
}
Act_7 = {
    1: "The Broken Bridge",
    2: "The Crossroads",
    3: "The Fellshrine Ruins",
    4: "The Crypt 1",
    5: "The Crypt 2",
    6: "The Chamber of Sins 1",
    7: "Maligaro's Sanctum",
    8: "Chamber of Sins 2",
    9: "The Den",
    10: "The Ashen Fields",
    11: "The Northern Forest",
    12: "The Dread Thicket",
    13: "The Causeway",
    14: "The Vaal City",
    15: "The Temple of Decay",
}
Act_8 = {
    1: "The Sarn Ramparts",
    2: "The Toxic Conduits",
    3: "Doedre's Cesspool",
    4: "The Grand Promenade",
    5: "The Bath House",
    6: "The Lunaris Concourse",
    7: "The Lunaris Temple 1",
    8: "The Lunaris Temple 2",
    9: "The Quay",
    10: "The Grain Gate",
    11: "The Imperial Fields",
    12: "Solaris Temple 1",
    13: "Solaris Temple 2",
    14: "Harbour Bridge",
    15: "Got Instance Details from login server",
}
Act_9 = {
    1: "The Blood Aqueduct",
    2: "The Descent",
    3: "The Vastiri Desert",
    4: "The Oasis",
    5: "The Foothills",
    6: "The Boiling Lake",
    7: "The Tunnel",
    8: "The Quarry",
    9: "Shrine of The Winds",
    10: "The Refinery",
    11: "The Belly of the Beast",
    12: "Got Instance Details from login server",
    13: "Got Instance Details from login server",
    14: "Got Instance Details from login server",
    15: "Got Instance Details from login server",
}
Act_10 = {
    1: "The Cathedral Rooftop",
    2: "The Ravaged Square",
    3: "The Ossuary",
    4: "The Torched Courts",
    5: "The Desecrated Chambers",
    6: "The Reliquary",
    7: "The Control Blocks",
    8: "The Canals",
    9: "The Feeding Trough",
    10: "Got Instance Details from login server",
    11: "Got Instance Details from login server",
    12: "Got Instance Details from login server",
    13: "Got Instance Details from login server",
    14: "Got Instance Details from login server",
    15: "Got Instance Details from login server",
}
