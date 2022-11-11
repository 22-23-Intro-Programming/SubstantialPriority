from graphics import*
from Button import*

def main():

    win = GraphWin("Character Creator", 800, 800)
    Face = Oval(Point(100, 100), Point(500, 700))
    Face.draw(win)

    eyes1 = Button(win, Point(525, 100), Point(625, 175), "cyan", "Big Eyes")
    eyes2 = Button(win, Point(650, 100), Point(750, 175), "green", "Small Eyes")

    QButton = Button(win, Point(600, 625), Point(750, 725), "red", "Quit")

    Eye1 = Circle(Point(200, 250), 50)
    Eye2 = Circle(Point(400, 250), 50)

    eye1 = Circle(Point(200, 250), 20)
    eye2 = Circle(Point(400, 250), 20)

    eyes = [Eye1, Eye2, eye1, eye2]            
                    
    M1 = Button(win, Point(525, 300), Point(625, 375), "blue", "Happy Smile")
    M2 = Button(win, Point(650, 300), Point(750, 375), "yellow", "Sad Frown")

    Mouth2 = Polygon([Point(300, 550), Point(180, 600), Point(420, 600)])
    Mouth1 = Polygon([Point(180, 600), Point(420,600), Point(300,650)])

    Ear1 = Circle(Point(100, 270), 20)
    Ear2 = Circle(Point(500, 270), 20)

    ear1 = Circle(Point(80,270), 50)
    ear2 = Circle(Point(510, 270), 50)

    EarBut1 = Button(win, Point(525, 500), Point(625, 575), "orange", "Small Ears")
    EarBut2 = Button(win, Point(650, 500), Point(750, 575), "pink", "Big Ears")
    ears = [Ear1, Ear2, ear1, ear2]

    

    mouths = [Mouth1, Mouth2]   
    while True:
        m = win.getMouse()
        if eyes1.isClicked(m):
            for e in eyes:
                e.undraw()

            Eye1.draw(win)
            Eye2.draw(win)
            print("Big Eyes")

        if eyes2.isClicked(m):
            for e in eyes:
                e.undraw()
            eye1.draw(win)
            eye2.draw(win)
            print("small eyes")

        if QButton.isClicked(m):
            break

        if M1.isClicked(m):
            for e in mouths:
                e.undraw()

            Mouth1.draw(win)
            print("Happy!")

        if M2.isClicked(m):
            for e in mouths:
                e.undraw()

            Mouth2.draw(win)
            print("Depressed!")

        if QButton.isClicked(m):
            break

        if EarBut1.isClicked(m):
            for e in ears:
                e.undraw()

            Ear1.draw(win)
            Ear2.draw(win)

        if EarBut2.isClicked(m):
            for e in ears:
                e.undraw()

            ear1.draw(win)
            ear2.draw(win)
            
                

    win.close()


    

   
       
       
if __name__=="__main__":
        main()
