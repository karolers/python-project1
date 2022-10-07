# define rooms and items
import random
import os
#from winsound import PlaySound
import gametext as gt
import playsound 


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

prisoner = {
    "name": "prisoner",
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
    "msg":"You cut your own leg"
}

door = {
    "name": "door",
    "type": "door",
    "msg": " "
}

lock = {
    "name": "lock",
    "type": "door",
    "msg":"You unlocked the chain lock"
}

tape = {
    "name": "tape",
    "type": "key",
    "target": dead_man,
    "msg": "You might find a way out where the heart doesn't beat."
}

note = {
    "name": "note",
    "type": "key",
    "target": prisoner,
    "msg": "Now you have to convince the other prisoner to give you the key for the chain lock!"
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

freedom = {
    "name": "freedom",
    "type": "key",
    "target": door,
    "msg": " "
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

all_doors = [door,dead_man,prisoner,leg,lock]

# define which items/rooms are related

object_relations = {
    "bathroom": [lock,gun,toilet,bathtub,prisoner,dead_man,leg,door],
    "outside": [door, freedom],
    "toilet": [tape],
    "prisoner": [key,saw],
    "dead man": [note],
    "door": [bathroom,outside],
    "leg":[freedom],
    "lock":[freedom]

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
        print(gt.getObjectText("saw"))
        return True
    else:
        print(gt.getDialogue("prisoner"))
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
    print(gt.getNarration("start"))
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    while game_state["light_on"] == False:
        intended_action = input(gt.getNarration("light switch")).strip()
        if intended_action == "turn on the lights!":
            game_state["light_on"] = True
            play_room(room)
        else:
            print(gt.getNarration("lights off"))

    intended_action = input(gt.getNarration("advice")).strip()
    if intended_action == "explore":
        explore_room(room)
        play_room(room)
    elif intended_action == "examine":
        examine_item(input(gt.getNarration("choice")).strip())
    else:
        print(gt.getNarration("wrong input"))
        play_room(room)
    linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    print(gt.getExplore())

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
            output = gt.getNarration("examine", item_name)

            if(item["type"] == "door"):
                have_key = False

                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += gt.getNarration("find", item_found["name"])

                        if item["name"] == 'lock':
                            output = gt.getNarration("unlock")
                            game_state["keys_collected"].append(freedom)

                        if item["name"] == 'leg':
                            output = gt.getNarration("cut")
                            game_state["keys_collected"].append(freedom)

                        if item["name"] == 'door':
                            print(gt.getNarration("free"))
                            os._exit(0)
                            
                    else:
                        #print("Teste que mensagem extra apareceu para o :" item["name"])
                        output += item["msg"]
                else:
                    output += gt.getNarration("no info")

            else:      #### FURNITURE WITH KEYS
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += gt.getNarration("find", item_found["name"])
                else:      #### FURNITURE WITH NOTHING
                    output += gt.getNarration("fail")

            print(output)
            break

    if(output is None):
        print(gt.getNarration("no item"))

    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()


if __name__ == '__main__':
    playsound.playsound("saw.wav")
    start_game()