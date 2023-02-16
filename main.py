import random 
from wordlist import wordlist

# random word
answer = random.choice(wordlist) 
print("For testing:", answer) 


play_num = 0 
r = ""
while r != "n":     #looper
    play_num += 1
    if play_num >= 2: # Changes word on 2nd playthrough 
            answer = random.choice(wordlist) 
            print("For testing:", answer)


    for t in range(1,7): #wordle game
        print()
        user_guess = input("Enter Your Guess: ").lower()
        if user_guess not in wordlist: 
            while user_guess not in wordlist:   # loops till user gives a actual word
                if len(user_guess) != 5:
                    print("Word should be 5 letters")
                    user_guess = input("Re-Enter Your Guess: ").lower()
                else:
                    print("Invalid Input")
                    user_guess = input("Re-Enter Your Guess: ").lower()
                #loops infinitely and doesnt count towards guess
        
        print("You have used", str(t)+"/6", "tries" )
    
        for i in range(len(user_guess)):                  # Wordle Guessing 
            if user_guess[i] == answer[i]:
                print("🟩", end="")
            elif user_guess[i] in answer:
                print("🟨", end="")
            else:
                print("⬛", end="")
        print() #to make sure the next print is in the next line

        #end screen:
        if user_guess == answer:
            if t == 1:
                print("Congrats, You got the word in the first guess")
                break
            else:
                print("Congrats, You got the word in", t,"guesses")
                break
        elif t == 6:
            print("You've run out of tries...")
            print("The wordle was ", answer)  
    print()
    r = input("If you want to play again, press enter, Type N if you DONT want to play again... ").lower()

print("Thank You For Playing Wordle", play_num, "time(s)")