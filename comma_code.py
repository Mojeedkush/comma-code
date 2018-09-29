print ("This program takes in any food item you input and displays it in an organised manner")
print ("Hello there! Can you please enter your name?")
user = input ()
print ("Welcome!",user)

while True:
    def food (items): # a function is defined with "item" as the single parameter
        no_of_items = 0 # a counter for the number of items in the list is declared
        items_string = "" # a string for the list is also formed

        while no_of_items < len (items) - 1: # condition for compiling all the items except the last one
            items_string += items [no_of_items] + ", " # each item and ", " is added to the string via concatenation
            no_of_items += 1 # counter is increased accordingly
        return items_string + "and " + items [no_of_items] # the last item and "and" is brought in
        
            
    meal = [] # program creates an empty list

    print ("Enter any food of your choice and press enter when done")

    usermeal = input () # asks user to enter a food item

    while usermeal != "": # the program continues to run until nothing is entered and user press enter 
        meal = meal + [usermeal] #each item entered by the user is added to the list
        usermeal = input () # asks for more entry
        
    print (food (meal))

    close = input ("\nWould you like to exit?\n 1.Yes\t 2. No\n Choice:")
    if close == "2": # conditions for quitting the program
        continue
    
    elif close == "1":
        print ("Thank you for your time,",user,", do have a nice day!")
        break

































