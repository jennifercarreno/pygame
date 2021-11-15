import pygame
import random
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])
lanes = [93, 218, 343]

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)    
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'images/apple.png')
    self.dx = 0
    self.dy = (random.randint(0, 200) / 100) + 1
    self.reset() 

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.y > 500: 
      self.reset()
  
  def reset(self):
    self.x = random.choice(lanes)
    self.y = -64

class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'images/strawberry.png')
    self.dx = (random.randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset() 

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500: 
      self.reset()
  
  def reset(self):
    self.x = -64
    self.y = random.choice(lanes)

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'images/player.png')
    self.dx = 0
    self.dy = 0
    self.reset()

  def left(self):
    self.dx -= 100

  def right(self):
    self.dx += 100

  def up(self):
    self.dy -= 100

  def down(self):
    self.dy += 100


  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32

apple = Apple()
player = Player()
strawberry = Strawberry()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            running = False
          elif event.key == pygame.K_LEFT:
            player.left()
          elif event.key == pygame.K_RIGHT:
            player.right()
          elif event.key == pygame.K_UP:
            player.up()
          elif event.key == pygame.K_DOWN:
            player.down()

    screen.fill((255, 255, 255))

    apple.move()
    apple.render(screen)

    player.move()
    player.render(screen)

    strawberry.move()
    strawberry.render(screen)

    pygame.display.flip()
    clock.tick(60)



