from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.refresh()
    key = None
    while key != 'q':
        key = stdscr.getkey()
        stdscr.addstr(0, 0, key.encode('UTF-8'))


wrapper(main)