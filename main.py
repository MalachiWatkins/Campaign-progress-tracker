import re
import os

with open('log.txt') as logfile:
    regex = r"2020.08.20 ..:..:.. ..............\WINFO Client .......: (.*?)\n"
    Log = str(logfile.read())  # reads file
    # matches for current regex in file
    matches = re.findall(regex, Log, re.MULTILINE)
    matchLen = (len(matches))  # number of matches

WhileMatchLen = matchLen + 1
MatchWhile = WhileMatchLen

while MatchWhile < matchLen:  # Global while for looping with matches###
    MatcheNum = MatchWhile
    MatchWhile += 1
Act1 = {
    1: "You have entered Lioneye's Watch,",
    2: "You have entered The Coast.",
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
    15: 'Got Instance Details from login server'
}

Whilenum = 1
while Whilenum < 3:
    num = Whilenum
    Whilenum += 1
    if matches[3] == Act1[num]:  # Loop Through the Dict of act 1####
        print('yes')
    else:
        print('no')
Act2 = {
    1: "The Southern Forest",
    2: "The Old Fields",
    3: "The Crossroads",
    4: "The Chamber of Sins Level 1",
    5: "The Chamber of Sins Level 2",
    6: "Broken Bridge",
    7: "The Riverways",
    8: "The Western Forest",
    9: "Weavers Chambers",
    10: "The Wetlands",
    11: "The Vaal Ruins",
    12: "The Northern Forest",
    13: "The Caverns",
    14: "Ancient pyramid",
    15: 'Got Instance Details from login server'
}
Act3 = {
    1: "The City of Sarn",
    2: "The Slums",
    3: "The Crematorium",
    4: "The Sewers",
    5: "The Markteplace",
    6: "The Battlefront",
    7: "The Docks",
    8: "The Solaris Temple 1",
    9: "The Solaris Temple 2",
    10: "The Ebony Barracks",
    11: "Lunaris Temple 1",
    12: "Lunaris Temple 2",
    13: "Imperial Gardens",
    14: "The Sceptre of God",
    15: "Upper Sceptre of God"
}
Act4 = {
    1: "The Aqueduct",
    2: "The Dried Lake",
    3: "The Mines 1",
    4: "The Mines 2",
    5: "The Crystal Veins",
    6: "Daresso's Dream",
    7: "The Grand Arena",
    8: "The Kaom's Dream   ",
    9: "The Kaom's Stronghold  ",
    10: "Belly of the Beast 1",
    11: "Belly of the Beast 2",
    12: "The Harvest",
    13: "The Ascent",
    14: "Got Instance Details from login server",
    15: "Got Instance Details from login server"
}
Act5 = {
    1: "The Slave Pens",
    2: "The Control Blocks",
    3: "Oriath Square",
    4: "The Templar Courts",
    5: "Chamber of Innocence",
    6: "The Torched Courts",
    7: "The Ruined Square",
    8: "The Ossuary",
    9: "The Reliquary",
    10: "Cathedral Rooftop",
    11: "Got Instance Details from login server",
    12: "Got Instance Details from login server",
    13: "Got Instance Details from login server",
    14: "Got Instance Details from login server",
    15: "Got Instance Details from login server"
}

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

Act_names = {
    1: Act1,
    2: Act2,
    3: Act3,
    4: Act4,
    5: Act5,
}
Act_names2 = {
    1: Act_6,
    2: Act_7,
    3: Act_8,
    4: Act_9,
    5: Act_10,
}
