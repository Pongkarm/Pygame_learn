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
FPS = 30

#รูปภาพ
paddle = pygame.image.load('image/Circle1.png')
paddle = pygame.transform.scale(paddle, (100, 100))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
print(screen_rect.center)
paddle_rect_x = screen_rect.centerx
paddle_rect_y = screen_rect.centery
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(paddle, (paddle_rect_x, paddle_rect_y))
    key = pygame.key.get_pressed()
    pygame.display.update()   
    if key[pygame.K_UP]:
        print('key up')
        paddle_rect_y -= 2
    if key[pygame.K_DOWN]:
        paddle_rect_y += 2
        print('key down')
    if key[pygame.K_LEFT]:
        print('key left')
        paddle_rect_x -= 2
    if key[pygame.K_RIGHT]:
        print('key right')
        paddle_rect_x += 2
    if key[pygame.K_w]:
        print('w')
        paddle_rect_y -= 2
    if key[pygame.K_a]:
        print('a')
        paddle_rect_x -= 2
    if key[pygame.K_s]:
        print('s')
        paddle_rect_y += 2
    if key[pygame.K_d]:
        print('d')
        paddle_rect_x += 2
    screen.fill(BLACK)
    clock.tick(FPS)
pygame.quit()