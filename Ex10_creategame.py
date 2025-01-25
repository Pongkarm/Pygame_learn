import pygame
import random

pygame.init()
pygame.display.set_caption("Game's Pongkarm")

#กำหนดขนดหน้าจอ จะใช้ตัวแปรพิมใหญ่ทั้งหมดสำหรับค่าคงที่ที่ไม่มีการเปลี่ยนแปลง
SCREEN_W = 1000
SCREEN_H = 800

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

#ตั้งค่าสี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 255)
RED = (255, 0, 0)
FPS = 30
SPEED = 20
BOLLSPEED = 20
score = 0

#รูปภาพ
boll = pygame.image.load('image/Circle3.png')
boll = pygame.transform.scale(boll, (70, 70))

paddle = pygame.image.load('image/paddle1.png')
paddle = pygame.transform.scale(paddle, (170, 50))

boll_rect = boll.get_rect()
boll_rect.center = (random.randint(0, SCREEN_W-100), 50)
paddle_rect = paddle.get_rect()
paddle_rect.center = (SCREEN_W//2, SCREEN_H -50)

#font 
sys_font = pygame.font.SysFont('adobehebrewitalicopentype', 50)
scorefont = sys_font.render(f'score : {str(score)}', False, BLACK)
score_rect = scorefont.get_rect()
score_rect.topleft = (10, 10)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)
    screen.blit(boll, boll_rect)
    screen.blit(paddle, paddle_rect)
    screen.blit(scorefont, score_rect)
    key = pygame.key.get_pressed()   
    
    #ถ้าโดน
    if paddle_rect.colliderect(boll_rect):
        boll_rect.y = 0
        boll_rect.x = random.randint(0, SCREEN_W-100)
        score += 1
        scorefont = sys_font.render(f'score : {str(score)}', False, BLACK)

        
        # running = False

    if key[pygame.K_LEFT] and paddle_rect.left > 0:
        # print('key left')
        paddle_rect.x -= SPEED
    if key[pygame.K_RIGHT] and paddle_rect.right < SCREEN_W:
        # print('key right')
        paddle_rect.x += SPEED
    if key[pygame.K_a] and paddle_rect.left > 0:
        # print('a')
        paddle_rect.x -= SPEED
    if key[pygame.K_d] and paddle_rect.right < SCREEN_W:
        # print('d')
        paddle_rect.x += SPEED
      
    #เคลีอนที่ลูกบอล
    if boll_rect.y < SCREEN_H:
        boll_rect.y += BOLLSPEED
    else:
        boll_rect.y = 0
        boll_rect.x = random.randint(0, SCREEN_W-100)
      
    #สร้าง hit block ของแต่ละรูป    
    # pygame.draw.rect(screen, RED, boll_rect,1)    
    # pygame.draw.rect(screen, RED, tree_rect,1)    
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()