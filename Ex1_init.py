print('Pygame')
import pygame

pygame.init()
pygame.display.set_caption("Game's Pongkarm")

#กำหนดขนดหน้าจอ จะใช้ตัวแปรพิมใหญ่ทั้งหมดสำหรับค่าคงที่ที่ไม่มีการเปลี่ยนแปลง
SCREEN_W = 1000
SCREEN_H = 800

Screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
pygame.quit()