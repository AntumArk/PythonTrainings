print("Hello world")

grid_width_scale : int = 5
grid_height : int = 3
blank_character : str = " "
x_character : str = "❌" # 2 whitespaces long
x_whitespaces : int = 2 # 2 whitespaces long
x=1
o=-1
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

def draw_vertical_line(scale,cells):
    # This is where empty lines should be drawn
    for index in range(2):
        print_filled_cell(scale,cells[index])
        if index!=2:
            print_no_endl(vertical_line_character)
    print()

def print_blank_cell(scale):
    for a in range(whitespaces_per_cell*scale):
        print_no_endl(blank_character)

def print_filled_cell(scale, value):
    if value == 0:
        print_blank_cell(scale)
        return
    if value == x:
        print_no_endl(x_character)
    if value == o:
        print_no_endl(o_character)  
    for a in range(whitespaces_per_cell*scale-x_whitespaces):
        print_no_endl(blank_character)

def print_no_endl(text):
    print(text,end="")

def draw_horizontal_line(scale):
    # This is where empty lines should be drawn
    for index in range(3):
        for a in range(whitespaces_per_cell*scale):
            print_no_endl(horizontal_line_character)
        if index!=2:
            print_no_endl(horizontal_separator_character)
    print()



def draw_grid(scale_x, scale_y, cells):
    print()
    for row in range(3):
       draw_vertical_line(scale_y, cells[0+row:2+row])
       if row!=2:
          draw_horizontal_line(scale_x)
    print()
        

# draw_vertical_line(1)
# draw_horizontal_line(1)
# draw_vertical_line(2)
# draw_horizontal_line(2)
# draw_vertical_line(3)
# draw_horizontal_line(3)


game_cells=[x,0,o,
            x,o,x,
            0,0,0]

draw_grid(2,2,game_cells)
# print(x_character)
# print(o_character)