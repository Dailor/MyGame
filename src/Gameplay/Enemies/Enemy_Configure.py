from Utilities import load_image_v2
import pygame

pygame.init()
pygame.display.set_mode()

SIZE_ENEMY = 70, 70

Bee_stay = [load_image_v2(['Gameplay/Enemies/bee', 'bee-1.png'], SIZE_ENEMY),
            load_image_v2(['Gameplay/Enemies/bee', 'bee-2.png'], SIZE_ENEMY),
            load_image_v2(['Gameplay/Enemies/bee', 'bee-3.png'], SIZE_ENEMY),
            load_image_v2(['Gameplay/Enemies/bee', 'bee-4.png'], SIZE_ENEMY),
            load_image_v2(['Gameplay/Enemies/bee', 'bee-5.png'], SIZE_ENEMY),
            load_image_v2(['Gameplay/Enemies/bee', 'bee-6.png'], SIZE_ENEMY),
            load_image_v2(['Gameplay/Enemies/bee', 'bee-7.png'], SIZE_ENEMY),
            load_image_v2(['Gameplay/Enemies/bee', 'bee-8.png'], SIZE_ENEMY)]

Piranha_Plant = [load_image_v2(['Gameplay/Enemies/piranha-plant', 'piranha-plant-1.png'], SIZE_ENEMY),
                 load_image_v2(['Gameplay/Enemies/piranha-plant', 'piranha-plant-2.png'], SIZE_ENEMY),
                 load_image_v2(['Gameplay/Enemies/piranha-plant', 'piranha-plant-3.png'], SIZE_ENEMY),
                 load_image_v2(['Gameplay/Enemies/piranha-plant', 'piranha-plant-4.png'], SIZE_ENEMY)]

Piranha_Plant_Attack = [
    load_image_v2(['Gameplay/Enemies/piranha-plant-attack', 'piranha-plant-attack-1.png'], SIZE_ENEMY),
    load_image_v2(['Gameplay/Enemies/piranha-plant-attack', 'piranha-plant-attack-2.png'], SIZE_ENEMY),
    load_image_v2(['Gameplay/Enemies/piranha-plant-attack', 'piranha-plant-attack-3.png'], SIZE_ENEMY),
    load_image_v2(['Gameplay/Enemies/piranha-plant-attack', 'piranha-plant-attack-4.png'], SIZE_ENEMY)]

Slug_stay = [load_image_v2(['Gameplay/Enemies/slug', 'slug-1.png'], SIZE_ENEMY),
             load_image_v2(['Gameplay/Enemies/slug', 'slug-2.png'], SIZE_ENEMY),
             load_image_v2(['Gameplay/Enemies/slug', 'slug-3.png'], SIZE_ENEMY),
             load_image_v2(['Gameplay/Enemies/slug', 'slug-4.png'], SIZE_ENEMY)]
