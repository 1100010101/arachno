#arachno game

# import pygame
# import pygame.locals

# def load_tile_table(filename, width, height):
#     image = pygame.image.load(filename).convert()
#     image_width, image_height = image.get_size()
#     tile_table = []
#     for tile_x in range(0, image_width/width):
#         line = []
#         tile_table.append(line)
#         for tile_y in range(0, image_height/height):
#             rect = (tile_x*width, tile_y*height, width, height)
#             line.append(image.subsurface(rect))
#     return tile_table

# if __name__=='__main__':
#     pygame.init()
#     screen = pygame.display.set_mode((128, 98))
#     screen.fill((255, 255, 255))
#     table = load_tile_table("ground.png", 24, 16)
#     for x, row in enumerate(table):
#         for y, tile in enumerate(row):
#             screen.blit(tile, (x*32, y*24))
#     pygame.display.flip()
#     while pygame.event.wait().type != pygame.locals.QUIT:
#         pass

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

#green color

green = (0,128,0)

#red color

red = (255,0,0)

#hexagon

kuusikulmio = [(400, 50) , (425, 50), (440, 68), (425, 83),(400, 83) , (382, 68)]

#rectangle

nelio = pygame.Rect(50, 50, 100, 100)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.draw.rect(screen, green, nelio )
    #piirretään kuusikulmio
    pygame.draw.polygon(screen, red, kuusikulmio)
    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()