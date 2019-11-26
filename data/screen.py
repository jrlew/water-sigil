"""
Placeholder
"""

import pygame

from .store import Store

size = width, height = 480, 360
FONT_SIZE = 24
PIXEL_SIZE = 32
WIDTH = 10
WHITE = 255, 255, 255
BLACK = 0, 0, 0
MSG_WIDTH = 150
MSG_HEIGHT = 120

class Screen():
    def __init__(self):
        self.display = pygame.display.set_mode(size)
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.store = Store.instance()


    ##########################
    # Screen Setup Functions #
    ##########################

    def init_screen(self, terrain):
        y_coord = 0
        for row in terrain:
            x_coord = 0
            for col in row:
                self.display.blit(col.image, (x_coord, y_coord))
                x_coord += PIXEL_SIZE
            y_coord += PIXEL_SIZE


    def init_info_pane(self):
        info_pane_x_offset = 320 # TODO: no magic
        # Horizontal Bars for Unit Info
        pygame.draw.rect(self.display, WHITE, [info_pane_x_offset, 0, 160, 4], 0)
        pygame.draw.rect(self.display, WHITE, [info_pane_x_offset, 29, 160, 4], 0)

        # Horizontal Dividing Bar
        pygame.draw.rect(self.display, WHITE, [info_pane_x_offset, 157, 160, 4], 0)

        # Horizontal Bars for Terrain Info
        pygame.draw.rect(self.display, WHITE, [info_pane_x_offset, 190, 160, 4], 0)
        pygame.draw.rect(self.display, WHITE, [info_pane_x_offset, 315, 160, 4], 0)

        # Vertical Bars
        pygame.draw.rect(self.display, WHITE, [info_pane_x_offset, 0, 4, 320], 0)
        pygame.draw.rect(self.display, WHITE, [width - 5, 0, 4, 320], 0)

        # Text
        self.display.blit(self.font.render("UNIT INFO", 1, (200, 200, 200)), (info_pane_x_offset + 8, 6))
        self.display.blit(self.font.render("TERRAIN INFO", 1, (200, 200, 200)), (info_pane_x_offset + 8, 165))


    def init_context_menu(self):
        # Bottom Context Message
        pygame.draw.rect(self.display, WHITE, [0, 320, width, 4], 0)
        pygame.draw.rect(self.display, WHITE, [0, 355, width, 4], 0)

        pygame.draw.rect(self.display, WHITE, [0, 320, 4, 40], 0)
        pygame.draw.rect(self.display, WHITE, [475, 320, 4, 40], 0)


    def init_all(self):
        self.init_screen(self.store.terrain)
        self.init_info_pane()
        self.init_context_menu()


    #######################
    # Info Pane Functions #
    #######################

    # TODO: Clean up formatting
    def display_unit_info(self, stats):
        info_pane_x_offset = WIDTH * PIXEL_SIZE
        info = [
            "{name} {remaining_move}/{max_move}".format(name=stats.name, remaining_move=stats.remaining_movement, max_move=stats.movement),
            "HP: {hp} / {maxhp}".format(hp=stats.current_hp, maxhp=stats.max_hp),
            "STR: {str}  DEF: {defense}".format(str=stats.strength, defense=stats.defense),
            "ACC: {acc}  EVD: {evd}".format(acc=stats.accuracy, evd=stats.evasion),
        ]
        y_offset = 34
        for line in info:
            self.display.blit(self.font.render(line, 1, (200, 200, 200)), (info_pane_x_offset + 8, y_offset))
            y_offset += (FONT_SIZE + 4)


    # TODO: Clean up parameters
    def display_terrain_info(self, terrain):
        info_pane_x_offset = WIDTH * PIXEL_SIZE
        terrain_info = [
            "{type}".format(type=terrain.type),
            "Def: {def_adjustment}".format(def_adjustment=terrain.def_adjustment),
            "Evd: {evasion_adjustment}".format(evasion_adjustment=terrain.evasion_adjustment),
        ]
        y_offset = 195
        for line in terrain_info:
            self.display.blit(self.font.render(line, 1, (200, 200, 200)), (info_pane_x_offset + 8, y_offset))
            y_offset += (FONT_SIZE + 4)


    def clear_info_pane(self):
        info_pane_x_offset = WIDTH * PIXEL_SIZE
        pygame.draw.rect(self.display, BLACK, [info_pane_x_offset + 4, 34, MSG_WIDTH, MSG_HEIGHT], 0)
        pygame.draw.rect(self.display, BLACK, [info_pane_x_offset + 4, 195, MSG_WIDTH, MSG_HEIGHT], 0)


    # TODO: Come up with a better name than context message
    def display_context_message(self, msg_text):
        pygame.draw.rect(self.display, BLACK, [8, 329, 440, 26], 0)
        self.display.blit(self.font.render(msg_text, 1, (200, 200, 200)), (8, 329))


    ####################
    # Render Functions #
    ####################

    def render_unit(self, x, y):
        self.display.blit(self.store.units[y][x].image, (x * PIXEL_SIZE, y * PIXEL_SIZE))


    def render_terrain(self, x, y):
        self.display.blit(self.store.terrain[y][x].image, (x * PIXEL_SIZE, y * PIXEL_SIZE))


    def render_highlight(self, x, y):
        self.display.blit(self.store.highlights[y][x].image, (x * PIXEL_SIZE, y * PIXEL_SIZE))


    def render_indicator(self):
        self.display.blit(self.store.indicator.image, (self.store.indicator.position.x * PIXEL_SIZE, self.store.indicator.position.y * PIXEL_SIZE))


    def render_image(self, image, x, y):
        self.display.blit(image, (x, y))
    

    def render_square(self, x, y):
        self.render_terrain( x, y)

        if self.store.units[y][x]:
            self.render_unit( x, y)

        if self.store.highlights[y][x]:
            self.render_highlight( x, y)

        if self.store.indicator.position.x == x and self.store.indicator.position.y == y:
            self.render_indicator()
