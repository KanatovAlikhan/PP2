import pygame, datetime
pygame.init()
screen = pygame.display.set_mode((1400,1050),pygame.RESIZABLE)
done=True
bg=pygame.image.load("images/mainclock.png")
r_hand=pygame.image.load("images/rightarm.png")
l_hand=pygame.image.load("images/leftarm.png")
while done:
        now = datetime.datetime.now()
        min_angle = now.minute *6
        sec_angle = now.second * 6 
        rot_r_hand=pygame.transform.rotate(r_hand,-min_angle)
        rot_l_hand=pygame.transform.rotate(l_hand,-sec_angle)
        screen.blit(bg,(0,0))
        screen.blit(rot_r_hand, rot_r_hand.get_rect(center=(700,525)))
        screen.blit(rot_l_hand, rot_l_hand.get_rect(center=(700,525)))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done=False
                        pygame.quit()
#Ex2
#space -> play music
#left -> previous music
#right -> next music
#up -> stop music and when 2nd time it continues
pygame.init()
delay_time = 1000
space_last_press_time = 0
left_last_press_time = 0
right_last_press_time = 0
space_button_pressed = False
left_button_pressed = False
right_button_pressed = False
music_playing = False
paused_time = 0

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
FPS = 5

musics = ['musics/one_piece1.mp3', 'musics/tokyo_ghoul.mp3', 'musics/one_piece2.mp3']
current_track = 0

pygame.mixer.init()

done = True

while done:
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not space_button_pressed:
        current_time = pygame.time.get_ticks()
        if current_time - space_last_press_time > delay_time:
            space_button_pressed = True
            space_last_press_time = current_time
            current_track = (current_track) % len(musics)
            pygame.mixer.music.load(musics[current_track])
            pygame.mixer.music.play()
            music_playing = True

    elif keys[pygame.K_RIGHT] and not right_button_pressed:
        current_time = pygame.time.get_ticks()
        if current_time - right_last_press_time > delay_time:
            right_button_pressed = True
            right_last_press_time = current_time
            current_track = (current_track + 1) % len(musics)
            pygame.mixer.music.load(musics[current_track])
            pygame.mixer.music.play()
            music_playing = True

    elif keys[pygame.K_LEFT] and not left_button_pressed:
        current_time = pygame.time.get_ticks()
        if current_time - left_last_press_time > delay_time:
            left_button_pressed = True
            left_last_press_time = current_time
            current_track = (current_track - 1) % len(musics)
            pygame.mixer.music.load(musics[current_track])
            pygame.mixer.music.play()
            music_playing = True
    if keys[pygame.K_UP]:
        if music_playing:
            pygame.mixer.music.pause()
            paused_time = pygame.mixer.music.get_pos()
            music_playing = False
        else:
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_pos(paused_time / 1000.0)
            music_playing = True
    if not keys[pygame.K_SPACE]:
        space_button_pressed = False
    if not keys[pygame.K_RIGHT]:
        right_button_pressed = False
    if not keys[pygame.K_LEFT]:
        left_button_pressed = False

    pygame.display.update()
    clock.tick(FPS)
#Ex3
pygame.init()
screen=pygame.display.set_mode((1000,500))
x=50
y=50
clock=pygame.time.Clock()
done=True
while done:
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(255,0,0),(x,y),25)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x>50:
                x-=20
        elif keys[pygame.K_RIGHT] and x<950:
                x+=20
        elif keys[pygame.K_UP] and y>50:
                y-=20
        elif keys[pygame.K_DOWN] and y<450:
                y+=20
        pygame.display.update()
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        pygame.quit()
        clock.tick(30)