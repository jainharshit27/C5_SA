import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

# Declare score with a value 0
score_font = pygame.----.----("freesansbold.ttf", 16)  # Replace the '--' to complete the line

dino_rect = pygame.Rect(100, 250, 64, 64)
cactus_rect = pygame.Rect(1100, 300, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

dino_y_change = 0

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino_y_change = -1
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    dino_y_change = 1
    
    dino_rect.y += dino_y_change
    if dino_rect.y > 250:
        dino_rect.y = 250
    if dino_rect.y < 100:
        dino_rect.y = 100
    
    cactus_rect.x = cactus_rect.x - 1
    if cactus_rect.x <= -30:
        cactus_rect.x = 1200
    
    score -- 1                         # Increment score by 1 by replacing '+=' and putting in correct operator.
    show_score = round(score/---)      # Replace '--' with a number to reduce the speed
    score_show = score_font.------("Score: " + str(show_score), True, (0, 0, 0))    # Replace the '--' to complete the line
    screen.----(----------, (10, 10))         # Replace the '--' to complete the line
    
    pygame.draw.rect(screen, (100, 100, 100), dino_rect)
    pygame.draw.rect(screen, (100, 100, 100), cactus_rect)
    pygame.draw.rect(screen, (100, 100, 100), ground_rect)
    
    if dino_rect.colliderect(cactus_rect):
        pygame.time.delay(2000)
        pygame.quit()
    
    pygame.display.update()
    
    
    
    
    
