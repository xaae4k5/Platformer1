from pygame import*
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Платформер')

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Platform(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.x_start = x

    def update(self):
        self.rect.x = self.x_start+x_pos

class Player(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.opora = False

    def update(self):
        global x_pos
        keys = key.get_pressed()
        if self.rect.x < x_start or self.rect.x>x_max-x_start:
            if keys[K_LEFT] and self.rect.x>10:
                self.rect.x-=self.speed
            if keys[K_RIGHT] and self.rect.x<700 -10- self.rect.width:
                self.rect.x += self.speed
        else:
            if keys[K_LEFT]:
                x_pos += self.speed
            if keys[K_RIGHT]:
                x_pos -= self.speed

        if keys[K_SPACE] and self.opora:
            self.rect.y += -150

    
    def gravity(self):
        self.opora = False
        sprite_list = sprite.spritecollide(player, platforms, False)
        if len(sprite_list)!=0:
            self.opora = True
        if not self.opora:
            self.rect.y+=3

class Enemy(GameSprite):
    def __init__(self, img, x, y, w, h, speed, fly=0):
        super().__init__(img, x, y, w, h, speed)
        self.fly = fly

    def start(self, z1, z2):
        self.z1 = z1
        self.z2 = z2

    def update(self):
        if self.fly == 1:
            if self.rect.y <= min(self.z1, self.z2):
                self.direct = 1
            elif self.rect.y >= max(self.z1, self.z2):
                self.direct = -1
            self.rect.y += self.speed*self.direct
        else:
            if self.rect.x <= min(self.z1, self.z2):
                self.direct = 1
            elif self.rect.x >= max(self.z1, self.z2):
                self.direct = -1
            self.rect.x += self.speed*self.direct



x_start = 350-60/2
x_pos = 0 
x_max = 1400

#задай фон сцены
background = transform.scale(image.load('fon.jpg'), (700,500))

platforms = sprite.Group()
pl_count = 5
for i in range(pl_count):
    x = randint(5, x_max-105)
    y = randint(200, 300)
    plt = Platform('plat.png', x, y, 100, 50, 0)
    platforms.add(plt)
plt = Platform('plat.png', 0, 380, 740, 100, 0)
platforms.add(plt)

player = Player('hero (1).jpg', 10, 100, 60, 80, 5)
enemyes = sprite.Group()
enemy1 = Enemy('vrag (1).jpg', 200,200, 50,50, 3)
enemy1.start(200, 300)
enemyes.add(enemy1)
enemy2 = Enemy('vrag (1).jpg', 400,200, 50,50, 3, 1)
enemy2.start(200, 300)
enemyes.add(enemy2)

game = True
clock = time.Clock()
fps = 60




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))
    platforms.update()
    platforms.draw(window)
    player.reset()
    player.update()
    player.gravity()
    enemyes.update()
    enemyes.draw(window)


    clock.tick(fps)
    display.update()