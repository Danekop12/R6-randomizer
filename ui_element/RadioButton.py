import pygame

from ui_element.GraphicElement import GraphicElement


class RadioButton(GraphicElement):
    def __init__(self, radius, pos1, pos2, is_pressed1=True, is_pressed2=False, border_size=5):
        super().__init__(pos1, (radius, radius))
        self.radius = radius
        self.pos1 = pos1
        self.pos2 = pos2
        self.is_pressed1 = is_pressed1
        self.is_pressed2 = is_pressed2
        self.border_size = border_size

    def render_element(self, screen):
        if self.is_pressed1:
            self.selected_button_render(screen, self.pos1)
            self.offline_button_render(screen, self.pos2)
        elif self.is_pressed2:
            self.selected_button_render(screen, self.pos2)
            self.offline_button_render(screen, self.pos1)
        else:
            print("Error")

    def click_first_button(self):
        self.is_pressed1 = True
        self.is_pressed2 = False

    def click_seconds_button(self):
        self.is_pressed1 = False
        self.is_pressed2 = True

    def press_button(self, coord):
        if self.pos1[0] - self.radius <= coord[0] <= self.pos1[0] + self.radius and\
                self.pos1[1] - self.radius <= coord[1] <= self.pos1[1] + self.radius:
            self.click_first_button()
        if self.pos2[0] - self.radius <= coord[0] <= self.pos2[0] + self.radius and\
                self.pos2[1] - self.radius <= coord[1] <= self.pos2[1] + self.radius:
            self.click_seconds_button()

    def selected_button_render(self, screen, pos):
        pygame.draw.circle(screen, (255, 50, 50), pos, self.radius)
        pygame.draw.circle(screen, (0, 120, 120), pos, self.radius, self.border_size)

    def offline_button_render(self, screen, pos):
        pygame.draw.circle(screen, (255, 255, 255), pos, self.radius)
        pygame.draw.circle(screen, (0, 120, 120), pos, self.radius, self.border_size)
