
secret_number = 42
guess = 0

while guess != secret_number:
    guess = eval(input("Guess the secret number? "))
    if guess < secret_number:
        print("The number is much too low try again ")
    elif guess > secret_number:
        print("The number is much too high try again ")
    elif guess == secret_number:
        print("Congratulations, you have guessed the secret number!")
