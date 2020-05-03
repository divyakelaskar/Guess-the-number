import random 

while True:

    print("\nN U M B E R   G U E S S I N G   G A M E") 
    print("\nYou have 10 chances to guess the number.")
    
    # randint function to generate the random number between 1 to 100 
    number = random.randint(1, 100) 
    
    """ number of chances to be given to the user to guess the number or it is the inputs
    given by user into input box here number of chances are 10 """
    chances = 0
    
    print("Guess a number (1 - 100):")  
    
    # While loop to count the number of chances 
    while chances < 10: 
        
        # Enter a number between 1 to 100  
        guess = int(input()) 
        
        # Compare the user entered number  with the number to be guessed  
        if guess == number: 
            
            """ if number entered by user is same as the generated number by randint
            function then  break from loop using loop control statement "break" """
            print("Congratulation YOU WON!!!") 
            break
            
        # Check if the user entered number is smaller than the generated number  
        elif guess < number: 
            print("Your guess was too low: Guess a number higher than", guess) 
    
        # The user entered number is greater than the generated number              
        else: 
            print("Your guess was too high: Guess a number lower than", guess) 
            
        # Increase the value of chance by 1 
        chances += 1
            
    # Check whether the user guessed the correct number  
    if not chances < 10: 
        print("YOU LOSE!!! The number is", number) 
    
    ans=input("Do you want to play again (y/n) : ")
    
    if ans != 'y' : 
        break

print("\n      T H A N K S     F O R     P L A Y I N G     ! ! ! ! !\n")  