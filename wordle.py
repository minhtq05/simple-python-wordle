import random
      
five_letter_words = [
    "apple", "apron", "baker", "beard", "beast", "black", "blink", "brick", "brush", "cabin",
    "cable", "charm", "chase", "check", "climb", "clock", "cloud", "crane", "crisp", "crowd",
    "daisy", "dance", "drown", "eagle", "earth", "elbow", "empty", "enemy", "fable", "fancy",
    "flame", "flock", "flute", "forge", "frown", "fudge", "giant", "glare", "globe", "grape",
    "green", "grind", "happy", "hatch", "heart", "honey", "house", "hurry", "igloo", "insect",
    "jolly", "judge", "juice", "kneel", "knife", "latch", "liver", "lunar", "mango", "match",
    "music", "noble", "oasis", "ocean", "opera", "piano", "pilot", "quilt", "quiet", "quick",
    "rider", "robin", "scent", "sheep", "shirt", "sight", "smile", "snake", "spark", "stack",
    "stove", "sweep", "swift", "table", "toxic", "trick", "truck", "ulcer", "under", "vault",
    "wager", "waste", "whale", "wrist", "xerox", "yacht", "zebra", "zesty", "zincs", "zoned"
]

hidden_word = random.choice(five_letter_words)
win = False

print("""
WORDLE
Guess a five letter word!  
Rules:
    * A player has to guess a 5 letter word.
    * You have six attempts.
""")

trials = 6 # you only have six trials

def check(guess, hidden_word):
    result = ""
    if (len(guess) != 5):
        return False
    if (guess == hidden_word):
        return True
    else:
        for [i,j] in zip(guess, hidden_word):
            if (i == j):
                result += 'v'
            elif (i in hidden_word):
                result += 'x'
            else:
                result += '_'
    
    return result

def get_a_guess():
    guess = input("What's your word? ")
    guess = guess.strip()
    return guess

while (win == False and trials > 0):
    guess = get_a_guess()
    result = check(guess, hidden_word)
    if (result == False):
        print('The length of your word is not five, try again!')
        continue
    elif (result == True):
        win = True
        print("Congrats!! You did it.")
        break
    else:
        print(result)
    trials = trials - 1

if (win == False):
    print('You lose!')
