import pygame

from ui_element.GraphicElement import GraphicElement


class GraphicElementContainer(GraphicElement):
    def __init__(self, pos, size, elements_inside=None):
        super().__init__(pos, size)
        if elements_inside is None:
            elements_inside = []
        self.children = elements_inside

    def add_element(self, element):
        self.children.append(element)

    def remove_element(self, element):
        self.children.remove(element)

    def get_flat_elements_current_first(self):
        elements = self.children.copy()
        for element in self.children:
            if type(element) == GraphicElementContainer:
                elements += element.get_flat_elements_current_first()
        return elements

    def get_flat_elements_current_last(self):
        elements = []
        for element in self.children:
            if type(element) == GraphicElementContainer:
                elements += element.get_flat_elements_current_last()
        elements += self.children.copy()
        return elements

    def render(self, screen):
        for graphical_element in self.children:
            graphical_element.render(screen)
