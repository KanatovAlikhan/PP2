import pygame
import random
pygame.init()
W, H = 1200, 800
FPS = 60
speed_increase_interval = 10000
last_speed_increase = pygame.time.get_ticks()
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)
collision_sound = pygame.mixer.Sound('sounds/catch.mp3')
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]
bonus_block_index = random.randrange(len(block_list))
unbreakable_block_list = [pygame.Rect(10 + 120 * i, 120, 100, 50) for i in range(5)]
unbreakable_color = (100, 100, 100) 
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    else:
        dx = -dx
    return dx, dy
while not done:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(bg)
    for color, block in enumerate(block_list):
        if color == bonus_block_index:
            pygame.draw.rect(screen, (255, 215, 0), block)
        else:
            pygame.draw.rect(screen, color_list[color], block)
    for block in unbreakable_block_list:
        pygame.draw.rect(screen, unbreakable_color, block)
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    if current_time - last_speed_increase > speed_increase_interval:
        ballSpeed += 1
        paddleW = max(paddleW - 10, 50)
        paddle.x += 5 
        last_speed_increase = current_time
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy
    paddle.width = paddleW
    paddle.x = max(min(paddle.x, W - paddleW), 0)
    unbreakable_collision_index = ball.collidelist(unbreakable_block_list)
    if unbreakable_collision_index != -1:
        dx, dy = detect_collision(dx, dy, ball, unbreakable_block_list[unbreakable_collision_index])
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        if hitIndex == bonus_block_index:  
            paddleW += 50  
        hitRect = block_list.pop(hitIndex)
        color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
    if ball.collidelist(unbreakable_block_list) != -1:
        dx, dy = -dx, -dy
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
    pygame.display.flip()
    clock.tick(FPS)
