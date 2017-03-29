Secret = 1337
Try = 0
Count = 0

while Try != Secret:

    Try = int(input("Guess a number: "))

    if Try < Secret:
                  print("Too small !")

    if Try > Secret:
                  print("Too big !")

    Count = Count + 1

if Count == 1:
    
    print("Congratulations ! You did it within", Count, "try !")

else:

    print("Congratulations ! You did it within", Count , "tries !")




    

                   
