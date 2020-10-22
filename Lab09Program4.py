"""
Q4:Draws a pattern of red squares and green ovals.
Date-written: Semester 2, 2020.
Author: Adam Du
"""

from tkinter import *


def main():
    window = Tk()
    window.title("Red and Green pattern - Austen")  # replace it with your UPI
    window.config(background='white')
    window.geometry("500x350+10+20")
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand=True)
    draw_grid(a_canvas)
    draw_pattern_in_canvas(a_canvas, 7)
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


def draw_square_row(x, y, square_length, step_length, row_number, canvas_name, colour):
    index = 0
    while index < row_number:
        draw_square(x,
                    y + index * step_length, square_length, canvas_name, colour)
        draw_square(x + index * step_length,
                    y + index * step_length, square_length, canvas_name, colour)
        if (abs(index-row_number) <= 2 and row_number % 2 != 0):
            column_index = 0
            while column_index < index:
                draw_square(x + column_index*step_length,
                            y + index * step_length, square_length, canvas_name, colour)
                column_index += 1
        index += 2


def draw_circle_row(x, y, radius, step_length, row_number, canvas_name, colour):
    row_index = 1
    while row_index < row_number:
        draw_circle(x, y + row_index*step_length, radius, canvas_name, colour)
        draw_circle(x + row_index*step_length, y + row_index *
                    step_length, radius, canvas_name, colour)
        if (abs(row_index-row_number) <= 2 and row_number % 2 == 0):
            column_index = 0
            while column_index < row_index:
                draw_circle(x + column_index*step_length,
                            y + row_index * step_length, radius, canvas_name, colour)
                column_index += 1
        row_index += 2


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
    draw_circle_row(origin_circle_x, origin_circle_y, radius,
                    step_length, number_of_rows, a_canvas, "green")
    draw_square_row(origin_square_x, origin_square_y,
                    square_length, step_length, number_of_rows, a_canvas, "red")


main()
