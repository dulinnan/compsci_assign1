"""
Q4:Draws a pattern of red squares and green ovals.
Date-written: Semester 2, 2020.
Author:
"""

from tkinter import *


def main():
    window = Tk()
    window.title("Red and Green pattern")  # replace it with your UPI
    window.config(background='white')
    window.geometry("500x350+10+20")
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand=True)
    draw_grid(a_canvas)
    draw_pattern_in_canvas(a_canvas, 6)
    window.mainloop()


def draw_grid(canvas):
    for row in range(50, 350, 50):
        canvas.create_line(-1, row, 501, row, fill="lightblue")
    for column in range(50, 500, 50):
        canvas.create_line(column, -1, column, 351, fill="lightblue")


def draw_circle(x, y, r, canvas_name, colour):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, fill=colour)


def draw_square(x, y, square_length, canvas_name, colour):
    x0 = x + square_length
    y0 = y + square_length
    return canvas_name.create_rectangle(x, y, x0, y0, fill=colour)


def draw_square_row(x, y, square_length, step_length, row_number, canvas_name):
    index = 0
    while index < row_number:
        draw_square(x + index * step_length,
                    y + index * step_length, square_length, canvas_name, "red")
        index += 2


def draw_pattern_in_canvas(a_canvas, number_of_rows):
    grid_size = 50
    size = 50
    y_down = 0
    left_hand_side = 0
    is_circle = False
    # complete this function
    radius = grid_size/2-1*2
    square_length = (grid_size/2-1*2)*2
    origin_circle_x = grid_size/2
    origin_circle_y = grid_size/2
    origin_square_x = 2
    origin_square_y = 2
    step_length = grid_size
    draw_circle(origin_circle_x, origin_circle_y+step_length,
                radius, a_canvas, "green")
    # draw_square(origin_square_x+2*step_length, origin_square_y+3*step_length,
    #             square_length, a_canvas, "red")
    draw_square_row(origin_square_x, origin_square_y,
                    step_length, square_length, 3, a_canvas)


main()
