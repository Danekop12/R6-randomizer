import pygame

from Constants import WHITE, BLACK
from ui_element.GraphicElement import GraphicElement


#font = pygame.font.SysFont("Arial", 25)

class DropDownList(GraphicElement):
    def __init__(self, pos, size_of_element, list_of_var, font, chosen_el=4, is_opened=False):
        super().__init__(pos, size_of_element)
        self.list_text = list_of_var
        self.chosen_el = chosen_el
        self.font = font
        self.is_opened = is_opened

    def render_element(self, screen):
        self.always_show_el(screen)
        if self.is_opened:
            self.show_whole_list(screen)
            # self.check_if_hover(screen, coord)

    def show_whole_list(self, screen):
        for i in range(len(self.list_text)):
            rect = (self.x, self.y + (self.height * (i + 1)), self.width, self.height)
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)
            text = self.font.render(self.list_text[i], True, BLACK)
            screen.blit(text, (self.x + self.width // 3, self.y + (self.height * (i + 1))))

    def always_show_el(self, screen):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text = self.font.render(str(self.chosen_el), True, BLACK)
        screen.blit(text, (self.x + self.width // 3, self.y))

    def check_if_hover(self, screen, coord):
        for i in range(len(self.list_text)):
            if self.x <= coord[0] <= self.width + self.x and \
               self.y + (self.height * (i + 1)) <= coord[1] <= self.height * (i + 2) + self.y:
                rect = (self.x, self.y + (self.height * (i + 1)), self.width, self.height)
                pygame.draw.rect(screen, (20, 20, 190), rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
                text = self.font.render(self.list_text[i], True, BLACK)
                screen.blit(text, (self.x + self.width // 3, self.y + (self.height * (i + 1))))
                break

    def click(self, coord):
        if self.x <= coord[0] <= self.width + self.x and self.y <= coord[1] <= self.height + self.y:
            self.is_opened = not self.is_opened
            pygame.time.delay(150)
            #TODO: mills counter, add delay attribute
        if self.is_opened:
            for i in range(len(self.list_text)):
                if self.x <= coord[0] <= self.width + self.x and \
                   self.y + (self.height * (i + 1)) <= coord[1] <= self.height * (i + 2) + self.y:
                    self.chosen_el = self.list_text[i]
                    self.is_opened = False