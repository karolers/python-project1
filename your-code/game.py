# define rooms and items
import random
import gametext
gun = {
    "name": "gun",
    "type": "furniture"
}

toilet = {
    "name": "toilet",
    "type": "furniture"
}

bathtub = {
    "name": "bathtub",
    "type": "furniture"
}

prisioner = {
    "name": "prisioner",
    "type": "door"
    }

dead_man = {
    "name": "dead man",
    "type": "door"
}

leg = {
    "name": "leg",
    "type": "door"
}

door = {
    "name": "door",
    "type": "door"
}

lock = {
    "name": "lock",
    "type": "door"
}

tape = {
    "name": "tape",
    "type": "key",
    "target": dead_man
}

note = {
    "name": "note",
    "type": "key",
    "target": prisioner
}

key = {
    "name": "key",
    "type": "key",
    "target": lock
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
  "type": "room"
}

outside = {
  "name": "outside"
}

all_rooms = [bathroom, outside]

all_doors = [door,dead_man,prisioner,leg,lock]

# define which items/rooms are related

object_relations = {
    "bathroom": [lock,gun,toilet,bathtub,prisioner,dead_man,leg,door],
    "outside": [door, freedom],
    "toilet": [tape],
    "prisioner": [key,saw],
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
        print(gametext.getObjectText("saw"))
        return True
    else:
        print(gametext.getObjectText("key"))
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
    print(gametext.getNarration("start"))
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    while game_state["light_on"] == False:
        intended_action = input("You found a light switch, turn on the lights!").strip()
        if intended_action == "turn on the lights!":
            game_state["light_on"] = True
            play_room(room)
        else:
            print("Not sure what you mean. type: 'turn on the lights!'")

        intended_action = input(gametext.getNarration("advice")).strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input(gametext.getNarration("choice")).strip())
        else:
            print(gametext.getNarration("advice"))
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    gametext.getExplore()

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
            output = gametext.getNarration("examine", item["name"])

            if(item["type"] == "door"):   ### DOORS
                have_key = False

                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output+= gametext.getNarration(item["name"], item_found["name"])    

                        if item["name"] == 'lock':
                                output += gametext.getNarration("unlock")
                                game_state["keys_collected"].append(free)
                            
                        if item["name"] == 'leg':
                                output += gametext.getNarration("cut")
                                game_state["keys_collected"].append(free)
                            
                        if item["name"] == 'door':
                                print(gametext.getNarration("free"))
                                os._exit(0)
                else:
                    output += gametext.getNarration("fail")

            else:      #### FURNITURE WITH KEYS
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output+= gametext.getNarration(item["name"], item_found["name"])
                else:      #### FURNITURE WITH NOTHING
                    output += gametext.getNarration("fail")

            print(output)
            break

    if(output is None):
        print(gametext.getNarration("no item"))

    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()

start_game()