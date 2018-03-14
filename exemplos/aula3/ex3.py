from curses import wrapper
import curses

def print_screen(screen):
    for i in range(82):
        screen.addstr(0, i, '=')
        screen.addstr(31, i, '=')

    for i in range(1,31):
        screen.addstr(i, 0, '|')
        screen.addstr(i, 81, '|')

    screen.addstr(32, 0, '(q)uit | (l)impar | (c)color')
    screen.addstr(33, 0, 'Use as setas para desenhar', curses.A_BLINK)

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
        
    # Clear screen
    stdscr.clear()
    stdscr.refresh()
    print_screen(stdscr)
    key = None
    x = 1
    y = 1
    color = 1
    while key != 'q':
        key = stdscr.getkey()
        if key == 'l':
            stdscr.clear()
            print_screen(stdscr)

        if key == 'c':
            color +=1

        if key == 'KEY_UP':
            x-=1
            if x < 1 :
                x = 1
            if x > 30:
                x = 30
        if key == 'KEY_DOWN':
            x+=1
            if x<1:
                x=1
            if x > 30:
                x = 30
        if key == 'KEY_LEFT':
            y-=1
            if y<1:
                y=1
            if y>80:
                y=80
        if key == 'KEY_RIGHT':
            y+=1
            if y<1:
                y=1
            if y>80:
                y=80

        stdscr.addstr(x, y, '\u220E', curses.color_pair(color))


wrapper(main)