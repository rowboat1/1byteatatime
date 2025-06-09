import challenge
import base64

# Write a python script that will break the password without you
# interfering.

# Using a new secret
challenge.secret = base64.b64decode("c3VzaGlzYW5kd2ljaA==")


def first_block_matches_last_block(text):
  _, blocks = challenge.register(text)
  return blocks[0] == blocks[-1]


if __name__ == "__main__":
  # The world is your oyster :) 

  
  pass
