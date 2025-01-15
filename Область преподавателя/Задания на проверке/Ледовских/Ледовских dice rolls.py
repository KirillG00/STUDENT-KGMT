import random

def roll_dice_simulation(quantity_dice, target_sum):
    count = 0
    for _ in range(quantity_dice):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 + dice2 == target_sum:
            count += 1
    return count

throws = 1000
target_sum = 7
result = roll_dice_simulation(throws, target_sum)

print(f"Сумма {target_sum} появлялась {result} раз из {throws} бросков.")
