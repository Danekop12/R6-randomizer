import pygame

# Initialize Pygame
pygame.init()

# Set the window size and title
window_size = (400, 400)
window_title = "Button Example"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Define the button's dimensions and position
button_width = 150
button_height = 50
button_x = (screen.get_width() - button_width) // 2
button_y = (screen.get_height() - button_height) // 2

# Define the button's label text
button_text = "Click me!"

# Create a font object for the button label
font = pygame.font.Font(None, 36)

# Render the button label text
button_label = font.render(button_text, 1, (255, 255, 255))

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the mouse is hovering over the button
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
        # If the mouse is hovering over the button, draw a darker version of the button
        pygame.draw.rect(screen, (0, 0, 150), (button_x, button_y, button_width, button_height))
    else:
        # If the mouse is not hovering over the button, draw the regular button
        pygame.draw.rect(screen, (0, 0, 255), (button_x, button_y, button_width, button_height))

    # Blit the button label onto the button
    screen.blit(button_label, (button_x + (button_width - button_label.get_width()) // 2, button_y + (button_height - button_label.get_height()) // 2))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
