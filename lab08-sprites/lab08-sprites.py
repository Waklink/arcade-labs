import arcade
import random

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GOOD = 0.2
SPRITE_SCALING_BAD = 0.25
GOOD_COUNT = 150
BAD_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        """
        Initializer
        """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Variables that will hold sprite lists
        self.player_list = None
        self.good_list = None
        self.bad_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        self.player_sprite = Player(":resources:images/animated_characters/zombie/zombie_fall.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the goods
        for i in range(GOOD_COUNT):
            # Create the good instance
            # good image from arcade library
            good = arcade.Sprite(":resources:images/items/gemYellow.png", SPRITE_SCALING_GOOD)

            # Position the good
            good.center_x = random.randrange(SCREEN_WIDTH)
            good.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the good to the lists
            self.good_list.append(good)

        # Create the bads
        for i in range(BAD_COUNT):
            # Create the bad instance
            # bad image from arcade library
            bad = arcade.Sprite(":resources:images/items/star.png", SPRITE_SCALING_BAD)

            # Position the bad
            bad.center_x = random.randrange(SCREEN_WIDTH)
            bad.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the bad to the lists
            self.bad_list.append(bad)

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

        arcade.start_render()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        # Draw all the sprites.
        self.good_list.draw()
        self.player_list.draw()
        self.bad_list.draw()

    def update_player_speed(self):
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_update(self, delta_time):
        """ Movement and game logic """
        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.good_list.update()
        self.bad_list.update()

        # Generate a list of all sprites that collided with the player.
        goods_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_list)
        bads_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for good in goods_hit_list:
            good.remove_from_sprite_lists()
            self.score += 1

        for bad in bads_hit_list:
            bad.remove_from_sprite_lists()
            self.score -= 1


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()