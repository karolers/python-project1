objects =["lock", "gun", "toilet", "bathtub", "prisioner", "dead man", "leg", "door"]

objectText={
    "tape": "You may find a way out where the heart doesn't beat",
    "note": "Now you have to convince the other prisioner to give you the key for the chain lock!",
    "saw": "It's not a key!! But you got an Hacksaw - so be a man, and cut your leg",
    "key": "you got a key"
}

narration={
    "start": "You wake up on a bathroom locked by a chain. You don't remember why you are here and what had happened before. It's dark and you see almost nothing you must figure out how get out of there, NOW!",
    "light switch": "You found a light switch, turn on the lights! ",
    "advice": "What would you like to do? Try to 'explore' or to 'examine' what's around you.",
    "lights off": "Not sure what you mean. Turn on the lights!",
    "lights on": "You turned on the lights. Now you can look around.",
    "choice": "What would you like to examine?",
    "wrong input": "Not sure what you mean. Try to 'explore' or 'examine' anything.",
    "no item": "The item you requested is not found in the current room.",
    "explore": "You explored the room. You find ",
    "examine": "You examined ",
    "find"  : "You found a",
    "door": "You're out. I wonder if you'll come back for him...",
    "fail": "There isn't anything interesting about it.",
    "free": "Congrats! You escaped the bathroom! You are free.",
    "unlock": "You unlocked the chain on your ankle. ",
    "cut": "You cut your own leg, but at least you can escape now. ",
    "toilet": "toilet"

}

def getExplore():
    print(narration["explore"]+ ", ".join(objects))

def getObjectText(objectKey):
    return objectText[objectKey]

def getNarration(dict_key, object=None):
    output= narration[dict_key]

    if (object =="tape") | (object=="note") | (object=="key") | (object=="saw"):
        output+=object,". ", objectText(object)
    elif(object!=None):
        output+="the "+object+". "
    return output

