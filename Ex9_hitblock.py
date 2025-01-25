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
SPEED = 10

#รูปภาพ
boll = pygame.image.load('image/Circle2.png')
boll = pygame.transform.scale(boll, (200, 200))

tree = pygame.image.load('image/tree1.png')
tree = pygame.transform.scale(tree, (50, 50))

boll_rect = boll.get_rect()
boll_rect.center = (SCREEN_W//2, SCREEN_H//2)
tree_rect = tree.get_rect()
tree_rect.center = (SCREEN_W//2, (SCREEN_H//2) -200)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)
    screen.blit(boll, boll_rect)
    screen.blit(tree, tree_rect)
    key = pygame.key.get_pressed()   
    
    #ถ้าโดน
    if tree_rect.colliderect(boll_rect):
        print('hit')
        tree_rect.x = random.randint(0, SCREEN_W-20)
        tree_rect.y = random.randint(0, SCREEN_H-20)
        # running = False
    if key[pygame.K_UP]:
        # print('key up')
        boll_rect.y -= SPEED
    if key[pygame.K_DOWN]:
        boll_rect.y += SPEED
        # print('key down')
    if key[pygame.K_LEFT]:
        # print('key left')
        boll_rect.x -= SPEED
    if key[pygame.K_RIGHT]:
        # print('key right')
        boll_rect.x += SPEED
    if key[pygame.K_w]:
        # print('w')
        boll_rect.y -= SPEED
    if key[pygame.K_a]:
        # print('a')
        boll_rect.x -= SPEED
    if key[pygame.K_s]:
        # print('s')
        boll_rect.y += SPEED
    if key[pygame.K_d]:
        # print('d')
        boll_rect.x += SPEED
    #สร้าง hit block ของแต่ละรูป    
    pygame.draw.rect(screen, RED, boll_rect,1)    
    pygame.draw.rect(screen, RED, tree_rect,1)    
        
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()