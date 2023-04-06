import pygame
from pygame.constants import KEYDOWN, K_ESCAPE


class Page:
    def __init__(self, game, page_manager, screen, screen_size):
        self.screen_size = screen_size
        self.screen = screen
        self.game = game
        self.page_manager = page_manager
        self.graphical_elements = []

    def render_page_background(self):
        pass

    def render_children(self):
        for graphical_element in self.graphical_elements:
            graphical_element.render(self.screen)

    def render(self):
        self.render_page_background()
        self.render_children()

    def process_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
        for graphical_element in self.graphical_elements:
            graphical_element.process_event(event)

    def go_to_next_page(self):
        pass

    def go_to_prev_page(self):
        pass
#Масштабивровние
