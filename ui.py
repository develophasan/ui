#!/usr/bin/env python3
import curses

def draw(stdscr):
    curses.curs_set(0)     # İmleci gizle
    stdscr.nodelay(False)  # Kullanıcı tuş basana kadar bekle

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # Başlık
        title = "AIOS Minimal UI  |  Çıkış: q"
        stdscr.addstr(0, max(0, (w - len(title)) // 2), title)

        # Üst çizgi
        for x in range(w - 1):
            stdscr.addch(1, x, "-")

        # Orta içerik
        stdscr.addstr(3, 2, "Bu AIOS için temel bir terminal arayüzüdür.")
        stdscr.addstr(4, 2, "Buraya sol panel, sağ panel, log panel eklenebilir.")
        stdscr.addstr(6, 2, "[q] → Çıkış yap")

        # Alt bilgi
        stdscr.addstr(h - 2, 2, f"Ekran boyutu: {w}x{h}")
        stdscr.addstr(h - 1, 2, "AIOS terminal arayüzü çalışıyor...")

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break

def main():
    curses.wrapper(draw)

if __name__ == "__main__":
    main()
