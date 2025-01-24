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
paddle = pygame.transform.scale(paddle, (300, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(paddle, (100, 100))
    pygame.display.update()   

pygame.quit()