import random

def play_game():
    print("🚪 Welcome to the Door Challenge!")
    print("You stand before 3 mysterious doors...")
    print("Choose wisely — one leads to treasure, one to safety, and one to a trap!")
    
    while True:
        try:
            choice = int(input("Pick a door (1, 2, or 3). Enter 0 to quit: "))
        except ValueError:
            print("⚠️ Please enter a valid number (1, 2, 3, or 0).")
            continue

        if choice == 0:
            print("👋 Thanks for playing. Goodbye!")
            break
        
        if choice not in [1, 2, 3]:
            print("⚠️ Invalid door number. Please choose 1, 2, or 3.")
            continue
        
        outcome = random.choice(["treasure", "safe", "trap"])
        
        if outcome == "treasure":
            print(f"🎉 You opened door {choice} and found a chest of gold! 💰")
        elif outcome == "safe":
            print(f"😊 You opened door {choice} and found a quiet empty room. You're safe!")
        else:
            print(f"💀 You opened door {choice} and fell into a trap! Game over!")
            break
        
        print("-" * 30)

if __name__ == "__main__":
    play_game()
