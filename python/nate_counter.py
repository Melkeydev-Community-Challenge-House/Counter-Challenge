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
