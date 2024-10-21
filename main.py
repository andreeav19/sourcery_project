import random


def monte_carlo_dice(num_throws):
    num_successful_throws = 0

    for _ in range(num_throws):
        dices_sum = random.randint(1, 12) + random.randint(1, 12)

        if dices_sum >= 17:
            num_successful_throws += 1

    estimated_prob = num_successful_throws / num_throws
    return estimated_prob


throws = 1000
estimated_probability = monte_carlo_dice(throws)

print(f"The estimated probability of obtaining the sum of 17 after throwing 2 dice with 12 faces "
      f"{throws} times is {estimated_probability}")
