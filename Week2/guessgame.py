secret_word = "sihle"
guess = ""
count = 0 # it is the guess count
limit = 3  # limit is the number limit for the gueses
out_of_guess = False

while guess != secret_word and not(out_of_guess):
  if count < limit:
    guess = input("Enter guess : ") 
    count = count + 1 # increment the count
  else:
    out_of_guess = True # it is true when the user hase used 3 guesses  

if out_of_guess:
  print("Out of guesses, you lose !")
else:
    print("You wone!")