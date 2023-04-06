import pygame

from ui_element.GraphicElement import GraphicElement


class Button(GraphicElement):
    def __init__(self, pos, image, size=(100, 100)):
        super().__init__(pos, size)
        self.image = image
        self.image_size = pygame.transform.scale(self.image, size)

    def render_element(self, screen):
        screen.blit(self.image_size, (self.x, self.y))

    def click(self):
        self.is_clicked = not self.is_clicked
