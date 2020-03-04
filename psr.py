import getpass 

#vars
print("Welcome to this game!!") 
user1 = input("What's your name? ") 
user2 = input("And your name? ") 
score1 = 0
score2 = 0
#funcs
def win(user):
    text = "%s wins this round!\r\n%s score: %d\r\n%s score: %d" %(user, user1, score1, user2, score2)
    return text

def compare(u1, u2):
    global score1
    global score2
    if u1 == u2:
        return("It's a tie!") 

    elif u1 == 'rock': 
        if u2 == 'scissors':
            score1 += 1
            return win(user1)
        else: 
            score2 += 1
            return win(user2)

    elif u1 == 'scissors': 
        if u2 == 'paper':
            score1 += 1
            return win(user1)
        else: 
            score2 += 1
            return win(user2)

    elif u1 == 'paper': 
        if u2 == 'rock': 
            score1 += 1
            return win(user1)
        else: 
            score2 += 1
            return win(user2)

    else: 
        return("Invalid input! You have not entered rock, paper or scissors, try again.") 
       

rounds = int(input("How many rounds would you like to play? "))
while rounds not in range(3,11):
    try:
        rounds = int(input("Sorry! I can only play between 3 and 10 rounds. Try again: "))
    except:
        print ("ERROR invalid input. Out of range or wrong type of data.")
   

for i in range(rounds):
    user1_answer = getpass.getpass("%s, do yo want to choose rock, paper or scissors?" % user1) 
    user2_answer = getpass.getpass("%s, do you want to choose rock, paper or scissors?" % user2) 
    print(compare(user1_answer, user2_answer))

if score1 == score2:
    print ("you both suck")
elif score1 < score2:
    print ("%s won the game" %(user2))
elif score2 < score1:
    print ("%s won the game" %(user1))