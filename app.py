import random
import joblib

model = joblib.load("model.pkl")

def start():
    print("nim game")
    print("the one who pick the last point wins")
    
    return

def loop(self):
    point = 8
    while point > 0:
        print("remaining point ",point)
        self = int(input("pick a number from 1 to 3 :"))
        if self > 3 or self < 0:
            print("a number between 1 and 3")
        else :
            point = point - self
            if point <= 0 :
                print("you win")
                break
            else:
                if point > 0:
                    self = model.predict([[point]])[0]
                    print("bot picked ",self)
                    point = point - self
                    if point <= 0:
                        print("bot wins")
    return

def game():
    
    start()
    loop(self=1)
    return game

game()