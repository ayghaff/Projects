print("Welcome to my quiz")

playing = input("Would you like to start the quiz? ")

if playing.lower() != "yes":
    print(":(")
    quit()

print("Alright! Lets start :)")
score = 0

answer = input("What does 'CPU' stand for? ").lower()
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does 'GPU' stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does 'RAM' stand for? ").lower()
if answer == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does 'ROM' stand for? ").lower()
if answer == "read only memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

if score == 4:
    print("You got", score, "out of 4, or", ((score / 4) * 100),"%! Well done!")
else:
    print("You got", score, "out of 4, or", ((score / 4) * 100), "%! Not bad!¯\_(ツ)_/¯")