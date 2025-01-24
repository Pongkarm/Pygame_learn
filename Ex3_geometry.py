#การกำหนดสีจะกำหนดแบบ RGB เป็นรูปแบบ Tuple (0,0,0) (R,G,B)
#ชื่อตัวแปร = (R,G,B)
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

pygame.draw.line(screen, RED, (0, 0), (100, 120), 5)
pygame.draw.rect(screen, GREEN, (0, 50, 100, 130))
pygame.draw.circle(screen, WHITE, (200, 170), 126, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()   

pygame.quit()