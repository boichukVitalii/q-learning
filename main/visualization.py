import pygame as p

WIDTH = HEIGHT = 600
DIMENSION = (5,3)
SQ_SIZE_HEIGHT = h = 120
SQ_SIZE_WIDTH = w = 200

def main(lst):
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    running = True
    dog_image = p.transform.scale(p.image.load("images/dogg.png"), (w-80,h-60))
    i = 0
    while running:
        drawEnv(screen)
        # keys = p.key.get_pressed()
        for event in p.event.get():
            if event.type == p.KEYDOWN:
                i = i + 1
            if i == len(lst):
                running = False
        screen.blit(dog_image, p.Rect(lst[i][1]*(SQ_SIZE_WIDTH+15), lst[i][0]*(SQ_SIZE_HEIGHT+15), SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
        p.display.flip()
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

def drawEnv(screen):
    number_font = p.font.SysFont(None, 48)
    border_width = 7
    p.draw.rect (screen, p.Color('green'), p.Rect(0*SQ_SIZE_WIDTH, 0*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_0 = number_font.render('0', True, p.Color('red'), p.Color('green'))
    screen.blit(number_0,( 0, 0 ))
    p.draw.rect (screen, p.Color('green'), p.Rect(1*SQ_SIZE_WIDTH, 0*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    p.draw.lines(screen, p.Color('black'), False, [(200,120), (400, 120)], border_width)
    p.draw.rect (screen, p.Color('green'), p.Rect(2*SQ_SIZE_WIDTH, 0*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    p.draw.lines(screen, p.Color('black'), False, [(400,120), (600, 120)], border_width)
    p.draw.rect (screen, p.Color('white'), p.Rect(0*SQ_SIZE_WIDTH, 1*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_1 = number_font.render('1', True, p.Color('red'), p.Color('white'))
    screen.blit(number_1,( 0, 120 ))
    p.draw.lines(screen, p.Color('black'), False, [(0,240), (200, 240)], border_width)
    p.draw.rect (screen, p.Color('gray'), p.Rect(1*SQ_SIZE_WIDTH, 1*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_2 = number_font.render('2', True, p.Color('red'), p.Color('grey'))
    screen.blit(number_2,( 200, 120 ))
    p.draw.lines(screen, p.Color('black'), False, [(200,240), (400, 240)], border_width)
    p.draw.rect (screen, p.Color('white'), p.Rect(2*SQ_SIZE_WIDTH, 1*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_3 = number_font.render('3', True, p.Color('red'), p.Color('white'))
    screen.blit(number_3,( 400, 120 ))
    p.draw.rect (screen, p.Color('gray'), p.Rect(0*SQ_SIZE_WIDTH, 2*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_4 = number_font.render('4', True, p.Color('red'), p.Color('gray'))
    screen.blit(number_4,( 0, 240 ))
    p.draw.rect (screen, p.Color('white'), p.Rect(1*SQ_SIZE_WIDTH, 2*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_5 = number_font.render('5', True, p.Color('red'), p.Color('white'))
    screen.blit(number_5,( 200, 240 ))
    p.draw.rect (screen, p.Color('gray'), p.Rect(2*SQ_SIZE_WIDTH, 2*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    p.draw.rect (screen, p.Color('white'), p.Rect(0*SQ_SIZE_WIDTH, 3*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_6 = number_font.render('6', True, p.Color('red'), p.Color('gray'))
    screen.blit(number_6,( 400, 240 ))
    p.draw.rect (screen, p.Color('gray'), p.Rect(1*SQ_SIZE_WIDTH, 3*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_7 = number_font.render('7', True, p.Color('red'), p.Color('white'))
    screen.blit(number_7,( 0, 360 ))
    p.draw.lines(screen, p.Color('black'), False, [(200,360), (400, 360)], border_width - 3)
    p.draw.rect (screen, p.Color('white'), p.Rect(2*SQ_SIZE_WIDTH, 3*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_8 = number_font.render('8', True, p.Color('red'), p.Color('grey'))
    screen.blit(number_8,( 200, 365 ))
    p.draw.rect (screen, p.Color('green'), p.Rect(0*SQ_SIZE_WIDTH, 4*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_9 = number_font.render('9', True, p.Color('red'), p.Color('white'))
    screen.blit(number_9,( 400, 360 ))
    p.draw.lines(screen, p.Color('black'), False, [(0,480), (200, 480)], border_width - 3)
    p.draw.rect (screen, p.Color('green'), p.Rect(1*SQ_SIZE_WIDTH, 4*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    p.draw.rect (screen, p.Color('green'), p.Rect(2*SQ_SIZE_WIDTH, 4*SQ_SIZE_HEIGHT, SQ_SIZE_WIDTH, SQ_SIZE_HEIGHT))
    number_0 = number_font.render('0', True, p.Color('red'), p.Color('green'))
    screen.blit(number_0,( 300, 520 ))
    p.draw.lines(screen, p.Color('black'), False, [(400,480), (600, 480)], border_width - 3)

if __name__ == "__main__":
    main()
