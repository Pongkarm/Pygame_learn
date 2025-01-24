import pygame
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

#รูปภาพ
paddle = pygame.image.load('image/Circle1.png')
paddle = pygame.transform.scale(paddle, (100, 100))
screen_rect = screen.get_rect()
print(screen_rect.center)
paddle_rect_x = screen_rect.centerx
paddle_rect_y = screen_rect.centery
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mose_x = event.pos[0]
            mose_y = event.pos[1]
            print(mose_x, mose_y)
            paddle_rect_x = mose_x
            paddle_rect_y = mose_y
    # screen.fill(WHITE)
    screen.blit(paddle, (paddle_rect_x- paddle.get_rect().centerx, paddle_rect_y-paddle.get_rect().centery))
    pygame.display.update()   

pygame.quit()