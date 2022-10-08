from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab


class BresenhamCanvas(Canvas):

    def draw_point(self, x, y, color="red"):
        self.create_line(x, y, x+1, y+1, fill=color, width=2)

    # def draw_line(self, x0, y0, x1, y1, color="red"):
    #     dx = abs(x1-x0)
    #     dy = abs(y1-y0)
    #     p = 2*dy-dx if dx > dy else 2*dx-dy
    #     incE = 2*dy if dx > dy else 2*dx
    #     incNE = 2*(dy-dx) if dx > dy else 2*(dx-dy)
    #     if (x0 > x1) or (y0 > y1):
    #         x, y = x1, y1
    #         xend, yend = x0, y0
    #     else:
    #         x, y = x0, y0
    #         xend, yend = x1, y1
    #     if dx > dy:
    #         start = x
    #         end = xend
    #     else:
    #         start = y
    #         end = yend

    #     self.draw_point(x, y, color=color)
    #     for i in range(start, end):
    #         if dx > dy:
    #             x = x+1 if x < x1 else x-1
    #         else:
    #             y = y+1 if y < y1 else y-1
    #         if p < 0:
    #             p += incE
    #         else:
    #             if dx > dy:
    #                 y = y+1 if y < y1 else y-1
    #             else:
    #                 x = x+1 if x < x1 else x-1
    #             p += incNE

    #         self.draw_point(x, y, color=color)
    def draw_line(self, x0, y0, x1, y1, color="red"):
        dx = (x1-x0)
        dy = (y1-y0)
        if dy < 0:
            dy = -dy
            stepy = -1
        else:
            stepy = 1
        if dx < 0:
            dx = -dx
            stepx = -1
        else:
            stepx = 1
        x = x0
        y = y0
        self.draw_point(x, y, color=color)
        if (dx > dy):
            p = 2 * dy-dx
            incE = 2 * dy
            incNE = 2 * (dy-dx)
            while (x != x1):
                x = x + stepx
                if p < 0:
                    p = p + incE
                else:
                    y = y + stepy
                    p = p + incNE
                self.draw_point(x, y, color=color)
        else:
            p = 2 * dx - dy
            incE = 2 * dx
            incNE = 2 * (dx-dy)
            while y != y1:
                y = y + stepy
                if p < 0:
                    p = p + incE
                else:
                    x = x + stepx
                    p = p + incNE
                self.draw_point(x, y, color=color)

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


def draw_circle():
    canvas.delete('all')
    setpoint_circle()
    canvas.bind("<Button-1>", press_button_mouse)
    canvas.pack(side=LEFT)
    canvas.circlebress(x0, y0, 50)


def drawsquare():
    canvas.delete('all')
    setpoints_square()
    canvas.draw_line(x0, y0, x1, y1, color="blue")
    canvas.draw_line(x0, y0, y1, x1, color="blue")
    canvas.draw_line(x1, y0, x1, x1, color="blue")
    canvas.draw_line(x0, x1, x1, x1, color="blue")


def draw_triangle():
    canvas.delete('all')
    setpoints_triangle()
    canvas.draw_line(x0, y0, x1, y1, color="blue")
    canvas.draw_line(x1, y1, x2, y2, color="blue")
    canvas.draw_line(x2, y2, x0, y0, color="blue")


def press_button_mouse(event):
    puntosx.append(event.x)
    puntosy.append(event.y)
    canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="red")


def setpoint_circle():
    global x0, y0
    x0 = puntosx[0]
    y0 = puntosy[0]


def setpoints_square():
    global x0, y0, x1, y1
    x0 = puntosx[0]
    y0 = puntosy[0]
    x1 = puntosx[1]
    y1 = puntosy[1]


def setpoints_triangle():
    global x0, y0, x1, y1, x2, y2
    x0 = puntosx[0]
    y0 = puntosy[0]
    x1 = puntosx[1]
    y1 = puntosy[1]
    x2 = puntosx[2]
    y2 = puntosy[2]


def savefile():
    file = filedialog.asksaveasfilename(initialdir="C:/",
                                        filetypes=(('PNG File', '.PNG'), ('PNG File', '.PNG'), ('JPEG File', '.JPEG'), ('JPEG File', '.JPEG')))
    file = file + ".PNG"
    # ImageGrab.grab().crop((x0-250, y0-250, 600, 600)).save(file)
    ImageGrab.grab().crop((500-x0, 700-y0, 500, 700)).save(file)


# def mouse_move(event):
#     window.title(str(event.x)+'-'+str(event.y))


def clear_canvas():
    canvas.delete('all')
    puntosx.clear()
    puntosy.clear()


def create_menu():
    menu_bar = Menu(window)
    window.config(menu=menu_bar)
    options1 = Menu(menu_bar, tearoff=0)
    options1.add_command(label="Clear", command=clear_canvas)
    options1.add_command(label="Save", command=savefile)
    menu_bar.add_cascade(label="Options", menu=options1)


def create_buttons():
    buton_square = Button(window, text="Square", font=(
        "Comic Sans", 15), width=10, command=drawsquare)
    buton_square.place(x=540, y=150)

    buton_triangle = Button(window, text="Triangle",
                            font=("Comic Sans", 15), width=10, command=draw_triangle)
    buton_triangle.place(x=540, y=200)

    buton_circle = Button(window, text="Circle",
                          font=("Comic Sans", 15), width=10, command=draw_circle)
    buton_circle.place(x=540, y=250)

    # button_save = Button(window, text="Save",
    #                      font=("Comic Sans", 15), width=10, command=savefile)
    # button_save.place(x=540, y=300)
    button_close = Button(window, text="Close",
                          font=("Comic Sans", 15), width=10, command=window.destroy)
    button_close.place(x=540, y=600)


def create_canvas():
    global canvas
    canvas = BresenhamCanvas(frame, width=500, height=700)
    # canvas.bind("<Motion>", mouse_move)
    canvas.bind("<Button-1>", press_button_mouse)
    canvas.pack(side=LEFT)


def main():
    global window, frame, puntosx, puntosy
    puntosx = []
    puntosy = []
    window = Tk()
    window.geometry("700x700")
    window.title("GUI grafi")
    window.resizable(0, 0)
    window.config(background="#1c1c1c")
    create_menu()
    label = Label(window, text="  Choose your \n figure to draw", fg="white", bg="#1c1c1c", font=("Verdana", 15)).place(
        x=515, y=60)
    create_buttons()
    frame = Frame(window, width=500, height=600, bg="white")
    frame.pack(side=LEFT)
    create_canvas()
    window.mainloop()


if __name__ == '__main__':
    main()
