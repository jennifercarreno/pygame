import pygame
import random
pygame.init()
pygame.font.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 500])
lanes = [93, 218, 343]

class ScoreBoard(pygame.sprite.Sprite):
  def __init__(self, x, y, score):
    super(ScoreBoard, self).__init__()
    self.score = score
    self.font = pygame.font.SysFont('Comic Sans MS', 30)
    self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
    self.dx = 0
    self.dy = 0
    self.x = x
    self.y = y


  def update(self, points):
    self.score += points

  def move(self):
    self.x += self.dx
    self.y += self.dy

  def render(self, screen):
    self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
    screen.blit(self.surf, (self.x, self.y))

  def reset(self):
	  self.score = 0

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)    
    self.x = x
    self.y = y
    self.rect = self.surf.get_rect()

  def render(self, screen):
    self.rect.x = self.x
    self.rect.y = self.y
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
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = lanes[self.pos_x]
    self.y = lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y
  
  def update_dx_dy(self):
    self.dx = lanes[self.pos_x]
    self.dy = lanes[self.pos_y]

class Bomb(GameObject):
  def __init__(self):
    super(Bomb, self).__init__(0, 0, 'images/bomb.png')
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
    self.y = random.choice(lanes)


apple = Apple()
player = Player()
strawberry = Strawberry()
bomb = Bomb()
score = ScoreBoard(30, 30, 0)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
all_sprites.add(score)

fruit_sprites = pygame.sprite.Group()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

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

    for entity in all_sprites:
	    entity.move()
	    entity.render(screen)
    
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
      strawberry.dx += .5
      apple.dy += .5
      score.update(100)
      fruit.reset()
    
    if pygame.sprite.collide_rect(player, bomb):
      running = False

    pygame.display.flip()
    clock.tick(60)



