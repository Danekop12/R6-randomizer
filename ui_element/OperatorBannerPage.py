from pygame import K_ESCAPE
from pygame.constants import KEYDOWN

from Constants import DEFENDER_OPERATORS, ATTACKER_OPERATORS, PATH_TO_BUTTONS, amount_players, drop_down_el_size, \
    PATH_TO_ICONS, ALL_TEXT_ON_OPERATOR_BAN_PAGE

import pygame

from ui_element.Page import Page
from ui_element.Button import Button
from ui_element.DropDownList import DropDownList
from ui_element.GraphicElementContainer import GraphicElementContainer
from ui_element.Icon import Icon
from ui_element.RadioButton import RadioButton
from ui_element.Text import Text

SPACE_BETWEEN_ATT_DEF = 500


def generate_filename(name, path):
    return f"{path}/{name.lower()}.png"


class OperatorBannerPage(Page, GraphicElementContainer):
    """Class represents page where we ban operators for this match"""

    def __init__(self, game, page_manager, screen, screen_size):
        super().__init__(game, page_manager, screen, screen_size)
        unscaled_background = pygame.image.load("pictures/buttons/bg.png")
        self.background = pygame.transform.scale(unscaled_background, screen_size)
        self.graphical_elements = self._create_graphical_elements()

    def render_page_background(self):
        self.screen.blit(self.background, (0, 0))

    def _create_graphical_elements(self):
        elements = [
            self._create_container_with_text(ALL_TEXT_ON_OPERATOR_BAN_PAGE),
            self._create_container_with_icons(100, ATTACKER_OPERATORS),
            self._create_container_with_icons(100 + SPACE_BETWEEN_ATT_DEF, DEFENDER_OPERATORS),
            Button((500, 520), pygame.image.load(generate_filename("Start_button", PATH_TO_BUTTONS))),
            RadioButton(15, (600, 80), (150 + SPACE_BETWEEN_ATT_DEF, 80)),
            RadioButton(10, (200, 1000), (350, 1000)),
            DropDownList((800, 650), drop_down_el_size, amount_players, pygame.font.SysFont("Arial", 25))
        ]
        return elements

    def _create_container_with_icons(self, starting_x, operators_list):
        container = GraphicElementContainer((100, 100), (600, 600))
        PIC_SIZE = 40
        distance_between_icons = 10
        for index, operator_name in enumerate(operators_list):
            icon = Icon((starting_x + (PIC_SIZE + distance_between_icons) * (index % 5),
                         (PIC_SIZE + distance_between_icons) * ((index // 5) + 1)), (PIC_SIZE, PIC_SIZE),
                        pygame.image.load(generate_filename(operator_name, PATH_TO_ICONS)), operator_name)
            container.add_element(icon)
        return container

    def _create_container_with_text(self, text_list):
        container = GraphicElementContainer((100, 100), (600, 600))
        for elements in text_list:
            textes = Text(elements[1], (20, 50), elements[0], pygame.font.SysFont("Arial", 25))
            container.add_element(textes)
        return container
