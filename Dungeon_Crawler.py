import random

def encounter():
    events = [
        "a wild goblin attacks! 🗡",
        "you find a healing potion. 🧪 +10 HP",
        "a hidden trap triggers! 💥 -10 HP",
        "you discover a treasure chest! 💰 +50 gold",
        "an empty, eerie room... 😶"
    ]
    return random.choice(events)

def play_game():
    hp = 50
    gold = 0
    room = 1
    
    print("🏰 Welcome to the Dungeon Crawler!")
    print("Explore rooms, survive dangers, and collect treasure!")
    print("Commands: 'forward' to move, 'quit' to exit.\n")

    while hp > 0:
        command = input(f"Room {room} — what will you do? ").strip().lower()
        
        if command == "quit":
            print("👋 You leave the dungeon. Final stats:")
            print(f"❤️ HP: {hp}, 💰 Gold: {gold}, 🏠 Rooms explored: {room - 1}")
            break
        elif command == "forward":
            event = encounter()
            print(f"You enter the room... {event}")
            
            if "goblin" in event:
                damage = random.randint(5, 15)
                hp -= damage
                print(f"The goblin hits you for {damage} damage! ❤️ HP: {hp}")
            elif "healing potion" in event:
                heal = 10
                hp += heal
                print(f"You gain {heal} HP! ❤️ HP: {hp}")
            elif "trap" in event:
                damage = 10
                hp -= damage
                print(f"You take {damage} damage! ❤️ HP: {hp}")
            elif "treasure" in event:
                gold_gain = 50
                gold += gold_gain
                print(f"You gain {gold_gain} gold! 💰 Gold: {gold}")
            
            room += 1
        else:
            print("⚠️ Invalid command. Type 'forward' or 'quit'.")

    if hp <= 0:
        print("\n💀 You have perished in the dungeon!")
        print(f"💰 Gold collected: {gold}, 🏠 Rooms explored: {room - 1}")

if __name__ == "__main__":
    play_game()
