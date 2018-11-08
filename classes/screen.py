"""
Placeholder
"""

import pygame

size = width, height = 480, 360
FONT_SIZE = 24
PIXEL_SIZE = 32
PIXEL_SIZE = 32
WHITE = 255, 255, 255
BLACK = 0, 0, 0
MSG_WIDTH = 150
MSG_HEIGHT = 120

class Screen():
    def __init__(self):
        self.display = pygame.display.set_mode(size)
        self.font = pygame.font.Font(None, FONT_SIZE)


    def init_info_pane(self, state):
        info_pane_x_offset = state.level.width * PIXEL_SIZE
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


    def display_unit_info(self, state, stats):
        info_pane_x_offset = state.level.width * PIXEL_SIZE
        info = [
            "{name}".format(name=stats.name),
            "HP: {hp} / {maxhp}".format(hp=stats.current_hp, maxhp=stats.max_hp),
            "STR: {str}  DEF: {defense}".format(str=stats.strength, defense=stats.defense),
            "ACC: {acc}  EVD: {evd}".format(acc=stats.accuracy, evd=stats.evasion),
        ]
        y_offset = 34
        for line in info:
            self.display.blit(self.font.render(line, 1, (200, 200, 200)), (info_pane_x_offset + 8, y_offset))
            y_offset += (FONT_SIZE + 4)


    # TODO: Clean up parameters
    def display_terrain_info(self, state):
        info_pane_x_offset = state.level.width * PIXEL_SIZE
        ter = state.level.terrain[state.indicator.position.y][state.indicator.position.x]
        terrain_info = [
            "{type}".format(type=ter.type),
            "Def: {def_adjustment}".format(def_adjustment=ter.def_adjustment),
            "Evd: {evasion_adjustment}".format(evasion_adjustment=ter.evasion_adjustment),
        ]
        y_offset = 195
        for line in terrain_info:
            self.display.blit(self.font.render(line, 1, (200, 200, 200)), (info_pane_x_offset + 8, y_offset))
            y_offset += (FONT_SIZE + 4)


    def display_context_message(self, msg_text):
        pygame.draw.rect(self.display, BLACK, [8, 329, 440, 26], 0)
        self.display.blit(self.font.render(msg_text, 1, (200, 200, 200)), (8, 329))


    def clear_info_pane(self, state):
        info_pane_x_offset = state.level.width * PIXEL_SIZE
        pygame.draw.rect(self.display, BLACK, [info_pane_x_offset + 4, 34, MSG_WIDTH, MSG_HEIGHT], 0)
        pygame.draw.rect(self.display, BLACK, [info_pane_x_offset + 4, 195, MSG_WIDTH, MSG_HEIGHT], 0)


    def init_screen(self, terrain):
        y_coord = 0
        for row in terrain:
            x_coord = 0
            for col in row:
                self.display.blit(col.image, (x_coord, y_coord))
                x_coord += PIXEL_SIZE
            y_coord += PIXEL_SIZE

        
    def render_unit(self, unit):
        self.display.blit(unit.image, (unit.position.x * PIXEL_SIZE, unit.position.y * PIXEL_SIZE))


    def render_terrain(self, terrain, x_coord, y_coord):
        self.display.blit(terrain.image, (x_coord * PIXEL_SIZE, y_coord * PIXEL_SIZE))


    def move_indicator(self, state):
        state.screen.render_terrain(state.level.terrain[state.indicator.prev_position.y][state.indicator.prev_position.x], state.indicator.prev_position.x, state.indicator.prev_position.y)
        if not state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x] == 0:
            state.screen.render_unit(state.level.units[state.indicator.prev_position.y][state.indicator.prev_position.x])

        state.screen.render_terrain(state.level.terrain[state.indicator.position.y][state.indicator.position.x], state.indicator.position.x, state.indicator.position.y)
        if not state.level.units[state.indicator.position.y][state.indicator.position.x] == 0:
            state.screen.render_unit(state.level.units[state.indicator.position.y][state.indicator.position.x])

        state.screen.render_unit(state.indicator)
    