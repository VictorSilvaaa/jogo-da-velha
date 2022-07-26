import pygame

#button class
class Button():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

  def draw(self, surface):
    #draw button on screen
    surface.blit(self.image, (self.rect.x, self.rect.y))

  def clicked(self):
    click = False
    pos = pygame.mouse.get_pos()
    
    #check mouseover and clicked conditions
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1:
        click = True
    return click
  