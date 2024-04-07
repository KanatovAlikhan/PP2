import pygame,math
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
                elif event.key==pygame.K_s:
                    mode='square'
                elif event.key==pygame.K_t:
                    mode='right_triangle'
                elif event.key==pygame.K_k:
                    mode='equilateral triangle'
                elif event.key==pygame.K_j:
                    mode='rhombus'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mode in ['rectangle', 'circle','square','right_triangle','equilateral triangle','rhombus']:
                    rect_start = event.pos
                else:
                    if event.button == 1:
                        radius = min(200, radius + 1)
                    elif event.button == 3: 
                        radius = max(1, radius - 1)
            elif event.type == pygame.MOUSEBUTTONUP:
                if mode in ['rectangle', 'circle','square','right_triangle','equilateral triangle','rhombus'] and rect_start:
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
    elif mode== 'square':
        rect_width = abs(start[0] - end[0])
        pygame.draw.rect(screen,color,(min(start[0], end[0]), min(start[1], end[1]), rect_width, rect_width),width)
    elif mode =='right_triangle':
        third_point = (start[0], end[1])
        pygame.draw.polygon(screen,color,[start,end,third_point],width)
    elif mode == 'equilateral triangle':
        side_length = ((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5
        height = (side_length * (math.sqrt(3)/2))
        midpoint = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
        if start[1] <= end[1]:
            third_vertex = (midpoint[0], midpoint[1] - height)
        else: 
            third_vertex = (midpoint[0], midpoint[1] + height)
        pygame.draw.polygon(screen, color, [start, end, third_vertex], width)
    elif mode =='rhombus':
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        dist = math.sqrt(dx**2 + dy**2) / 2
        middle = ((start[0]+end[0])/2, (start[1]+end[1])/2)
        vertex1 = (middle[0], middle[1] - dist)
        vertex2 = (middle[0] + dist, middle[1])
        vertex3 = (middle[0], middle[1] + dist)
        vertex4 = (middle[0] - dist, middle[1])
        pygame.draw.polygon(screen, color, [vertex1, vertex2, vertex3, vertex4], width)
main()
