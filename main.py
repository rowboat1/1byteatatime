import challenge

# This script will read out any guesses you put in guesses.txt
# If you run this script now (try it!), you will get no results.

# But if you add an underscore to each line of guesses.txt, you will decrypt
# one byte of the secret.

if __name__ == "__main__":
  with open("guesses.txt") as guesses:
    for guess in guesses:
      print("======================================")
      print(f"Using guess: {guess}")
      challenge.register(guess.strip())
