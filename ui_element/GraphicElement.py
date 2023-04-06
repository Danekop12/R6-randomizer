"""
Describes base class for all graphical children
responsible for storing element's size and position
can check if mouse was clicked on it
"""


class GraphicElement:
    def __init__(self, pos, size, name=None, is_visible=True, is_enabled=True):
        self.x, self.y = pos
        self.width, self.height = size
        if name is None:
            name = hash(self)
        self.name = f"{type(self)}.{name}"
        self.is_visible = is_visible
        self.is_enabled = is_enabled

    def render(self, screen):
        if self.is_visible:
            self.render_element(screen)

    def render_element(self, screen):
        pass

    def process_event(self, event):
        if self.is_enabled:
            self.process_event_element(event)

    def process_event_element(self, screen):
        pass


    # TODO: Check to be a positive
    # def click(self):
    #      self.on

    def check_if_clicked(self, coord):
        print("check_if_clicked")
        print(self.x, self.y)
        print(self.width + self.x, self.height + self.y)
        print(coord)
        return self.x <= coord[0] <= self.width + self.x and \
               self.y <= coord[1] <= self.height + self.y
