from tkinter import *


class BresenhamCanvas(Canvas):
    def draw_point(self, x, y, color="red"):
        self.create_line(x, y, x+1, y+1, fill=color, width=2)

    def draw_line(self, x0, y0, x1, y1, color="red"):
        dx = abs(x1-x0)
        dy = abs(y1-y0)
        p = 2 * dy - dx
        incE = 2*dy
        incNE = 2*(dy-dx)
        if x0 > x1:
            x = x1
            y = y1
            xend = x0
        else:
            x = x0
            y = y0
            xend = x1
        for i in range(x, xend):
            print('x =', x, 'y =', y)
            x = x+1 if x < x1 else x - 1
            if p < 0:
                p += incE
                self.draw_point(x, y, color=color)
            else:
                y = y+1 if y < y1 else y - 1
                p += incNE
                self.draw_point(x, y, color=color)


class CircleBresenham(Canvas):
    def draw_point_circle(self, xc, yc, x, y):
        self.create_rectangle((xc+x, yc+y)*2, outline="blue")
        self.create_rectangle((xc-x, yc+y)*2, outline="blue")
        self.create_rectangle((xc+x, yc-y)*2, outline="blue")
        self.create_rectangle((xc-x, yc-y)*2, outline="blue")
        self.create_rectangle((xc+y, yc+x)*2, outline="blue")
        self.create_rectangle((xc-y, yc+x)*2, outline="blue")
        self.create_rectangle((xc+y, yc-x)*2, outline="blue")
        self.create_rectangle((xc-y, yc-x)*2, outline="blue")

    def circlebress(self, xc, yc, r):
        x = 0
        y = r
        d = 3 - 2 * r
        self.draw_point_circle(xc, yc, x, y)
        while y >= x:
            x = x + 1
            if d > 0:
                y = y - 1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6
            self.draw_point_circle(xc, yc, x, y)


if __name__ == "__main__":
    CANVAS_SIZE = 600
    root = Tk()
    canvas = CircleBresenham(root, width=CANVAS_SIZE, height=CANVAS_SIZE)
    canvas.pack()
    # canvas.draw_line(100, 100, 200, 100, color="blue")
    # canvas.draw_line(200, 100, 300, 350, color="blue")
    canvas.circlebress(400, 300, 100)
    root.mainloop()
