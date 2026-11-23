day = 1
gold = 50
energy = 30
hunger = 0
game_running = True

tomato_seeds = 0
corn_seeds = 0
strawberry_seeds = 0

# TODO: plots, watering days, watered-today flags, and harvested crops

def display_status():
    print("\n--------------------------------------------------")
    print(f"Day: {day} | Gold: {gold} | Energy: {energy} | Hunger: {hunger}/3")
    print("--------------------------------------------------")


def get_valid_choice(min_val, max_val):
    choice = -1
    valid = False
    while not valid:
        raw_input = input(">> ")
        if raw_input.isdigit():
            choice = int(raw_input)
            if min_val <= choice <= max_val:
                valid = True
            else:
                print(f"Invalid option. Please enter a number between {min_val} and {max_val}.")
        else:
            print(f"Invalid input. Please enter a valid number between {min_val} and {max_val}.")
    return choice


def get_positive_quantity(prompt_text):
    qty = 0
    valid = False
    while not valid:
        raw_input = input(prompt_text)
        if raw_input.isdigit():
            qty = int(raw_input)
            if qty > 0:
                valid = True
            else:
                print("Quantity must be greater than 0.")
        else:
            print("Invalid input. Please enter a positive whole number.")
    return qty


def go_home():
    global day, gold, energy, hunger, game_running

    print("\nYou went home, got a good night's sleep, and restored your energy to 30.")
    day = day + 1
    energy = 30

    if gold >= 10:
        gold = gold - 10
        hunger = 0
        print("You ate a hearty breakfast for 10 gold. Hunger reset to 0/3.")
    else:
        hunger = hunger + 1
        print(f"You don't have enough gold for breakfast! You are starving. Hunger: {hunger}/3.")
        if hunger == 3:
            print("\nGAME OVER: You starved for 3 consecutive days and passed out from hunger and thirst.")
            game_running = False


def buy_seeds(crop_type, quantity):
    global gold, tomato_seeds, corn_seeds, strawberry_seeds

    if crop_type == 1:
        cost = 3 * quantity
        if gold >= cost:
            gold = gold - cost
            tomato_seeds = tomato_seeds + quantity
            print(f"Bought {quantity} bags of Tomato seeds for {cost} gold.")
        else:
            print(f"Not enough gold! You need {cost} gold, but you only have {gold}.")
    elif crop_type == 2:
        cost = 5 * quantity
        if gold >= cost:
            gold = gold - cost
            corn_seeds = corn_seeds + quantity
            print(f"Bought {quantity} bags of Corn seeds for {cost} gold.")
        else:
            print(f"Not enough gold! You need {cost} gold, but you only have {gold}.")
    elif crop_type == 3:
        cost = 7 * quantity
        if gold >= cost:
            gold = gold - cost
            strawberry_seeds = strawberry_seeds + quantity
            print(f"Bought {quantity} bags of Strawberry seeds for {cost} gold.")
        else:
            print(f"Not enough gold! You need {cost} gold, but you only have {gold}.")


# TODO: sow_seeds(), water_crops(), harvest_crops(), sell_crops()


def farm_menu():
    # TODO: build the farm menu (sow, water, harvest)
    print("\nThe farm is still under construction. Coming soon!")


def shop_menu():
    in_shop = True
    while in_shop:
        print("\n=== GENERAL SHOP ===")
        print(f"Gold: {gold}")
        print(f"Seeds Bag  -> Tomato: {tomato_seeds} | Corn: {corn_seeds} | Strawberry: {strawberry_seeds}")
        print("\nWhat would you like to do at the shop?")
        print("[1] Buy Seeds")
        print("[2] Sell Crops (coming soon)")
        print("[0] Back to Main Menu")
        action = get_valid_choice(0, 2)

        if action == 1:
            print("\nWhich type of seed do you want to buy?")
            print("[1] Tomato (3g/bag)  [2] Corn (5g/bag)  [3] Strawberry (7g/bag)  [0] Cancel")
            crop = get_valid_choice(0, 3)
            if crop != 0:
                qty = get_positive_quantity("How many bags of seeds are you buying? ")
                buy_seeds(crop, qty)
        elif action == 2:
            # TODO: selling crops
            print("\nSelling crops isn't available yet. Coming soon!")
        elif action == 0:
            in_shop = False


print("Welcome to Harvest Sun!")
print("You arrive in town bright-eyed and ready for a fresh start, having already")
print("eaten a hearty breakfast to power you through your first morning.")

while game_running:
    display_status()
    print("What would you like to do?")
    print("[1] Go Home       - rest up and call it a day")
    print("[2] Go to the Farm - tend to your fields")
    print("[3] Go to the Shop - buy seeds and/or sell crops")
    print("[0] Quit")

    main_choice = get_valid_choice(0, 3)

    if main_choice == 1:
        go_home()
    elif main_choice == 2:
        farm_menu()
    elif main_choice == 3:
        shop_menu()
    elif main_choice == 0:
        print("\nThank you for playing Harvest Sun! Goodbye!")
        game_running = False