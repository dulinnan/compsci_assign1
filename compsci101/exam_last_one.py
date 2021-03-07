from tkinter import *


def main():
    window = Tk()
    window.title("A5 by ...")
    canvas_width = 60
    canvas_height = 60
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand=True)  # Canvas fills the whole window
    draw_grid(a_canvas)
    draw_pattern(a_canvas, 10,10,10)
    window.mainloop()

def draw_pattern(a_canvas, left, top, size):
    number_of_shapes = 4
    is_circle = False
    for count in range(number_of_shapes):
        shape = (left, top, left + size, top + size)
        if is_circle:
            a_canvas.create_oval(shape)
        else:
            a_canvas.create_rectangle(shape)
        is_circle = not is_circle
        a_canvas.create_line(shape)
        left = left + size
        top = top + size

def draw_grid(canvas):
    for row in range(10, 100, 10):
        canvas.create_line(-1, row, 101, row, fill="lightblue")
    for column in range(10, 100, 10):
        canvas.create_line(column, -1, column, 101, fill="lightblue")
main()
