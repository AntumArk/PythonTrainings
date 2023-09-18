print("Hello world")

grid_width : int = 5
grid_height : int = 3
blank_character : str = "  "
x_character : str = "❌"
o_character : str = "⭕"
horizontal_line_character : str = "───┼───┼───"
vertical_line_character : str = "   │   │    "







def draw_grid(grid_width, grid_height):
    print()
    for row in range( 0, grid_height):
        # for column in range( 0, grid_width):

        #     #print(column)
        #     # if column!= 1 and column!=3 :
        #     #     print(blank_character,sep="",end="")
        #     # else:
        #     #     print(vertical_line_character,sep="",end="")
        #     print()
        print(vertical_line_character)
        if row<grid_height-1:
            print(horizontal_line_character,end="")
        print()
    print()
        


draw_grid(grid_width,grid_height)
print(x_character)
print(o_character)