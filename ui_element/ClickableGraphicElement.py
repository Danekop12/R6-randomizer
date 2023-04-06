from ui_element.GraphicElement import GraphicElement


class ClickableGraphicElement(GraphicElement):
    def __init__(self, pos, size, is_hovered, is_clicked):
        super().__init__(pos, size)
        self.is_hovered = is_hovered
        self.is_clicked = is_clicked

    def check_if_clicked(self, coord):
        return self.x <= coord[0] <= self.width + self.x and \
               self.y <= coord[1] <= self.height + self.y
