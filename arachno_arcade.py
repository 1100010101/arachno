# This is arcade library version


import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        SPRITE_SCALING_FLY = 0.6
        SPRITE_SCALING_SPIDER = 1.2

        FLY_COUNT = 10

        # Create the sprite lists
        self.spider_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.spider_sprite = arcade.Sprite("images/spider.png", SPRITE_SCALING_SPIDER)
        self.spider_sprite.center_x = 50 # Starting position
        self.spider_sprite.center_y = 50
        self.spider_list.append(self.spider_sprite)

        # Create the coins
        for i in range(FLY_COUNT):

            # Create the fly instance
            
            fly = arcade.Sprite("images/fly.png", SPRITE_SCALING_FLY)

            # Position the fly
            fly.center_x = random.randrange(SCREEN_WIDTH)
            fly.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the fly to the lists
            self.fly_list.append(fly)
            pass

        def on_draw(self):
            """ Render the screen. """
            arcade.start_render()
            # Your drawing code goes here

        def update(self, delta_time):
            """ All the logic to move, and the game logic goes here. """
            pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

