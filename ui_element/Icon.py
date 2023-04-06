from ui_element.ClickableGraphicElement import ClickableGraphicElement
from ui_element.GraphicElement import GraphicElement
import pygame


class Icon(ClickableGraphicElement):
    def __init__(self, pos, size, icon, name, is_clicked=False):
        super().__init__(pos, size, is_hovered=False, is_clicked=False)
        if icon == "":
            raise Exception('There is no icon for this operator')
        self.icon = pygame.transform.scale(icon, size)
        self.is_pressed = is_clicked
        self.is_hovered = False
        self.name = name

    def check_state(self, mouse_coords):
        if self.x <= mouse_coords[0] <= self.width + self.x and self.y <= mouse_coords[1] <= self.height + self.y:
            self.is_hovered = True
        else:
            self.is_hovered = False

    def render_element(self, screen):
        if self.is_pressed:
            pygame.draw.rect(screen, (255, 120, 120), (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
            screen.blit(self.icon, (self.x, self.y))
        elif self.is_pressed:
            pygame.draw.rect(screen, (255, 0, 0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
            screen.blit(self.icon, (self.x, self.y))
        elif self.is_hovered:
            pygame.draw.rect(screen, (0, 125, 125), (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
            screen.blit(self.icon, (self.x, self.y))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
            screen.blit(self.icon, (self.x, self.y))

    def click(self):
         self.is_pressed = not self.is_pressed

    def show_only_icon(self, screen):
        screen.blit(self.icon, (self.x, self.y))

    def change_size(self, new_size):
        self.width, self.height = new_size, new_size


