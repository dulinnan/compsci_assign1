"""
Aim: 
Author: aedg256
Q: Complete the draw_pattern(a_canvas, colours_dictionary, pattern_list, size, left, top) function
This function is passed SIX parameters: 
the Canvas object, a colours dictionary, a list of String elements, 
and followed by three integer parameters.  
The function draws a grid of coloured rectangles inside the canvas area.  
The left-top position of the grid of coloured rectangles is given by the last two parameter 
values and the size of each rectangle is given by the size parameter.  
Once you have completed this function you should see rows of coloured rectangles 
in the canvas area.
"""
from tkinter import *


def main():
    index = input("Enter an index for the pattern: ")

    size = 50
    start_left1 = size * 2
    start_down = size * 2
    names_list = ['steve', 'pig', 'zombie', 'skeleton', 'creeper1', 'creeper2']
    # names_list = ['creeper1']
    name_index = int(index)
    palette_filename, pattern_filename = get_filename(names_list, name_index)

    palette_content = process_file(palette_filename)
    colours_dictionary = create_colours_dictionary(palette_content)

    pattern_content = process_file(pattern_filename)
    pattern_list = create_pattern_list(pattern_content)

    number_of_rows = len(pattern_list)
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns + size * 4
    canvas_height = number_of_rows * size + size * 4
    window = Tk()
    window.title("A5 by ...")
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand=True)  # Canvas fills the whole window
    draw_pattern(a_canvas, colours_dictionary, pattern_list,
                 size, start_left1, start_down)
    window.mainloop()


def get_filename(names_list, index):
    list_of_lists = []
    for name in names_list:
        name1 = name + "_palette.txt"
        name2 = name + ".txt"
        name_list = [name1, name2]
        list_of_lists.append(name_list)
    list_of_tuples = [tuple(l) for l in list_of_lists]

    indexed_list = list_of_tuples[index]

    return indexed_list


def split_codes(line):
    return list(line)


def process_file(filename):
    input_stream = open(filename, 'r')
    contents = input_stream.read().strip()
    input_stream.close()
    line_list = contents.split("\n")
    return line_list


def create_colours_dictionary(colours_list):
    colour_dictionary = {}
    for colour in colours_list:
        the_key = colour[0:1]
        the_value = colour[2:]
        colour_dictionary[the_key] = the_value

    return colour_dictionary


def create_pattern_list(lines):
    lines_list = []
    for string in lines:
        string_list = list(string)
        lines_list.append(string_list)
    return lines_list


def draw_square(x, y, square_length, canvas_name, colour):
    x0 = x + square_length
    y0 = y + square_length
    return canvas_name.create_rectangle(x, y, x0, y0, fill=colour)


def calculate_column_amount(pattern_list):
    column_amount = len(pattern_list)
    return column_amount


def extract_colour_list(pattern_list, colours_dictionary):
    colour_list = []

    for each_colour_abbr in pattern_list:
        lookup_colour = colours_dictionary.get(each_colour_abbr)
        colour_list.append(lookup_colour)
    return colour_list


def draw_row(x0, y0, row_number, square_length, pattern_list, colours_dictionary, canvas_name):
    colour_list = extract_colour_list(pattern_list, colours_dictionary)
    column_amount = calculate_column_amount(colour_list)
    index = 0
    while index < column_amount:
        draw_square(x0+index*square_length, y0+row_number*square_length, square_length,
                    canvas_name, colour_list[index])
        index += 1


def draw_pattern(a_canvas, colours_dictionary, pattern_list, size, left, top):
    index = 0
    # down = top
    while index < len(pattern_list):
        each_list = pattern_list[index]
        draw_row(left, top, index, size, each_list,
                 colours_dictionary, a_canvas)
        index += 1


main()
