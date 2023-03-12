import os
import random
import pygame
pygame.init()

sw = 650
sh = 800
bg = pygame.image.load('mtnbg.png')
platform = pygame.image.load('iceplat.png')
kiblast = pygame.image.load('Kamehameha.png')
heart = pygame.image.load('Heart.png')
kiSound = pygame.mixer.Sound('kisound.wav')
hitSound = pygame.mixer.Sound('woah.wav')
sensuSound = pygame.mixer.Sound('sensuEating.wav')
lostSound = pygame.mixer.Sound('youreKidding.wav')
music = pygame.mixer.music.load('dbzSong.mp3')
pygame.mixer.music.play(-1)

win = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Game")
goku_images = [pygame.image.load(os.path.join("gokus", "goku1.png")),
                 pygame.image.load(os.path.join("gokus", "goku2.png")),
                 pygame.image.load(os.path.join("gokus", "goku3.png")),
                 pygame.image.load(os.path.join("gokus", "goku4.png")),
                 pygame.image.load(os.path.join("gokus", "goku5.png")),
                 pygame.image.load(os.path.join("gokus", "goku6.png"))]

food_images = [[pygame.image.load(os.path.join("food", "senzubox.png")), pygame.image.load(os.path.join("food", "senzu.png"))]]

clock = pygame.time.Clock()

class Ground(object):
    def __init__(self):
        self.w = sw
        self.h = platform.get_height()
        self.y = sh - self.h + 50

    def draw(self, win):
        win.blit(platform, (0, self.y))

class Player(object):
    animTime = 5 #Speed of animation
    imgs = goku_images
    firing = False
    def __init__(self):
        self.x = sw//2 - goku_images[0].get_width()
        self.y = ground.y - goku_images[0].get_height() + 30
        self.w = goku_images[0].get_width()
        self.h = goku_images[0].get_height()
        self.img = self.imgs[0]
        self.imageCount = 0
        self.one = False

    def draw(self, win):

        if self.firing:
            self.imageCount += 1
            b = Blast(self.x + self.w // 2 - kiblast.get_width() // 2, self.y - kiblast.get_height(),
                      kiblast.get_width(), kiblast.get_height())
            if self.imageCount < self.animTime:
                self.img = self.imgs[0]
            elif self.imageCount < self.animTime * 2:
                self.img = self.imgs[1]
            elif self.imageCount < self.animTime * 3:
                self.img = self.imgs[2]
            elif self.imageCount < self.animTime * 4:
                self.img = self.imgs[3]
                if self.one == False:
                    b.img = pygame.transform.scale(b.img, (int(b.img.get_width()), int(b.img.get_height()*.2)))
                    b.y = self.y-b.img.get_height()
                    b.h = b.img.get_height()
                    blasts.append(b)

            elif self.imageCount < self.animTime * 5:
                self.img = self.imgs[3]
                if self.one == False:
                    b.img = pygame.transform.scale(b.img, (int(b.img.get_width()), int(b.img.get_height() * .4)))
                    b.y = self.y - b.img.get_height()
                    b.h = b.img.get_height()
                    blasts.clear()
                    blasts.append(b)

            elif self.imageCount < self.animTime * 6:
                self.img = self.imgs[3]
                if self.one == False:
                    b.img = pygame.transform.scale(b.img, (int(b.img.get_width()), int(b.img.get_height() * .6)))
                    b.y = self.y - b.img.get_height()
                    b.h = b.img.get_height()
                    blasts.clear()
                    blasts.append(b)
            elif self.imageCount < self.animTime * 7:
                self.img = self.imgs[3]
                if self.one == False:
                    b.img = pygame.transform.scale(b.img, (int(b.img.get_width()), int(b.img.get_height() * .8)))
                    b.y = self.y - b.img.get_height()
                    b.h = b.img.get_height()
                    blasts.clear()
                    blasts.append(b)
            elif self.imageCount < self.animTime * 8:
                self.img = self.imgs[3]
                if self.one == False:
                    b.img = pygame.transform.scale(b.img, (int(b.img.get_width()), int(b.img.get_height() * 1)))
                    b.y = self.y - b.img.get_height()
                    b.h = b.img.get_height()
                    blasts.clear()
                    blasts.append(b)
            elif self.imageCount < self.animTime * 9:
                self.img = self.imgs[2]
                self.one = False
            elif self.imageCount < self.animTime * 10:
                self.img = self.imgs[1]
            else:
                self.imageCount = 0
                self.firing = False
        else:
            self.imageCount = 0
            self.img = self.imgs[0]

        win.blit(self.img, (self.x, self.y))




class Blast(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = kiblast.get_width()
        self.h = kiblast.get_height()
        self.img = kiblast

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        # pygame.draw.rect(win, self.color, [self.x, self.y, self.w, self.h])


class Food(object):
    def __init__(self):
        self.w = 65
        self.h = 65
        self.food = random.choice(food_images)
        self.img = self.food[0]
        self.x = random.randrange(0,sw-self.w)
        self.y = -100
        self.yv = random.randrange(3,6)
        self.isHit = False
        self.isEaten = False

    def draw(self, win):
        if self.isHit == False:
            self.img = self.food[0]
        else:
            self.img = self.food[1]
        win.blit(self.img, (self.x, self.y))



def redrawGameWindow():
    win.blit(bg, (0, 0))
    ground.draw(win)
    goku.draw(win)
    font = pygame.font.SysFont('comicsans', 50)
    fontA = pygame.font.SysFont('arial', 70)
    for b in blasts:
        b.draw(win)

    for f in foods:
        f.draw(win)

    for i in range(lives):
        win.blit(heart, (30 + 62*i, 30))

    scoreText = font.render("Score: " + str(score), 1, (0, 100, 180))
    highScoreText = font.render("High Score: " + str(highScore), 1, (0, 100, 180))
    win.blit(scoreText, (sw - (scoreText.get_width()) - 20, 30))
    if highScore != 0:
        win.blit(highScoreText, (sw - (highScoreText.get_width()) - 20, 70))
    if gameOver:
        goText = fontA.render("Game Over" , 1, (0, 100, 180))
        win.blit(goText, (sw//2-goText.get_width()//2, sh//2-goText.get_height()//2))
        paText = font.render("Press Space to Play Again!", 1, (0, 100, 180))
        win.blit(paText, (sw // 2 - paText.get_width() // 2, sh // 2 - paText.get_height() // 2 + 50))
    # pong.draw(win)

    pygame.display.update()

ground = Ground()
goku = Player()
blasts = []
foods = []

def set_new_highscore(score):
    if score > get_highscore():
        with open("highscore.txt", 'w') as f:
            f.write(str(score))

def get_highscore():
    with open("highscore.txt", "r") as f:
        return int(f.readline())

def init():
    global ground
    ground = Ground()

count = 0
missedFoods = 0
score = 0
lives = 3
gameOver = False
run = True
highScore = get_highscore()
while run:
    clock.tick(80)
    if gameOver == False:
        count += 1
        if (pygame.mouse.get_pos()[0] - goku.w // 2) < 0:
            goku.x = 0
        elif (pygame.mouse.get_pos()[0] + goku.w // 2) > sw:
            goku.x = sw - goku.w
        else:
            goku.x = pygame.mouse.get_pos()[0] - goku.w // 2


        if ground.y  > sh - ground.h + 50:
            ground.y = sh - ground.h + 50
            goku.y = ground.y - goku_images[0].get_height() + 30

        # new food
        if count <= 1000:
            if count % 60 == 0:
                foods.append(Food())
        elif count <= 2000:
            if count % 45 == 0:
                foods.append(Food())
        else:
            if count % 30 == 0:
                foods.append(Food())

        # score inc
        if count % 10 == 0:
            score += 1
            ground.y -= 1
            goku.y -= 1


        for f in foods:
            f.y += f.yv
            if f.y > sh:
                missedFoods += 1
                ground.y -= 20
                goku.y -= 20
                foods.pop(foods.index(f))

        for f in foods:
            for b in blasts:
                if b.y <= f.y + f.h and b.y + b.h >= f.y:
                    if (f.x + f.w >= b.x and f.x + f.w < b.x + b.w) or (f.x >= b.x and f.x <= b.x + b.w):
                        f.isHit = True
                        f.w = 45
                        f.h = 45
                        f.img = f.food[1]
                        f.yv = 7

        for f in foods:
            if f.isHit:
                if f.y >= ground.y - f.h//2:
                    f.vy = 0
                    f.y = ground.y - f.h//2
            if goku.y + goku.h >= f.y + f.h and goku.y + 15 <= f.y + f.h:
                if (f.x >= goku.x and f.x <= goku.x + goku.w) or (f.x + f.w <= goku.x + goku.w and f.x + f.w >= goku.x):
                    if f.isHit:
                        foods.pop(foods.index(f))
                        score += 100
                        ground.y += 5
                        goku.y += 5
                        sensuSound.play(maxtime=1000)
                    else:
                        lives -= 1
                        if lives != 0:
                            hitSound.play()
                        foods.pop(foods.index(f))

        # show blasts
        for b in blasts:
            b.y -= 5

        for b in blasts:
            if b.y + b.h < -50:
                blasts.pop(blasts.index(b))

        if lives == 0 or goku.y <= 0:
            gameOver = True
            lostSound.play()
    else:
        if highScore < score:
            highScore = score
            set_new_highscore(score)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            gameOver = False
            lives = 3
            ground.y = sh - ground.h + 50
            goku.y = ground.y - goku_images[0].get_height() + 30
            score = 0
            count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            goku.firing = True
            kiSound.play()
    redrawGameWindow()
pygame.quit()
