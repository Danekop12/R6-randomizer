amount_players = ["1",
                  "2",
                  "3",
                  "4",
                  "5"]
# TODO:
# TODO:
# Create a variable to track the current selected option
import pygame

# Initialize pygame
pygame.init()

# Set the window size and title
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dropdown List")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
dimention = (20, 50)
el_size = (100, 20)
font = pygame.font.Font(None, 32)
bg = pygame.image.load("pictures/buttons/bg.png")


# Create a list of options for the dropdown
options = ["Option 1", "Option 2", "Option 3"]
new_list = amount_players[0:2]
print(new_list)
# Create a variable to track the current selected option
selected_option = 0

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0, 0))
    # Draw the dropdown box
    #pygame.draw.rect(screen, (255, 255, 255), (50, 50, 200, 40))
    #players_num.show(screen, pygame.mouse.get_pos())
    # Draw the currently selected option

    #text = font.render(options[selected_option], True, (0, 0, 0))
    #screen.blit(text, (60, 60))

    # Check for a mouse click on the dropdown box
    #if event.type == pygame.MOUSEBUTTONUP:
        # Get the mouse position
        #mouse_pos = pygame.mouse.get_pos()
        #players_num.click(mouse_pos)
    pygame.display.flip()

# Quit pygame
pygame.quit()
