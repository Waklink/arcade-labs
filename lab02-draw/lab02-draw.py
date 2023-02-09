import arcade

arcade.open_window(600, 600, 'Drawing Example')

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

# El oceano
arcade.draw_lrtb_rectangle_filled(0, 600, 500, 0, arcade.color.BLUE)
# El cielo
arcade.draw_lrtb_rectangle_filled(0, 600, 600, 500, arcade.color.SKY_BLUE)
# La línea de horizonte
arcade.draw_line(0, 500, 600, 500, arcade.color.BLACK, 0.1)
# La isla de fondo
arcade.draw_line(290, 500.1, 330, 500.1, arcade.color.BROWN_NOSE, 2.4)
# El cuerpo del barco
arcade.draw_polygon_filled(((40, 100), (110, 30), (310, 30), (380, 100)), arcade.color.DARK_BROWN)
# La bandera del barco
arcade.draw_line(210, 100, 210, 300, arcade.color.DARK_BROWN, 3)
arcade.draw_triangle_filled(212.5, 150, 212.5, 300, 253, 170, arcade.color.WHITE)
# Los pájaros del cielo

def pajaro(left, right, bottom, color = arcade.color.WHITE):
    radio = (right-left)
    arcade.draw_arc_outline(left, bottom, radio, radio, color, 0, 90, 1, 0, 100)
    arcade.draw_arc_outline(right, bottom, radio, radio, color, 90, 180, 1, 0, 100)

pajaro(50, 60, 530)
pajaro(65, 76, 535)
pajaro(55, 79, 550)
pajaro(70, 100, 515)
pajaro(40, 68, 505)

arcade.finish_render()

arcade.run()
