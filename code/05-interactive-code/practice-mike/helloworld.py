import random

print("---------------------------")
print("Favorite Number Guessing Game")
print("---------------------------")

random_fav_num = random.randint(1, 10)

odd_even_remainder = random_fav_num % 2
odd_even_flag = "placeholder"

if odd_even_remainder == 0:
    odd_even_flag = "even"
else:
    odd_even_flag = "odd"

attempt_limit = 5
attempts = 0

my_favorite_number = random_fav_num

while attempts < attempt_limit:

    remaining_attempts = attempt_limit - attempts

    if attempts == 0:
        fav_number_guess_str = input(f"What's my favorite number? You get {attempt_limit} guesses!")
        fav_number_guess = int(fav_number_guess_str)

    else:
        fav_number_guess_str = input(f"Try again? You get {remaining_attempts} more guesses! What's my fav number?")
        print(fav_number_guess_str)
        fav_number_guess = int(fav_number_guess_str)

    attempts += 1

    attempts_modulus = attempts % 2

    if fav_number_guess > my_favorite_number:
        directional_hint = "too high"
    elif fav_number_guess < my_favorite_number:
        directional_hint = "too low"

    if fav_number_guess == random_fav_num:
        print(f"Wow, you guessed my favorite number {fav_number_guess}! Good job!")
        break

    elif fav_number_guess != random_fav_num and attempts_modulus != 0:
        print(f"That's not my favorite number, here is a hint:  My favorite number is an {odd_even_flag} number, try again!")

    elif fav_number_guess != random_fav_num and attempts_modulus != 1:
        print(f"That's not my favorite number, here is a hint:  Your guess is {directional_hint}!")
print
