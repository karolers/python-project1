objects =["lock", "gun", "toilet", "bathtub", "prisoner", "dead man", "leg", "door"]

objectText={
    "tape": "You may find a way out where the heart doesn't beat",
    "note": "Now you have to convince the other prisoner to give you the key for the chain lock!",
    "saw": "It's not a key!! But you got an Hacksaw - so be a man, and cut your leg",
    "key": "Good for you, unlock your chain!"
}

examined_item={
    "gun": "the gun. ",
    "toilet": "the toilet. ",
    "saw": "a saw. ",
    "note": "a note. ",
    "tape": "a tape. ",
    "lock": "your lock. ",
    "bathtub": "the bathtub. ",
    "prisoner": "the prisoner. ",
    "dead man": "the dead man. ",
    "leg": "your leg. ",
    "door": "the door. "
}

narration={
    "start": "You wake up on a bathroom locked by a chain. You don't remember why you are here and what had happened before. \nIt's dark and you see almost nothing you must figure out how get out of there, NOW!",
    "light switch": "You found a light switch, turn on the lights! ",
    "advice": "What would you like to do? Try to 'explore' or to 'examine' what's around you.",
    "lights off": "Not sure what you mean. Type: 'turn on the lights!'",
    "lights on": "You turned on the lights. Now you can look around.",
    "choice": "What would you like to examine?",
    "wrong input": "Not sure what you mean. Try to 'explore' or 'examine' anything.",
    "no item": "You look around, but can't find anything similar to it.",
    "explore": "You explored the room. You find ",
    "examine": "You examined ",
    "find"  : "You found ",
    "door": "You're out. I wonder if you'll come back for him...",
    "fail": "There isn't anything interesting about it.",
    "free": "Congratulations! You escaped the bathroom! You are free.",
    "unlock": "You unlocked the chain on your ankle. ",
    "cut": "You cut your own leg, but at least you can escape now. ",
    "no info": "You're missing some tips, explore some more and then come back!"

}

dialogue={
    "prisoner": "Here, I'll give you the key. But please don't forget me here!"
}

def getExplore():
    print(narration["explore"]+ ", ".join(objects))

def getObjectText(objectKey):
    return objectText[objectKey]

def getNarration(dict_key, object=None):
    output=""
    output+= narration[dict_key]

    if (object =="tape") | (object=="note") | (object=="key") | (object=="saw"):
        output+=examined_item[object]+". "+ objectText[object]
    elif(object!=None and dict_key=="examine"):
        output+=examined_item[object]
    return output

def getDialogue(dict_key):
    return dialogue[dict_key]
