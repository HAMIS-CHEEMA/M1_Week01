# IF ELIF  ELSE   conditions

light = input("enter from red , green and yellow(R,G,Y) ").lower()

if light == "red" or light == "r":
    print("you must have to stop on signal.")
elif light == "yellow" or light == "y":
    print("start your engine.")
elif light == "green" or light =="g":
    print("you can go, now.")
else:
    print("invalid input , try again!")
# -----------------------------------------------

age = int(input("Enter your Age please "))
if age >= 18:
    id_card = input("Do you have ID Card (yes or No) ? ").lower()
    if id_card == "yes":
        movie_type = input("you want to watch 3d/regular movie")
        if movie_type == "3d":
            print("price for this is 500")
        elif movie_type == "regular":
            print("price is 200")
        else:
            print("invalid input ")
    elif id_card ==  "no":
        print("bring you card with you for watching movie")
    else:
        print("choose yes/no ")
elif age >=13:
    print("you can watch movie with your parents")
elif age >=5:
    print("you can watch cartoons for FREE")
else:
    input("invalid input")


