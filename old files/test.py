import pygame

class Control:
   def __init__(self):
      self.screensize = (800,600)
      self.screen = pygame.display.set_mode(self.screensize)
      self.clock = pygame.time.Clock()
      self.gamestate = True
      self.set_menu()
   
      self.mainloop()
      
   def set_menu(self):
      menu_width = self.screensize[0] // 4
      table_size = self.screensize[0] - menu_width
      
      menu_top = 0
      menu_height = self.screensize[1]
      self.menu = pygame.Rect(table_size, menu_top, menu_width, menu_height)
      self.menu_bg = (50,50,50)
      
      scrollbar_width = 10
      self.menu_scroll_bar_bg = pygame.Rect(self.screensize[0] - scrollbar_width, menu_top, scrollbar_width, self.screensize[1])
      
      top = 20
      height = 20
      self.menu_scroll_bar = pygame.Rect(self.screensize[0] - scrollbar_width, top, scrollbar_width, height)
      
   def mainloop(self):
      while self.gamestate:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               self.gamestate = False
         
         self.update()
         pygame.display.flip()
         
   def update(self):
      self.screen.fill((100,100,100))
      pygame.draw.rect(self.screen, self.menu_bg, self.menu, 0)
      pygame.draw.rect(self.screen, (200,200,200), self.menu_scroll_bar_bg, 0)
      pygame.draw.rect(self.screen, (0,0,0), self.menu_scroll_bar, 0)
      

app = Control()