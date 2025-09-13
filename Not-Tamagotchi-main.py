import time
import os
from pet import notTamagotchi

def clear_screen():
    """Clears the console for a clean display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    pet_name = input("Give your new pet a name: ")
    my_pet = notTamagotchi(pet_name)

    while my_pet.alive:
        clear_screen()
        print("****************************")
        print(f"       Meet {my_pet.name}       ")
        print("****************************")
        print("\n")
        print(f"Status: {my_pet.get_status()}")
        print(f"Hunger: {my_pet.hunger}")
        print(f"Happiness: {my_pet.happiness}")
        print("\n")
        
        print("What would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Wait (pass time)")
        
        choice = input("> ")
        
        if choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.play()
        elif choice == "3":
            pass # The clock_tick will handle this
        else:
            print("Invalid choice.")
        
        my_pet.clock_tick()
        time.sleep(1) # Pauses the game for a second

    clear_screen()
    print("****************************")
    print("        Game Over!          ")
    print("****************************")
    print(f"\nYour pet, {my_pet.name}, has passed away.")

if __name__ == "__main__":
    main()
