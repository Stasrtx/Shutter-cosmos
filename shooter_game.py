from pygame import *
from random import randint
from time import sleep
win = 0
pr = 0
font.init()
text = font.Font(None, 30)
text2 = font.Font(None, 30)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x , y , size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image) , (size_x , size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image , (self.rect.x , self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 50:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 30, -50)
        bulets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global pr
        if self.rect.y == win_height:
            self.rect.y = 0
            self.rect.x = randint(50, 650)
            pr += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire = mixer.Sound('fire.ogg')
win_width = 700
win_height = 500
window = display.set_mode((win_width , win_height))
display.set_caption('Космос')
background = transform.scale(image.load('galaxy.jpg') , (win_width , win_height))
hero = Player('rocket.png' , 250, 450, 50, 50, 5)
enemy1 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
enemy2 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
enemy3 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
enemy4 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
enemy5 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
bulets = sprite.Group()
monsters = sprite.Group()
monsters.add(enemy1)
monsters.add(enemy2)
monsters.add(enemy3)
monsters.add(enemy4)
monsters.add(enemy5)
clock = time.Clock()
FPS = 60
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire.play()
                hero.fire()
    if not finish:
        if sprite.groupcollide(bulets, monsters, True, True):
            win += 1
            monsters.add(Enemy('ufo.png', randint(50, 650), 0, 50, 50, 5))
        if sprite.spritecollide(hero, monsters, True):
            monsters.add(Enemy('ufo.png', randint(50, 650), 0, 50, 50, 5))
            finish = True
        if pr >= 20:
            finish = True
        wintop = text.render('Счет:' + str(win) , True , (255, 255, 255))
        prtop = text2.render('Пропущено:' + str(pr) , True , (255, 255, 255))
        window.blit(background , (0 , 0))
        window.blit(wintop, (0, 0))
        window.blit(prtop, (0, 25))
        monsters.draw(window)
        monsters.update()
        hero.update()
        hero.draw()
        bulets.update()
        bulets.draw(window)
        display.update()
        clock.tick(FPS)
    else:
        finish = False
        pr = 0
        win = 0
        for b in bulets:
            b.kill()
        for b in monsters:
            b.kill()
        enemy1 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
        enemy2 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
        enemy3 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
        enemy4 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
        enemy5 = Enemy('ufo.png', randint(50, 650), 0, 50, 50, randint(1, 5))
        monsters.add(enemy1)
        monsters.add(enemy2)
        monsters.add(enemy3)
        monsters.add(enemy4)
        monsters.add(enemy5)
