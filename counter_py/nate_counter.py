
	# TODO: Simple counting program.

        ## ***** Feel free to get creative with this. ******

	# 	 1.
	# 	  ask the user if they want to start counting (only once)
	# 	  do something if they fail yes/no
		
	# 	 2.
	# 	  ask what they want to count to (a whole number)
	# 	  do something if they fail this
		
	# 	 3.
	# 	  counting output must be controlled by user input
	# 	  example +1 every time they hit the enter key

	# 	 4. 
	#     ask if they want to count to (X) more than once
        #       This is optional
    

import sys

def main() -> None:    
    count, age = 0, 0
    
    print("Would you like to start?")
    tmpin = input("[y/n]? ")
    while tmpin != "y":
        tmpin = input("Try Again [y/n]?")
        if tmpin == "y":
            break
        if tmpin == "n":
            sys.exit(1)

    times_around = input("how many times around? ")
    while times_around == "":
        times_around = input("Try again: ")
        if times_around != "":
            break

    while count < int(times_around) + 1: 
        check = input(" ") 
        if count == int(times_around):
            count = 0
            age += 1
            print(f"{age} Time around!")
        
        if check == "":
            print(count)
            count += 1
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()