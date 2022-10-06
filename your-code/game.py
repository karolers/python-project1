# define rooms and items
import random
gun = {
    "name": "gun",
    "type": "furniture",
    "msg":" "
}

toilet = {
    "name": "toilet",
    "type": "furniture",
    "msg":" "
}

bathtub = {
    "name": "bathtub",
    "type": "furniture",
    "msg":" "
}

prisioner = {
    "name": "prisioner",
    "type": "door",
    "msg":" "
}

dead_man = {
    "name": "dead man",
    "type": "door",
    "msg":" "
}

leg = {
    "name": "leg",
    "type": "door",
    "msg":" "
}

door = {
    "name": "door",
    "type": "door",
    "msg": "You're out. I wonder if you'll come back for him..."
}

lock = {
    "name": "lock",
    "type": "door",
    "msg":" "
}

tape = {
    "name": "tape",
    "type": "key",
    "target": dead_man,
    "msg": "You might find a way out where the heat doesn't beat."
}

note = {
    "name": "note",
    "type": "key",
    "target": prisioner,
    "msg": "Now you have to convince the other prisioner to give you the key for the chain lock!"
}

key = {
    "name": "key",
    "type": "key",
    "target": lock,
    "msg": "Good for you, unlock your chain!"
}

saw = {
    "name": "saw",
    "type": "key",
    "target": leg,
    "msg": "Will you have the guts to cut your own leg? You can allways try a little bit harder to convince him!"
}

bathroom = {
  "name": "bathroom",
  "type": "room",
  "msg":" "
}

outside = {
  "name": "outside",
  "msg":" "
}

all_rooms = [bathroom, outside]

all_doors = [door,dead_man,prisioner,leg,lock]

# define which items/rooms are related

object_relations = {
    "bathroom": [lock,gun,toilet,bathtub,prisioner,dead_man,leg,door],
    "outside": [door],
    "lock": [key],
    "toilet": [tape],
    "leg": [saw],
    "prisioner": [key,saw],
    "dead man": [note],
    "door": [bathroom,outside],

}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": bathroom,
    "keys_collected": [],
    "target_room": outside,
    "light_on": False,
}

def lucky_key():
    dark_bag = {}
    if random.random() > 0.6:
        print("It's not a key!! But you got an Hacksaw - so be a man, and cut your leg")
        return True
    else:
        print("you got key")
        return True


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a bathroom locked by a chain. You don't remember why you are here and what had happened before. It's dark and you see almost nothing you must figure out how get out of there, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the bathroom!")
    else:
        while game_state["light_on"] == False:
            intended_action = input("You found a light switch, turn on the lights!").strip()
            if intended_action == "Turn on the lights!":
                game_state["light_on"] = True
                play_room(room)
            else:
                print("Not sure what you mean. Turn on the lights!")

        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explored the room. You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    output = None


    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examined " + item_name + ". "

            if(item["type"] == "door"):   ### DOORS
                have_key = False

                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "You find " + item_found["name"] + ". " + item_found["msg"]
                    else:
                        output += item_found["msg"]
                else:
                    output += "You're missing some tips, explore some more and then come back!"

            else:      #### FURNITURE WITH KEYS
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + ". " + item_found["msg"]
                else:      #### FURNITURE WITH NOTHING
                    output += "There isn't anything interesting about it."

            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")

    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()

start_game()