from ui_element.GraphicElement import GraphicElement
from Constants import WHITE


class Text(GraphicElement):
    def __init__(self, pos, size, text, font):
        super().__init__(pos, size)
        self.pos = pos
        self.font = font
        self.text = self.font.render(text, False, WHITE)

    def render_element(self, screen):
        screen.blit(self.text, self.pos)

    def set_text(self, new_text):
        self.text = new_text

    def set_font(self, text_size, text_style="Arial"):
        self.font = (text_style, text_size)

