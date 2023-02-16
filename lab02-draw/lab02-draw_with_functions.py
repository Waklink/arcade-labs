import arcade


def pajaro(left, right, bottom, color=arcade.color.WHITE):
    radio = (right-left)
    arcade.draw_arc_outline(left, bottom, radio, radio, color, 0, 90, 1, 0, 100)
    arcade.draw_arc_outline(right, bottom, radio, radio, color, 90, 180, 1, 0, 100)


def fondo_oceano(window_width, window_height):
    # El oceano
    arcade.draw_lrtb_rectangle_filled(0, window_width, 5*window_height/6, 0, arcade.color.BLUE)
    # El cielo
    arcade.draw_lrtb_rectangle_filled(0, window_width, window_height, 5*window_height/6, arcade.color.SKY_BLUE)
    # La línea de horizonte
    arcade.draw_line(0, 5*window_height/6, window_width, 5*window_height/6, arcade.color.BLACK, 0.1)
    # La isla del fondo
    arcade.draw_line(window_width/2-15, 5*window_height/6+0.1, window_width/2+15, 5*window_height/6+0.1, arcade.color.BROWN_NOSE, 2.4)


def barco_con_vela(centro_barco_x, centro_barco_y):
    x = 2/3*centro_barco_x
    y = 1/2*centro_barco_y
    x2 = 1/3*centro_barco_x
    y2 = 5*y
    mastil_width = centro_barco_x/70
    x3 = mastil_width/2
    # El cuerpo del barco
    arcade.draw_polygon_filled(((centro_barco_x-x, centro_barco_y+y), (centro_barco_x-x2, centro_barco_y-y),
                                (centro_barco_x+x2, centro_barco_y-y), (centro_barco_x+x, centro_barco_y+y)),
                               arcade.color.DARK_BROWN)
    # La bandera del barco
    arcade.draw_line(centro_barco_x, centro_barco_y+y, centro_barco_x, centro_barco_y+y2, arcade.color.DARK_BROWN, mastil_width)
    arcade.draw_triangle_filled(centro_barco_x+x3, 2*centro_barco_y, centro_barco_x+x3, centro_barco_y+y2,
                                centro_barco_x+x2/2, 2*centro_barco_y, arcade.color.WHITE)


def oleaje(window_width, window_height):
    for i in range(0, window_height, 20):
        for j in range(0, window_width, 20):
            arcade.draw_arc_outline(j, i, 20, 20, arcade.color.SKY_BLUE, 0, 90, 1, 0, 256)
            arcade.draw_arc_outline(j, i, 20, 20, arcade.color.SKY_BLUE, 90, 180, 1, 0, 256)
            arcade.draw_arc_outline(j, i, 20, 20, arcade.color.SKY_BLUE, 45, 135, 1, 0, 256)


def nube(centro_nube, anchura_nube, altura_nube, radio_circulos):
    arcade.draw_lrtb_rectangle_filled(centro_nube[0]-anchura_nube/2+radio_circulos, centro_nube[0]+anchura_nube/2-radio_circulos,
                                      centro_nube[1]+altura_nube/2-radio_circulos, centro_nube[1]-altura_nube/2+radio_circulos,
                                      arcade.color.DARK_GRAY)
    for i in range(0, anchura_nube-radio_circulos, radio_circulos):
        arcade.draw_arc_filled(centro_nube[0] - anchura_nube/2 + radio_circulos + i,
                               centro_nube[1] + altura_nube/2 - radio_circulos,
                               radio_circulos, radio_circulos, arcade.color.DARK_GRAY, 0, 180, 0, 256)
    for j in range(0, anchura_nube-radio_circulos, radio_circulos):
        arcade.draw_arc_filled(centro_nube[0] - anchura_nube / 2 + radio_circulos + j,
                               centro_nube[1] - altura_nube / 2 + radio_circulos,
                               radio_circulos, radio_circulos, arcade.color.DARK_GRAY, 180, 360, 0, 256)
    for k in range(0, altura_nube-radio_circulos, radio_circulos):
        arcade.draw_arc_filled(centro_nube[0] - anchura_nube / 2 + radio_circulos,
                               centro_nube[1] - altura_nube / 2 + radio_circulos + k,
                               radio_circulos, radio_circulos, arcade.color.DARK_GRAY, 90, 270, 0, 256)
    for r in range(0, altura_nube-radio_circulos, radio_circulos):
        arcade.draw_arc_filled(centro_nube[0] + anchura_nube / 2 - radio_circulos,
                               centro_nube[1] - altura_nube / 2 + radio_circulos + r,
                               radio_circulos, radio_circulos, arcade.color.DARK_GRAY, 270, 450, 0, 256)


arcade.open_window(600, 600, 'Drawing Example')

arcade.start_render()

fondo_oceano(600, 600)
nube((400, 550), 100, 50, 10)
nube((150, 520), 80, 40, 10)
nube((60, 540), 80, 40, 8)
pajaro(50, 60, 530)
pajaro(65, 76, 535)
pajaro(55, 79, 550)
pajaro(70, 100, 515)
pajaro(40, 68, 505)
oleaje(600, 500)
barco_con_vela(210, 65)

arcade.finish_render()

arcade.run()
