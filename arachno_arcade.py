# This is arcade library version


import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        SPRITE_SCALING_FLY = 0.4
        SPRITE_SCALING_SPIDER = 1.2
        SPRITE_SCALING_BLOCK = 0.5

        FLY_COUNT = 10



        # Create the sprite lists
        self.spider_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()


        # Score
        self.score = 0

        # Set up the walls
        

        topwall = 0

        #upper wall
        for i in range(30):
            wall = arcade.Sprite("images/block.png", SPRITE_SCALING_BLOCK)
            wall.center_x = topwall
            wall.center_y = 580
            topwall = topwall + 53
            self.wall_list.append(wall)


        topwall = 0
        #lower wall
        for i in range(30):
            wall = arcade.Sprite("images/block.png", SPRITE_SCALING_BLOCK)
            wall.center_x = topwall
            wall.center_y = 30
            topwall = topwall + 53
            self.wall_list.append(wall)


        # Set up the player
        # Character image from kenney.nl
        self.spider_sprite = arcade.Sprite("images/spider.png", SPRITE_SCALING_SPIDER)
        self.spider_sprite.center_x = 100 # Starting position
        self.spider_sprite.center_y = 100
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
        

        self.physics_engine = arcade.PhysicsEngineSimple(self.spider_sprite, self.wall_list)
        pass

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed """

        if key == arcade.key.UP:
            self.spider_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.spider_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.spider_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.spider_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.spider_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.spider_sprite.change_x = 0


    def on_draw(self):
            """ Render the screen. """
            arcade.start_render()
            self.spider_list.draw()
            self.fly_list.draw()
            self.wall_list.draw()
            arcade.finish_render()
            # Your drawing code goes here

    def update(self, delta_time):
            """ All the logic to move, and the game logic goes here. """
            fly_hit_list = arcade.check_for_collision_with_list(self.spider_sprite, self.fly_list)
            for fly in fly_hit_list:
                fly.kill()
                self.score += 1
            self.physics_engine.update()
            pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

