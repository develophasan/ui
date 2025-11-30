#!/usr/bin/env python3
import curses
import time
import os

def draw_ui(stdscr):
    curses.curs_set(0)  # imleci gizle
    stdscr.nodelay(False)

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        # Bölümler yüksekliği
        top_bar_h = 3
        bottom_h = 4
        right_w = 24

        # Üst bar çizimi
        stdscr.addstr(0, 2, " 🌑  AIOS — HasanOS Terminal Arayüzü ")
        stdscr.addstr(0, max_x - 15, "[ q : çıkış ]")

        # Ana gövde hesaplaması
        main_y = top_bar_h
        main_h = max_y - top_bar_h - bottom_h
        main_w = max_x - right_w

        # Sol panel genişliği
        left_w = int(main_w * 0.28)
        code_x = left_w + 1
        code_w = main_w - left_w - 1

        # Sol panel çerçeve
        for y in range(main_y, main_y + main_h):
            stdscr.addch(y, 0, "|")
            stdscr.addch(y, left_w, "|")
        for x in range(0, left_w + 1):
            stdscr.addch(main_y - 1, x, "-")
            stdscr.addch(main_y + main_h, x, "-")
        stdscr.addstr(main_y - 1, 2, " Dosyalar ")

        # Sol panel içerik (gerçek dosya listesi)
        file_list = os.listdir(".")
        for i, f in enumerate(file_list[:main_h - 2]):
            stdscr.addstr(main_y + 1 + i, 2, f[:left_w - 3])

        # Kod paneli çerçevesi
        for y in range(main_y, main_y + main_h):
            stdscr.addch(y, code_x - 1, "|")
        for x in range(code_x - 1, main_w):
            stdscr.addch(main_y - 1, x, "-")
            stdscr.addch(main_y + main_h, x, "-")
        stdscr.addstr(main_y - 1, code_x + 2, " Kod Alanı ")

        # Kod alanı dummy içerik
        sample_code = [
            "def hello_world():",
            "    print('AIOS çalışıyor...')",
            "",
            "# Yakında:",
            "#  - Asistan paneli",
            "#  - Terminal girdi kontrolü",
            "#  - AI entegrasyonu",
        ]
        for i, line in enumerate(sample_code):
            if main_y + 1 + i < main_y + main_h:
                stdscr.addstr(main_y + 1 + i, code_x + 1, line[:code_w - 2])

        # Sağ panel
        right_x = main_w + 1
        for y in range(main_y, main_y + main_h):
            stdscr.addch(y, right_x - 1, "|")
            stdscr.addch(y, max_x - 1, "|")
        for x in range(right_x - 1, max_x):
            stdscr.addch(main_y - 1, x, "-")
            stdscr.addch(main_y + main_h, x, "-")

        stdscr.addstr(main_y - 1, right_x + 2, " Sistem ")

        stdscr.addstr(main_y + 1, right_x + 2, f"CPU Kullanım: 0%")
        stdscr.addstr(main_y + 2, right_x + 2, f"RAM: {round(os.sysconf('SC_PAGE_SIZE')*os.sysconf('SC_PHYS_PAGES')/1024/1024/1024,2)} GB")
        stdscr.addstr(main_y + 4, right_x + 2, "AIOS v0.1")
        stdscr.addstr(main_y + 5, right_x + 2, "Terminal UI hazır")

        # Alt Log paneli
        term_y = max_y - bottom_h
        for x in range(0, max_x):
            stdscr.addch(term_y - 1, x, "-")
            stdscr.addch(max_y - 1, x, "-")
        stdscr.addstr(term_y - 1, 2, " Log / Terminal ")

        stdscr.addstr(term_y + 0, 2, "Sistem hazır...")
        stdscr.addstr(term_y + 1, 2, "AIOS başlatıldı.")
        stdscr.addstr(term_y + 2, 2, "Bekleniyor...")

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord('q'):
            break

def main():
    curses.wrapper(draw_ui)

if __name__ == "__main__":
    main()
