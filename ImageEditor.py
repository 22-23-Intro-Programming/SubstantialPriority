from graphics import*
from Button import*

def darken(img):

    x = img.getWidth()
    y = img.getHeight()
    
    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            newColor = color_rgb((r//2), (g//2), (b//2))
            img.setPixel(i, j, newColor)

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()
    
    for i in range(x):
        for j in range(y):
            pix  = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r=r*2
            g=g*2
            b=b*2
            if r>255:
                r=255
            if g>255:
                g=255
            if b>255:
                b=255
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)

def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix  = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            a = (r + g + b)//3
            newColor = color_rgb(a, a, a)
            img.setPixel(i, j, newColor)

def contrast(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix  = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            a = (r + g + b)//3
            if (a<=127):
                newColor = color_rgb((r//2), (g//2), (b//2))
                img.setPixel(i, j, newColor)
            if (a>127):
                r=r*2
                g=g*2
                b=b*2
                if r>255:
                    r=255
                if g>255:
                    g=255
                if b>255:
                    b=255
                newColor = color_rgb(r, g, b)
                img.setPixel(i, j, newColor)
        
def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("#FFAA00")

    I = Image(Point(300, 300), "veitchii.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Darken")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")
    B3 = Button(win, Point(600, 300), Point(700, 375), "tomato", "Grayscale")
    B4 = Button(win, Point(600, 400), Point(700, 475), "tomato", "Contrast")
    Q = Button(win, Point(600, 500), Point(700, 575), "misty rose", "QUIT")
    
    while True:
        m = win.getMouse()

        if B.isClicked(m):
            darken(I)

        if B2.isClicked(m):
            lighten(I)
        if B3.isClicked(m):
            grayscale(I)
        if B4.isClicked(m):
            contrast(I)
        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()

    
