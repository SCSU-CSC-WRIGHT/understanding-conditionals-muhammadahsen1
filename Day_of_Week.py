# Ask the user for a number between 1 and 7 

day_number = int(input("Enter a number between 1 and 7: ")) 

# Check the number and print the corresponding day of the week 

if day_number ==1: 

    print("Monday") 

elif day_number == 2: 

    print ("Tuesday") 

elif day_number == 3: 

    print ("Wednesday") 

elif day_number == 4: 

    print("Thursday") 

elif day_number == 5: 

    print ("Friday") 

elif day_number == 6: 

    print ("Saturday") 

elif day_number == 7: 

    print("Sunday") 
    
else: 

    print("Error: Please enter a number between 1 and 7.")
