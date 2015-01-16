"""
Console Manager: handles the creation and rendering of all consoles.
"""

import tdl
from tdl import Console


class ConsoleManager:

    def __init__(self):
        self.main_console_w = 80
        self.main_console_h = 60
        self.consoles = dict()

        tdl.setFont('terminal8x8_gs_ro.png')  # Configure the font.

        # Create the root console.
        self.main_console = tdl.init(self.main_console_w, self.main_console_h, 'Roguelike Game')

    def render_console(self, console, pos_x, pos_y):
        self.main_console.blit(console, pos_x, pos_y)

    def create_new_console(self, name, width, height, mode='scroll'):
        console = tdl.Console(width, height)
        console.setMode(mode)

        self.consoles[name] = console

    def render_main_menu(self):
        options = ['Play a new game', 'Quit']

        main_menu = Menu('Main Menu', options, self.main_console_w, self.main_console_h)
        self.render_console(main_menu, 0, 0)

        if len(options) > main_menu.max_options_len:
            raise ValueError('Cannot have a menu with more than 26 options.')

        x = 20
        y = 20

        main_menu.print_str('Welcome', x, y)
        y += 2
        main_menu.print_str('Your goal is to find the Cone of Dunshire (!).', x, y)
        y += 2
        main_menu.print_str('Use Caution as there are Trolls (T)and Orcs (o)', x, y)
        y += 1
        main_menu.print_str('lurking in this dungeon!', x, y)
        y += 2

        x += 5
        for option_text in options:
            text = '(' + chr(main_menu.letter_index) + ') ' + option_text
            main_menu.print_str(text, x, y)
            y += 2
            main_menu.letter_index += 1
        self.render_console(main_menu, 0, 0)
        tdl.flush()


class Menu(Console):

    def __init__(self, name, options, width, height):
        Console.__init__(self, width, height)
        self.name = name
        self.max_options_len = 26
        self.options = options
        self.letter_index = ord('a')

    def print_str(self, text, pos_x, pos_y):
        self.move(pos_x, pos_y)
        self.printStr(text)
