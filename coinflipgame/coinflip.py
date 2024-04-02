import random

while True:
    prob_head = float(input("What do you want the probability of the coin to land on heads? (0-1): "))
    if prob_head < 0 or prob_head > 1:
        print('no')
        quit()
    else:
        break

while True:
    flips = int(input("How many times do you want the coin to be flipped?: "))
    if flips < 0:
        print("You watch, as the world enters calamities, one after another, due to your tomfoolery.")
        quit()
    else:
        break

heads = 0
tails = 0

for i in range(flips):
    if random.random() < prob_head:
        heads += 1
    else:
        tails += 1

print("\nCoin being flipped...\n")
print(f"Heads: {heads}")
print(f"Tails: {tails}")
print(f"The coin landed on Heads about {heads/flips*100}% of the time, while it landed on Tails about {tails/flips*100}% of the time.")