
playing = input("Do you want to play? ")
print("")

if playing != "yes":
    quit()

print("okay! lets play :)")
print()

actual_number = 55
attempts = 0

while True:
    attempts += 1
    guess = int(input("guess any number between 1 and 100:\n"))
    if guess<actual_number:
        print()
        print("Yours Guess was too Low")

    elif guess>actual_number:
        print()
        print("Your Guess is too High")


    else:
        print()
        print(f"(＾▽＾) Amazing you guessed the correct number in [{attempts}] attempts")
        break
print("Thanks for playing.......   :) ")

