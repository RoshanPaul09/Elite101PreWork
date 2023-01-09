import random

def repsonseToUser(user_input):
  responses = [ "That's so cool!",  "How does that work?", "Coding is so fun!","That's Amazing!", "Thats not a nice thing to say."]
 
  return random.choice(responses)
  
def startAndLeaveChat():
  leavePhrase = 'Bye'

  userInput = input("Hey, how are you doing?\n")

  while userInput != leavePhrase:
    userInput = input(repsonseToUser(userInput) + "\n")

if __name__ == "__main__":
  startAndLeaveChat()