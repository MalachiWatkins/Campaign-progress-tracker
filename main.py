from tkinter import *
from fractions import Fraction
import math
import os
import re
# TODO
# 1: clean up code and comment as of now
# 2: finish basic gui and get percentages working

# must add encoding='utf-8' to open args for app to work with windows
with open('log.txt') as logfile:
    reg = " ........ ......... ... .INFO Client ....] : You have entered (.*?)\\n"
    regDate = "2020.08.31"
    regex = r"" + regDate + reg
    Log = str(logfile.read())  # reads file
    # matches for current regex in file
    matches = re.findall(regex, Log, re.MULTILINE)
    matchLen = (len(matches))  # number of matches
    matchlen = matchLen - 1
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
Act_6_7_8_9_10 = {
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
    16: "The Broken Bridge",
    17: "The Crossroads",
    18: "The Fellshrine Ruins",
    19: "The Crypt 1",
    20: "The Crypt 2",
    21: "The Chamber of Sins 1",
    22: "Maligaro's Sanctum",
    23: "Chamber of Sins 2",
    24: "The Den",
    25: "The Ashen Fields",
    26: "The Northern Forest",
    27: "The Dread Thicket",
    28: "The Causeway",
    29: "The Vaal City",
    30: "The Temple of Decay",
    31: "The Sarn Ramparts",
    32: "The Toxic Conduits",
    33: "Doedre's Cesspool",
    34: "The Grand Promenade",
    35: "The Bath House",
    36: "The Lunaris Concourse",
    37: "The Lunaris Temple 1",
    38: "The Lunaris Temple 2",
    39: "The Quay",
    40: "The Grain Gate",
    41: "The Imperial Fields",
    42: "Solaris Temple 1",
    43: "Solaris Temple 2",
    44: "Harbour Bridge",
    45: "The Blood Aqueduct",
    46: "The Descent",
    47: "The Vastiri Desert",
    48: "The Oasis",
    49: "The Foothills",
    50: "The Boiling Lake",
    51: "The Tunnel",
    52: "The Quarry",
    53: "Shrine of The Winds",
    54: "The Refinery",
    55: "The Belly of the Beast",
    56: "The Cathedral Rooftop",
    57: "The Ravaged Square",
    58: "The Ossuary",
    59: "The Torched Courts",
    60: "The Desecrated Chambers",
    61: "The Reliquary",
    62: "The Control Blocks",
    63: "The Canals",
    64: "The Feeding Trough",
}

# gui for app


def gui(percentage):
    master = Tk()
    PercentageFirsthalf = "percentage of Campaign first half Completed", percentage
    master.minsize(width=300, height=50)
    Perc1 = Lable(master, text=PercentageFirsthalf)
    Perc1.pack()
    mainloop()
    return


def half1(length):
    act1 = Act1_2_3_4_5
    percent = 0
    x = 0
    while x < length:
        x += 1
        for q in act1:
            if matches[x] == act1[q]:
                print(matches[x])
                percent += 100 / 66
                percent = round(percent)
        if percent > 100:
            percent = 100

            # gui(percentage=percent)
    print(percent)
    return


def half2(length):
    act2 = Act_6_7_8_9_10
    percent = 0
    x = 0
    while x < length:
        for q in act2:
            if matches[x] == act2[q]:
                # print(matches[x])
                percent += 100 / 64
                percent = round(percent, 1)
        x += 1
        if percent > 100:
            percent = 100
    print(percent)
    return


half1(length=matchlen)
half2(length=matchlen)
