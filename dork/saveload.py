# Generously inspired by our LA,
# https://github.com/LSmith-Zenoscave

from pprint import pprint
import yaml

ITEMDATA = ["holds"]
DIRECTIONS = ["north", "south", "east", "west"]

def _load(file_name = "./dork/yaml/dork.yml"):
    with open(file_name) as file:
        data = yaml.safe_load(file.read())

    return data

def _save():
    # Decide how to format save data
    # For now we have a test dork.yml file
    return

def _item(items, name, idata):
    item = items[name]
    if idata not in item:
        print(f"{name} does not have {idata} as a key.")
    elif item[idata] is None:
        print(f"There are no items in {name}.")
    else:
        other = item[idata]
        print(f"{other} is in {name}.")

def _path(rooms, name, direction):
    room = rooms[name]
    if direction not in room:
        print(f"{name} does not have {direction} as a key.")
    elif room[direction] is None:
        print(f"There is nothing {direction} of {name}.")
    elif room[direction] not in rooms:
        print(f"Going {direction} from {name} will lead to an error.")
    else:
        other = room[direction]
        print(f"{other} is {direction} of {name}.")

def main():
    data = _load()
    print("Data that was loaded:")
    pprint(data)

    print("Checking room and item list...")
    if "Rooms" not in data:
        print("No rooms found.")
        return

    if "Items" not in data:
        print("No items found.")
        return

    if not isinstance(data["Rooms"], dict):
        print("Rooms in data were not proper data.")
        return

    if not isinstance(data["Items"], dict):
        print("items in data were not proper data.")
        return

    rooms = data["Rooms"]
    for name in rooms:
        for direction in DIRECTIONS:
            _path(rooms, name, direction)

    items = data["Items"]
    for name2 in items:
        for idata in ITEMDATA:
            _item(items, name2, idata)

if __name__ == "__main__":
    main()