"""Haunted Mansion Rescue: a room-based command-line adventure game."""


def get_new_state(direction_from_user, current_room):
    """Update the player's room based on the direction they choose."""
    if direction_from_user in rooms[current_room]:
        return rooms[current_room][direction_from_user]

    print("Invalid move! You can't go that way.")
    return current_room


def show_status(current_room, inventory):
    """Display the player's current room, inventory, item, and available paths."""
    print(f"\nYou are currently in {current_room}.")

    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']} here.")
    else:
        print("There is no item in this room.")

    print(f"Your inventory: {inventory}")

    directions = [direction for direction in rooms[current_room] if direction != "item"]
    print(f"Available directions: {', '.join(directions)}")


def collect_item(current_room, inventory):
    """Collect the item in the current room when one is available."""
    if "item" in rooms[current_room]:
        item = rooms[current_room].pop("item")
        inventory.append(item)
        print(f"You picked up {item}!")


def main():
    """Run the Haunted Mansion Rescue game loop."""
    global rooms

    rooms = {
        "Great Hall": {
            "South": "Basement",
            "North": "Attic",
            "East": "Mudroom",
            "West": "Parlor",
        },
        "Mudroom": {"North": "Laboratory", "West": "Great Hall", "item": "Boots"},
        "Parlor": {"East": "Great Hall", "item": "Charm"},
        "Attic": {"South": "Great Hall", "East": "Study", "item": "Flashlight"},
        "Study": {"West": "Attic", "item": "Map"},
        "Laboratory": {"South": "Mudroom", "item": "Potion"},
        "Basement": {"North": "Great Hall", "East": "Dungeon", "item": "Key"},
        "Dungeon": {"West": "Basement", "item": "My Friend"},
    }

    print("\n=== Haunted Mansion Rescue ===")
    print("Explore the mansion, collect useful items, and rescue your friend.")

    while True:
        inventory = []
        current_room = "Great Hall"

        while True:
            show_status(current_room, inventory)

            direction = input(
                "\nEnter direction (North, South, East, West) or 'quit' to exit: "
            ).strip().capitalize()

            if direction == "Quit":
                print("Exiting the game.")
                return

            current_room = get_new_state(direction, current_room)
            collect_item(current_room, inventory)

            if current_room == "Dungeon":
                if "My Friend" in inventory:
                    print("You found your friend and defeated the ghost!")
                    break

                print("You encountered the ghost without what you needed and lost!")
                return

        restart = input("Do you want to restart the game? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
