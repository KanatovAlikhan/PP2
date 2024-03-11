import pygame 

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Clock")
screen.fill((17, 54, 27))
done = True
while done:
        pygame.display.update()
        pygame.draw.circle(screen,(112, 2, 2),(100,100),70)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False
                        pygame.quit()
                elif event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                                screen.fill((14, 32, 48))