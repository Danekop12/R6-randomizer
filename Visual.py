import pygame
import random

from ui_element.Icon import Icon
from ui_element.Button import Button
from ui_element.PageManager import PageManager
from ui_element.RadioButton import RadioButton

WIDTH = 1080
HEIGHT = 1920

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
bg = pygame.image.load("pictures/buttons/bg.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 30
font = pygame.font.SysFont("Arial", 25)
pygame.display.set_caption("R6 randomizer")
pygame.display.set_icon(pygame.image.load("pictures/buttons/icon.png"))

PATH_TO_ICONS = "pictures/operators"
PATH_TO_BUTTONS = "pictures/buttons"
#space_between_att_def = 1050
space_between_att_def = 400
distance_between_icons = 10
PIC_SIZE = 40
selected_option = 0
determined_icon_size = 120
amount_games = 1
amount_games_after = 1

operators_choose_area_size = (200, 400)
drop_down_el_size = (200, 30)

DEFENDER_OPERATORS = ["Recruit", "Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachanka",
                      "Jäger", "Bandit", "Frost", "Valkyrie", "Caveira", "Echo", "Mira", "Lesion", "Ela",
                      "Vigil", "Maestro", "Alibi", "Clash", "Kaid", "Mozzie", "Warden", "Goyo", "Wamai",
                      "Oryx", "Melusi", "Aruni", "Thunderbird", "Thorn", "Azami", "Solis"]

ATTACKER_OPERATORS = ["Recruit", "Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz",
                      "Fuze", "Blitz", "Iq", "Buck", "Blackbeard", "Capitao", "Hibana", "Jackal", "Ying",
                      "Zofia", "Dokkaebi", "Lion", "Finka", "Maverick", "Nomad", "Gridlock", "Nøkk", "Amaru",
                      "Kali", "Iana", "Ace", "Zero", "Flores", "Osa", "Sens", "Grim", "Brava"]
ALL_OPERATORS = (DEFENDER_OPERATORS, ATTACKER_OPERATORS)
ALL_TEXT_ON_OPERATOR_BAN_PAGE = [["ATTACKER_OPERATORS", (200, 50)], ["DEFENDER_OPERATORS", (200 + space_between_att_def, 50)],
                        ["Quick", (170, 950)], ["Ranked", (300, 950)], ["How many players?", (1300, 900)]]
big_icons_att = []
big_icons_def = []

amount_players = ["1",
                  "2",
                  "3",
                  "4",
                  "5"]
"""
Generates relative path to operator`s icon file
Get icons from      https://r6operators.marcopixel.eu  
"""


class Operator:
    def __init__(self, pos, size, name, operator_type="attacker"):
        self.x, self.y = pos
        self.size = size
        self.name = name
        self.operator_type = operator_type
        self.path = generate_filename(self.name, PATH_TO_ICONS)
        self.picture = pygame.image.load(self.path).convert_alpha()
        self.below_text = 30
        if self.operator_type == "attacker":
            self.multiplier = 0
        if self.operator_type == "defender":
            self.multiplier = 1

    def show_icon(self, screen):
        screen.blit(self.picture, (self.x, self.y))


    def change_picture_size(self, size):
        self.picture = pygame.transform.scale(self.picture, size)


    def placeText(self):
        caption = font.render(text, False, WHITE)
        screen.blit(caption, coords)


def generate_filename(name, path):
    return f"{path}/{name.lower()}.png"


def init_operator(object):
    return Operator((200, 200), determined_icon_size, object)


"""Change func"""
def initIcon(pic, multiplier):
    return Icon((100 + multiplier * space_between_att_def + (PIC_SIZE + distance_between_icons) * (pic[0] % 5),
                 (PIC_SIZE + distance_between_icons) * ((pic[0] // 5) + 1)), (PIC_SIZE, PIC_SIZE), pic[1].picture,
                pic[1].name)


def changeSizeOfIconList(list_to_change):
    for operator in list_to_change:
        operator.size = determined_icon_size


def placeText(text, coords):
    caption = font.render(text, False, WHITE)
    screen.blit(caption, coords)


def make_new_operator_list_without_bans(old_list):
    new_list = []
    for operator_old in old_list:
        if not operator_old.is_pressed:
            new_list.append(Operator((200, 200), determined_icon_size, operator_old.name))
    return new_list

def choose_n_random_elements_from_list(n, list):
    tmp_list = [x for x in list]
    random.shuffle(tmp_list)
    return tmp_list[0:n]


def show_chosen_icon(amount_op, op_num, object, screen):
    x_coord = ((WIDTH // amount_op) * (op_num)) - 100
    object.pos = (x_coord, 200)
    object.show_icon(screen)
    # Write name of operator


def show_big_icon(amount, list, screen):
    tmp_list = choose_n_random_elements_from_list(amount, list)
    for index, element in enumerate(tmp_list):
        show_chosen_icon(amount, index, element, screen)


# TODO: Create 2 list with bigger icon. Create random set of operators in one list. Draw icons. Write text below.
# TODO: Draw icons on the next screen, with text below
# TODO: Function for side change (add value Side, change when needed)
# TODO: Put text (placeText)
# TODO: Recruits

#start_button = Button((700, 820), pygame.image.load(generate_filename("Start_button", PATH_TO_BUTTONS)), (400, 200))
#next_button = Button((700, 820), pygame.image.load(generate_filename("Next_Button_2", PATH_TO_BUTTONS)), (400, 180))
#
start_button = Button((500, 520), pygame.image.load(generate_filename("Start_button", PATH_TO_BUTTONS)), (400, 200))
next_button = Button((500, 520), pygame.image.load(generate_filename("Next_Button_2", PATH_TO_BUTTONS)), (400, 180))

attack_or_defender_button = RadioButton(15, (600, 80), (150 + space_between_att_def, 80))
quick_or_ranked_button = RadioButton(10, (200, 1000), (350, 1000))

#players_num = DropDownList((1300, 950), drop_down_el_size, amount_players, font, 2, False)

# Create a list of pass to each Icon
file_names_def = list(map(lambda name: init_operator(name), DEFENDER_OPERATORS))

file_names_att = list(map(lambda name: init_operator(name), ATTACKER_OPERATORS))
# Creating a list of Icons-objects with their coords
icons_att = list(map(lambda pic: initIcon(pic, 0), enumerate(file_names_att)))
icons_def = list(map(lambda pic: initIcon(pic, 1), enumerate(file_names_def)))


def set_amount_games():
    global amount_games, amount_games_after
    if quick_or_ranked_button.is_pressed1:
        amount_games = 2
        amount_games_after = 1
    elif quick_or_ranked_button.is_pressed2:
        amount_games = 3
        amount_games_after = 4


def ban_operator_screen():
    for event in pygame.event.get():
        screen.blit(bg, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            for icon in icons_att:
                if icon.check_if_clicked(event.pos):
                    icon.click()
            for icon in icons_def:
                if icon.check_if_clicked(event.pos):
                    icon.click()
            if start_button.check_if_clicked(event.pos):
                start_button.click()
            attack_or_defender_button.press_button(pygame.mouse.get_pos())
            quick_or_ranked_button.press_button(pygame.mouse.get_pos())
            players_num.click(pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            pygame.quit()
        for text in ALL_TEXT_ON_OPERATOR_BAN_PAGE:
            placeText(text[0], text[1])

        MOUSE_POS = pygame.mouse.get_pos()

        players_num.show(screen, MOUSE_POS)
        start_button.render(screen)
        attack_or_defender_button.show(screen)
        quick_or_ranked_button.show(screen)
        for icon in icons_att:
            icon.show(MOUSE_POS, screen)
        for icon in icons_def:
            icon.show(MOUSE_POS, screen)


def initialize_var_operator_show_screen():
    # TODO: Change to class Operators, give name. Add coords and size
    global big_icons_att, big_icons_def
    big_icons_def = make_new_operator_list_without_bans(icons_def)
    big_icons_att = make_new_operator_list_without_bans(icons_att)
    set_amount_games()


def switch_side():
    if attack_or_defender_button.is_pressed1:
        attack_or_defender_button.click_seconds_button()
    if attack_or_defender_button.is_pressed2:
        attack_or_defender_button.click_first_button()


def operator_show_screen():
    initialize_var_operator_show_screen()
    amount_clicks = 0
    while amount_clicks != amount_games * 2 + amount_games_after:
        #print(amount_clicks, amount_games)
        if amount_clicks < amount_games:
            for event in pygame.event.get():
                screen.blit(bg, (0, 0))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if next_button.check_if_clicked(event.pos):
                        amount_clicks = + 1
                        if amount_clicks == amount_games - 1:
                            switch_side()
                    # next_button.is_clicked == False
                show_big_icon(int(players_num.chosen_el), big_icons_att, screen)
                next_button.render(screen)
                clock.tick(FPS)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    pygame.quit()
        elif amount_clicks < amount_games * 2:
            for event in pygame.event.get():
                screen.blit(bg, (0, 0))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if next_button.check_if_clicked(event.pos):
                        amount_clicks = + 1
                        if amount_clicks == amount_games - 1:
                            switch_side()
                show_big_icon(int(players_num.chosen_el), big_icons_def, screen)
                clock.tick(FPS)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    pygame.quit()
        elif amount_clicks == amount_games * 2:
            for event in pygame.event.get():
                screen.blit(bg, (0, 0))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    attack_or_defender_button.press_button(pygame.mouse.get_pos())
                    if next_button.check_if_clicked(event.pos):
                        amount_clicks = + 1
            attack_or_defender_button.show(screen)
            clock.tick(FPS)
            pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
        elif amount_clicks < amount_games * 2 + amount_games_after:
            pass

    """
    initialisation:
        make big icons
        define amount rounds
    loop:
        if fst_stage
            show_fst_stage
            if clicked_next
                ++side
        if snd_stage
            show_snd_stage
            if clicked_next
                ++side
        if  fst_stage + snd_stage:
            ask_side
            show_stage
            if clicked_next and asked_side:
                ++side

        if fst_stage + snd_stage:
            show_stage
            ++side
    """

    """
    for event in pygame.event.get():
        screen.blit(bg, (0, 0))

        if event.type == pygame.MOUSEBUTTONDOWN:
            show_big_icon(int(players_num.chosen_el), big_icons_att, screen)
        if event.type == pygame.QUIT:
            pygame.quit()
"""


def mainloop():
    page_manager = PageManager(screen, None, (1920, 1080))
    while not page_manager.quit_game:
        for event in pygame.event.get():
            page_manager.process_event(event)

        page_manager.render()
        clock.tick(FPS)
        pygame.display.flip()

    """ The infinite loop where things happen """
    """
    while not start_button.is_clicked:
        ban_operator_screen()

        pygame.display.update()
    while start_button.is_clicked:
        initialize_var_operator_show_screen()
        operator_show_screen()
    """


# ==================



mainloop()



