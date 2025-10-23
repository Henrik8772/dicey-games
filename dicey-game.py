import time
from random import randint


def game():
    dice_limit = 500
    multis = 1
    points = 0

    print("Welcome to DICE GAMES!!!")
    start = input("Start the game? y/n: ")
    if start != "y":
        print("Goodbye!")
        return

    while True:
        roll_dice = input("Do you want to roll? y/n: ")
        if roll_dice != "y":
            print("Thanks for playing!")
            break

        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        suma = (dice1 + dice2) * multis
        points += suma

        print("You rolled a", dice1)
        time.sleep(0.5)
        print("and")
        time.sleep(0.5)
        print("you also rolled a", dice2)
        time.sleep(1)
        print(
            f"That means you got ({dice1} + {dice2}) * {multis} = {suma} points")
        print(f"Total points: {points}")
        time.sleep(1)

        dice_limit -= 1

        print(f"You now have {dice_limit} rolls left!")

        shop = input("Do you want to use your points in the shop? y/n: ")
        if shop == "y":
            while True:
                print("These are some of the multis in stock.")
                time.sleep(1)
                print("1. The goblet of the gods: multi = +1.0x, cost = 12 points")
                time.sleep(0.5)
                print("2. Sword of the Hero: multi = +2.0x, cost = 35 points")
                time.sleep(1)
                print("3. We also sell dice rolls! 10 points per roll!")
                time.sleep(0.5)

                buy = input(
                    "Do you want to buy any of them? If so, write the name of the item or the number before the name: ")
                if buy == "The goblet of the gods" or buy == "1" and points >= 12:
                    multis += 1.0
                    points -= 12
                    print(
                        f"You have bought The goblet of the gods, your multi is now {multis}")
                elif buy == "Sword of the Hero" or buy == "2" and points >= 35:
                    multis += 2.0
                    points -= 35
                    print(
                        f"You have bought the Sword of the Hero, your multi is now {multis}")
                elif buy == "Dice" or buy == "3" and points >= 10:
                    amount = int(input("How many do u want to buy?: "))
                    if amount > 0:
                        dice_limit += 1 * amount
                        if amount >= 1 and points == 10*amount:
                            points -= 10 * amount
                            print(
                                f"You have bought {amount} dice you now have {dice_limit} dice!")
                        elif amount < 1:
                            print("You didnt put in an amount you silly :3")
                        elif points != 10*amount:
                            print(f"You dont have enough you silly :3")

                elif buy in ["The goblet of the gods", "1", "Sword of the Hero", "2", "Dice", "3"]:
                    print("Not enough points!")
                else:
                    print("No such item.")

                buy_again = input("Do you wanna buy anything else? y/n: ")
                if buy_again.lower() not in ("y", "yes", "Yes"):
                    break
            continue

        if dice_limit == 0:
            print("Game Over!")
            print("You ran out of rolls!")
            break


game()
