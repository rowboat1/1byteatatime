import challenge

# This script will read out any guesses you put in guesses.txt
# If you run this script now (try it!), you will get no results.

# But if you add an underscore to each line of guesses.txt, you will decrypt
# one byte of the secret.


GREEN = "\033[32m"
RESET = "\033[0m"

if __name__ == "__main__":
  with open("guesses.txt") as guesses:
    for guess in guesses:
      print("\n\n======================================")
      print(f"Using guess: {guess}")
      _, blocks = challenge.register(guess.strip())
      print("AES OUTPUT:")
      for block in blocks:
          if (blocks.count(block) > 1):
              print(f"{GREEN}{block}{RESET}👈👈✅✅✅")
          else:
              print(block)
