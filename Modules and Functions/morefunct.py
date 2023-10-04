import math
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter


def parablola(page,n):
    for x in range(-n, n):
        y = x*x/100
        plot(page, x, -y)


def draw_circle(page, radius, g,h):
    for x in range(g*100,(g+h)*100):
        x/=100
        y=h+math.sqrt(radius**2-((x-g)**2))
        plot(page,x,y)
        #symmertric plots
        plot(page,x,2*h-y)
        plot(page,2*g-x,y)
        plot(page,2*g-x,2*h-y)


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(page, x, y):
    page.create_line(x, y, x + 1, y + 1, fill="red")

mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480)
# canvas2.grid(row=0, column=1)

draw_axes(canvas)
# draw_axes(canvas2)
parablola(canvas,100)
draw_circle(canvas,100,100,100)
mainWindow.mainloop()
