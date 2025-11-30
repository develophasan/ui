#!/usr/bin/env python3
import curses
from curses import panel

def create_window(h, w, y, x, title=""):
    win = curses.newwin(h, w, y, x)
    win.box()

    if title:
        win.addstr(0, 2, f" {title} ")

    return win

def draw(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(False)

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # === ÜST MENÜ ÇUBUĞU ===
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(0, 0, " " * w)
        stdscr.addstr(0, 2, "AIOS  |  File  Edit  System  Help")
        stdscr.attroff(curses.color_pair(1))

        # === SOL BAŞLAT MENÜSÜ ===
        start_menu = create_window(h - 3, 20, 1, 0, "Start")
        start_menu.addstr(2, 2, "- File Manager")
        start_menu.addstr(3, 2, "- Terminal")
        start_menu.addstr(4, 2, "- Settings")
        start_menu.addstr(5, 2, "- About")
        start_menu.refresh()

        # === ORTA MASAÜSTÜ PENCERESİ ===
        desk_w = w - 22
        desk_h = h - 5
        desktop = create_window(desk_h, desk_w, 1, 21, "Home")
        desktop.addstr(2, 2, "AIOS Masaüstüne hoş geldiniz.")
        desktop.addstr(3, 2, "Bu pencereye ikonlar, dosyalar, uygulama pencereleri eklenebilir.")
        desktop.refresh()

        # === ALT GÖREV ÇUBUĞU ===
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(h - 2, 0, " " * w)
        stdscr.addstr(h - 2, 2, "[Start]  Terminal  FileManager  Settings")
        stdscr.addstr(h - 1, 2, f"AIOS Desktop Running  |  {w}x{h}")
        stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("q"):
            break

def main():
    curses.wrapper(init)

def init(stdscr):
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)   # üst menü
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # alt bar

    draw(stdscr)

if __name__ == "__main__":
    main()
