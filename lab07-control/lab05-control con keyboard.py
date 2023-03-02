""" Lab 7 - User Control """

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


def barco_con_vela(centro_barco_x, centro_barco_y, anchura_barco, altura_cuerpo_barco):
    # El cuerpo del barco
    arcade.draw_polygon_filled(((centro_barco_x-anchura_barco/2, centro_barco_y+altura_cuerpo_barco/2),
                                (centro_barco_x-(anchura_barco*2/9), centro_barco_y-altura_cuerpo_barco/2),
                                (centro_barco_x+(anchura_barco*2/9), centro_barco_y-altura_cuerpo_barco/2),
                                (centro_barco_x+anchura_barco/2, centro_barco_y+altura_cuerpo_barco/2)),
                               arcade.color.DARK_BROWN)
    # La bandera del barco
    arcade.draw_line(centro_barco_x, centro_barco_y+altura_cuerpo_barco/2,
                     centro_barco_x, centro_barco_y+altura_cuerpo_barco/2*6,
                     arcade.color.DARK_BROWN, anchura_barco/70)
    arcade.draw_triangle_filled(centro_barco_x+anchura_barco/140, centro_barco_y+altura_cuerpo_barco/2*6,
                                centro_barco_x+anchura_barco/140, centro_barco_y+altura_cuerpo_barco/2*3,
                                centro_barco_x+(anchura_barco*2/9)/2, centro_barco_y+altura_cuerpo_barco/2*3,
                                arcade.color.WHITE)


# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class Barco_con_vela:
    def __init__(self, position_x, position_y, change_x, change_y, anchura, altura):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.anchura = anchura
        self.altura = altura

    def draw(self):
        """ Draw the barcos with the instance variables we have. """
        barco_con_vela(self.position_x, self.position_y, self.anchura, self.altura)

    def update(self):
        # Move the barco
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the barco hit the edge of the screen. If so, change direction
        if self.position_x < self.anchura/2:
            self.position_x = self.anchura/2

        if self.position_x > SCREEN_WIDTH - self.anchura/2:
            self.position_x = SCREEN_WIDTH - self.anchura/2

        if self.position_y < self.altura/2:
            self.position_y = self.altura/2

        if self.position_y-self.altura/2 > SCREEN_HEIGHT*5/6:
            self.position_y = SCREEN_HEIGHT*5/6 + self.altura/2


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # Create our barco
        self.barco = Barco_con_vela(310, 165, 0, 0, 105, 30)

    def on_draw(self):
        arcade.start_render()

        # Background
        fondo_oceano(SCREEN_WIDTH, SCREEN_HEIGHT)
        pajaro(50, 60, SCREEN_HEIGHT*5/6+30)
        pajaro(65, 76, SCREEN_HEIGHT*5/6+35)
        pajaro(55, 79, SCREEN_HEIGHT*5/6+50)
        pajaro(70, 100, SCREEN_HEIGHT*5/6+15)
        pajaro(40, 68, SCREEN_HEIGHT*5/6+5)

        # La bola
        self.barco.draw()

    def update(self, delta_time):
        self.barco.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.barco.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.barco.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.barco.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.barco.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.barco.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.barco.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()