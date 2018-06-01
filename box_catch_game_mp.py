#This game is an uncompleted game so there are some bugs.("EARLY ACCESS ALPHA :d")
#Oyun tamamlanmış değildir o yüzden bazı buglar mevcut.
import pygame
x = pygame.init()
display_height = 800
display_width = 600

gameDisplay = pygame.display.set_mode((display_height,display_width))
pygame.display.set_caption("BOX CATCH")
white = (255, 255, 255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
lead_x = display_height/8
lead_y = display_width/6
lead_x0 = display_height/2
lead_y0= display_width/3*2
lead_x1 = 200
lead_y1 = 100
clock = pygame.time.Clock()
music = pygame.mixer.music.load("y.mp3")
pygame.mixer.music.play(1,6.0)
positioning = display_height/80
gameExit = False
font = pygame.font.SysFont(None,50)
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [250,300])
def red_won_ends(delay):
    txtt = "RED BOX WON"
    gameDisplay.fill(red)
    message_to_screen(txtt, blue)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)
    gameDisplay.fill(green)
    message_to_screen(txtt, red)
    pygame.time.delay(delay)
    pygame.display.update()
    gameDisplay.fill(blue)
    message_to_screen(txtt, green)
    pygame.time.delay(delay)
    pygame.display.update()
    gameDisplay.fill(red)
    message_to_screen(txtt, blue)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)
    gameDisplay.fill(green)
    message_to_screen(txtt, red)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)
    gameDisplay.fill(blue)
    message_to_screen(txtt, green)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)
def black_won_ends(delay):
    txtt = "BLACK BOX WON"
    gameDisplay.fill(red)
    message_to_screen(txtt, blue)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)
    gameDisplay.fill(green)
    message_to_screen(txtt, red)
    pygame.time.delay(delay)
    pygame.display.update()
    gameDisplay.fill(blue)
    message_to_screen(txtt, green)
    pygame.time.delay(delay)
    pygame.display.update()
    gameDisplay.fill(red)
    message_to_screen(txtt, blue)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)
    gameDisplay.fill(green)
    message_to_screen(txtt, red)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)
    gameDisplay.fill(blue)
    message_to_screen(txtt, green)
    pygame.time.delay(delay)
    pygame.display.update()
    pygame.time.delay(delay)


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                  lead_x -=10
            if event.key == pygame.K_RIGHT:
                  lead_x +=10
            if event.key == pygame.K_UP:
                 lead_y -=10
            if event.key == pygame.K_DOWN:
                lead_y +=10
            if event.key == pygame.K_a:
                 lead_x0 -=10
            if event.key == pygame.K_d:
                  lead_x0 +=10
            if event.key == pygame.K_w:
                 lead_y0 -=10
            if event.key == pygame.K_s:
                lead_y0 +=10
    gameDisplay.fill(white)
    redbox = gameDisplay.fill(red, rect = [lead_x,lead_y,30,30])
    blackbox=  gameDisplay.fill(black, rect=[lead_x0, lead_y0, 30, 30])
    pygame.display.update()
    '''
    if(lead_x0 == lead_x1 and lead_y0==lead_y1):
        x1g = random.randint(0,80)
        y1g = random.randint(0,60)
        randomx= x1g*10
        randomy = y1g*10
        xbox = gameDisplay.fill(green, rect=[randomx, randomy, 20, 20])
        pygame.display.update()
    if (lead_x == lead_x1 and lead_y == lead_y1):
        x1g = random.randint(0, 80)
        y1g = random.randint(0, 60)
        randomx = x1g * 10
        randomy = y1g * 10
        xbox = gameDisplay.fill(green, rect=[randomx, randomy, 20, 20])
        pygame.display.update()
    if (lead_x0 == randomx or lead_y0 == randomy):
            x1g = random.randint(0, 80)
            y1g = random.randint(0, 60)
            randomx = x1g * 10
            randomy = y1g * 10
            xbox = gameDisplay.fill(green, rect=[randomx, randomy, 20, 20])
            pygame.display.update()
    '''

    if (lead_x == lead_x0 and lead_y == lead_y0):
        red_won_ends(200)
        gameExit = True
    if (lead_x0 > display_height or lead_x > display_height or lead_y>display_width or lead_y0 > display_width):
        red_won_ends(200)
        gameExit = True
    if (lead_x0 < 0 or lead_x<0  or lead_y < 0 or lead_y0 <0):
        red_won_ends(200)
        gameExit = True
    if (lead_x >display_height or lead_y >display_width or lead_x <0 or lead_y<0)  :
        black_won_ends(200)
        gameExit = True

    clock.tick(30)


        #print(event)

pygame.quit()
quit()
