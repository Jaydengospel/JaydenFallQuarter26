numgrade = int(input("What number grade did you get?"))

if (numgrade >= 90):
    print("you got an A")
elif(80 <= numgrade <= 89):
    print("you got a B")
elif(70 <= numgrade <= 79):
    print("you got a C")
elif(60 <= numgrade <= 69):
    print("you got a D")
elif(numgrade < 60):
    print("you got a F")