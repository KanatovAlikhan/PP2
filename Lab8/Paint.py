import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    draw_color = (0, 0, 255)
    bg_color = (0, 0, 0)
    mode = 'draw'
    radius = 15
    points = []
    rect_start = None   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    draw_color = (255, 0, 0) 
                elif event.key == pygame.K_g:
                    draw_color = (0, 255, 0) 
                elif event.key == pygame.K_b:
                    draw_color = (0, 0, 255)
                elif event.key == pygame.K_e:
                    mode = 'erase'
                elif event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_q:
                    mode = 'rectangle'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mode in ['rectangle', 'circle']:
                    rect_start = event.pos
                else:
                    if event.button == 1:
                        radius = min(200, radius + 1)
                    elif event.button == 3: 
                        radius = max(1, radius - 1)
            elif event.type == pygame.MOUSEBUTTONUP:
                if mode in ['rectangle', 'circle'] and rect_start:
                    handle_shape_drawing(screen, rect_start, event.pos, mode, draw_color, radius)
                    rect_start = None
            elif event.type == pygame.MOUSEMOTION and mode in ['draw', 'erase']:
                if pygame.mouse.get_pressed()[0]:
                    color = bg_color if mode == 'erase' else draw_color
                    pygame.draw.circle(screen, color, event.pos, radius)
        pygame.display.flip()
        clock.tick(60)
def handle_shape_drawing(screen, start, end, mode, color, width):
    if mode == 'rectangle':
        rect_width = abs(start[0] - end[0])
        rect_height = abs(start[1] - end[1])
        pygame.draw.rect(screen, color, (min(start[0], end[0]), min(start[1], end[1]), rect_width, rect_height), width)
    elif mode == 'circle':
        center = start
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, center, radius, width)
main()
