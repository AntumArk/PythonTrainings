print("Hello world")

grid_width_scale : int = 5
grid_height : int = 3
blank_character : str = " "
x_character : str = "❌" # 2 whitespaces long
o_character : str = "⭕" # 2 whitespaces long
horizontal_line : str = "───┼───┼───"
horizontal_line_character : str = "─"
horizontal_separator_character : str = "┼"
vertical_line: str = "⭕ │❌ │⭕  "
vertical_line_character : str = "│"
whitespaces_per_cell: int = 3




def draw_vertical_data_line():
    # This is where x o drawing logic should be
    print(vertical_line_character)

def draw_vertical_line(scale):
    # This is where empty lines should be drawn
    for index in range(2):
        for a in range(whitespaces_per_cell*scale):
            print(blank_character,end="")
        if index!=2:
            print(vertical_line_character,end="")
    print()

def draw_horizontal_line(scale):
    # This is where empty lines should be drawn
    for index in range(3):
        for a in range(whitespaces_per_cell*scale):
            print(horizontal_line_character,end="")
        if index!=2:
            print(horizontal_separator_character,end="")
    print()



def draw_grid(scale_x, scale_y):
    print()
    for row in range(3):
       draw_vertical_line(scale_y)
       if row!=2:
          draw_horizontal_line(scale_x)
    print()
        

draw_vertical_line(1)
draw_horizontal_line(1)
draw_vertical_line(2)
draw_horizontal_line(2)
draw_vertical_line(3)
draw_horizontal_line(3)

draw_grid(3,3)
# print(x_character)
# print(o_character)