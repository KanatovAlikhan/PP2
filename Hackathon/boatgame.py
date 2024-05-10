import pygame
import random
background = pygame.image.load("images/background.png")
boat_image = pygame.image.load("images/boat.png")  
island_image = pygame.image.load("images/island.png") 
hh = pygame.image.load("images/man.png")
bridge_image = pygame.image.load("images/suret.png") 

def start3():
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BROWN = (139, 69, 19)

    WIDTH = 800
    HEIGHT = 550


    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Лодочная переправа")

    class Island(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = island_image
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)


    class Boat(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = boat_image
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH // 1.5-30, HEIGHT // 1.5)
            self.speed = 7

        def move(self, dx, dy):
            if 0 <= self.rect.x + dx <= WIDTH - self.rect.width:
                self.rect.x += dx
            if 0 <= self.rect.y + dy <= HEIGHT - self.rect.height:
                self.rect.y += dy

    class Person(pygame.sprite.Sprite):
        def __init__(self, island):
            super().__init__()
            self.image = hh
            self.rect = self.image.get_rect()
            self.island = island
            self.rect.center = self.island.rect.center

        def board(self, boat):
            if pygame.sprite.collide_rect(self, boat):
                self.rect.center = boat.rect.center

        def leave(self, island):
            self.island = island
            self.rect.center = self.island.rect.center
 

    class Bridge(pygame.sprite.Sprite):
        def __init__(self, island1, island2):
            super().__init__()
            self.image = bridge_image
            self.rect = self.image.get_rect()
            center_x1, center_y1 = island1.rect.center
            center_x2, center_y2 = island2.rect.center
        
            self.rect.centerx = (center_x1 + center_x2) // 2
            self.rect.centery = (center_y1 + center_y2) // 2
            self.direction = 1 

        def move(self):
            
            if self.rect.y <= 0:
                self.direction = 1 
            elif self.rect.y >= HEIGHT - self.rect.height:
                self.direction = -1 
            self.rect.y += self.direction * 1.8 

    island1 = Island(100, 200)
    island2 = Island(600, 400)

    boat = Boat()


    all_sprites = pygame.sprite.Group()
    all_sprites.add(island1, island2, boat)

 
    people = pygame.sprite.Group()


    bridges = pygame.sprite.Group()


   
    def create_people(island):
        num_people = random.randint(5, 10) 
        for _ in range(num_people):
            person = Person(island)
            people.add(person)
            all_sprites.add(person)  


 
    def create_bridges(island1, island2):
        num_bridges = random.randint(1, 3) 
        for _ in range(num_bridges):
            bridge = Bridge(island1, island2)
            bridges.add(bridge)
            all_sprites.add(bridge)

 
    create_people(island1)
    create_people(island2)


    create_bridges(island1, island2)

  
    font = pygame.font.Font(None, 36)
    text_color = WHITE


    start_time = pygame.time.get_ticks() 


    reached_island = False  

    current_time = 0

    start_time = pygame.time.get_ticks() 

    running = True
    while running:
       
        current_time = (pygame.time.get_ticks() - start_time) // 1000

        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.sprite.collide_rect(boat, island1):
                        for person in people:
                            if person.island == island1:
                                person.leave(island2)
                    elif pygame.sprite.collide_rect(boat, island2):
                        for person in people:
                            if person.island == island2:
                                person.leave(island1)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            boat.move(-boat.speed, 0)
        if keys[pygame.K_RIGHT]:
            boat.move(boat.speed, 0)
        if keys[pygame.K_UP]:
            boat.move(0, -boat.speed)
        if keys[pygame.K_DOWN]:
            boat.move(0, boat.speed)

        for bridge in bridges:
            bridge.move()

        if pygame.sprite.collide_rect(boat, island1):
            for person in people:
                if person.island == island1:
                    person.board(boat)
        if pygame.sprite.collide_rect(boat, island2):
            for person in people:
                if person.island == island2:
                    person.board(boat)

        for person in people:
            if pygame.sprite.collide_rect(boat, person):
                person.board(boat)

        if pygame.sprite.spritecollideany(boat, bridges):
            running = False 

        all_sprites.draw(screen)
        text_island1 = font.render(f"Island 1: {len([p for p in people if p.island == island1])}", True, text_color)
        text_island2 = font.render(f"Island 2: {len([p for p in people if p.island == island2])}", True, text_color)
        screen.blit(text_island1, (10, 10))
        screen.blit(text_island2, (WIDTH - 140, 10))
        text_time = font.render(f"Time: {current_time} sec", True, text_color)
        screen.blit(text_time, (10, 50))
        text_climate = font.render("Current climate in West Kazakhstan", True, text_color)
        text_climate_rect = text_climate.get_rect(center=(WIDTH // 2, 10))
        screen.blit(text_climate, text_climate_rect)
        pygame.display.flip()
    screen.fill(BLACK)
    text_game_finished = font.render("Game finished", True, WHITE)
    text_rect = text_game_finished.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_game_finished, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()

