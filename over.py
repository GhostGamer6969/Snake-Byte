import pygame

def disp():
    screen = pygame.display.set_mode((800, 800))
    screen.fill((255, 0, 0))
    pygame.display.update()
pygame.init()

# pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
if __name__ == '__main__':
    disp()