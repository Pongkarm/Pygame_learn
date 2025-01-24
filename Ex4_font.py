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

# fonts = pygame.font.get_fonts()
# for font in fonts:
#     print(font)
sys_font = pygame.font.SysFont('adobehebrewitalicopentype', 20)
message = sys_font.render("Hello World", True, GREEN)
message2 = sys_font.render("Hello World", False, RED)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(message, (0,40))
    screen.blit(message2, (0,100))
    pygame.display.update()   

pygame.quit()


# ravie
# adobehebrewitalicopentype
# adobehebrewregularopentype
# adobemingstdlightopentype
# adobemyungjostdmediumopentype
# adobesongstdlightopentype
# kozgopr6nboldopentype
# kozgopr6nextralightopentype
# kozgopr6nheavyopentype
# kozgopr6nlightopentype
# kozgopr6nmediumopentype
# kozgopr6nregularopentype
# kozminpr6nboldopentype
# kozminpr6nextralightopentype
# kozminpr6nheavyopentype
# kozminpr6nlightopentype
# kozminpr6nmediumopentype
# kozminpr6nregularopentype
# lettergothicstdboldopentype
# lettergothicstdboldslantedopentype
# lettergothicstdslantedopentype
# lettergothicstdopentype
# minionproboldopentype
# minionprobolditopentype
# minionproitopentype
# minionproregularopentype
# myriadhebrewopentype
# myriadproboldopentype
# myriadproboldcondopentype
# myriadproboldconditopentype
# myriadprobolditopentype
# myriadprocondopentype
# myriadproconditopentype
# myriadproitopentype
# myriadproregularopentype
# myriadprosemiboldopentype
# myriadprosemibolditopentype
# simsunextg
# codicon
# elusiveiconswebfont
# fontawesome47webfont
# fontawesome5brandswebfont
# fontawesome5regularwebfont
# fontawesome5solidwebfont
# materialdesignicons5webfont
# materialdesignicons6webfont
# phosphor
# remixicon