import pygame, random


pygame.init()
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('DinoStorm')


FPS = 60
clock = pygame.time.Clock()

FLOOR_TILE = pygame.image.load('Dinostorm/resources/Tiles/Tile (2).png')

class Player(pygame.sprite.Sprite):
    DIRECTION = 'right'
    MOVEMENT_FRAME = 0
    MOVING_IMAGES = {
        'walk_right':[pygame.image.load(f'Dinostorm/resources/dino/walk_right/{x}.png') for x in range(1,11)],
        'walk_left': [pygame.image.load(f'Dinostorm/resources/dino/walk_left/{x}.png') for x in range(1, 11)],
        'idle_left': [pygame.image.load(f'Dinostorm/resources/dino/idle_left/{x}.png') for x in range(1,11)],
        'idle_right': [pygame.image.load(f'Dinostorm/resources/dino/idle_right/{x}.png') for x in range(1,11)]
    }

    def __init__(self):
        super().__init__()
        
        self.image = self.MOVING_IMAGES['idle_right'][0]
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = 700
        self.velocity = 5

    def update(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
            self.MOVEMENT_FRAME += 1
            self.DIRECTION = 'left'
            if self.MOVEMENT_FRAME == 10:
                self.MOVEMENT_FRAME = 0
            self.image = self.MOVING_IMAGES['walk_left'][self.MOVEMENT_FRAME]

        if keys[pygame.K_RIGHT] and self.rect.right <WINDOW_WIDTH:
            self.rect.x += self.velocity
            self.MOVEMENT_FRAME += 1
            if self.MOVEMENT_FRAME ==10:
                self.MOVEMENT_FRAME = 0
            self.image = self.MOVING_IMAGES['walk_right'][self.MOVEMENT_FRAME]
            self.DIRECTION = 'right'

    def reset(self):
        self.rect.centerx = WINDOW_WIDTH//2
        self.rect.bottom = 700


class Asteroid(pygame.sprite.Sprite):

    IMAGES = {
        'small': [pygame.image.load(f'Dinostorm/resources/asteroids/small/{x}.png') for x in range(1,16)],
        'medium': [pygame.image.load(f'Dinostorm/resources/asteroids/medium/{x}.png') for x in range(1,16)],
        'large': [pygame.image.load(f'Dinostorm/resources/asteroids/large/{x}.png') for x in range(1,16)]
    }

    def __init__(self, x, y, size):
        super().__init__()

        self.image = self.IMAGES[size][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.velocity = random.randint(1, 10)

    def update(self):
        self.rect.y += self.velocity

        if self.rect.bottom == 700:
            self.rect.bottom = 700

class Game():
    def __init__(self, player, asteroids):
        self.asteroids_dodged = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.asteroids = asteroids

        self.asteroid_sizes = ['small', 'medium', 'large']
        self.next_asteroid_size = random.choice(self.asteroid_sizes)
        


def draw_floor(floor_tile, positions):
    for x in positions:
        display_surface.blit(floor_tile, x)


my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    display_surface.fill((135 , 206, 235))
    draw_floor(FLOOR_TILE, [(0, 700), (128, 700), (256, 700), (384, 700), (512, 700), (640, 700), (768, 700), (896, 700), (1024, 700), (1152, 700)])

    my_player_group.update()
    my_player_group.draw(display_surface)

    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()