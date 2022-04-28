# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calculateBuyer(price, hasGoodCredit):
    if hasGoodCredit:
        price = price - (price * 10 / 100)
        print('since buyer has a good credit the price will have 10%')
        print(f'price is : {price}')


def carGame():
    while True:
        decision = input("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    carStopped = False
    while True:
        userInput = input(">").lower()
        if userInput == "help":
            print('''
            start - to start the car
            stop - to stop the car
            quit - to quit the game''')
        elif userInput == "start":
            if (carStopped):
                print("Car started . ready to go")
                carStopped = False
            else:
                print("car already started")
        elif userInput == "stop" :
            if (carStopped):
                print('car already stopped')
            else:
                print("Car stopped ")
                carStopped = True
        elif userInput == "quit":
            print("bye bye ..... ")
            break
        else:
            print("sorry ya prens I don't understand this")
