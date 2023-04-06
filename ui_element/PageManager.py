from ui_element.OperatorBannerPage import OperatorBannerPage


class PageManager:
    def __init__(self, screen, game, screen_size):
        self._screen = screen
        self._pages = [OperatorBannerPage(game, self, screen, screen_size)]
        self._active_page_index = 0
        self.quit_game = False

    def get_active_page(self):
        return self._pages[self._active_page_index]

    def set_active_page(self, page_index):
        self._active_page_index = page_index

    def process_event(self, event):
        self.get_active_page().process_event(event)

    def render(self):
        self.get_active_page().render()
