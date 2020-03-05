import rpsmodule as rps

#vars
print("Welcome to this game!!") 

rounds = 0
while rounds not in range(3,11):
    try:
        rounds = int(input("Pick between 3 and 10 rounds."))
    except:
        print("ERROR invalid input. Out of range or wrong type of data.")

rps.choose(rounds)

rps.end()