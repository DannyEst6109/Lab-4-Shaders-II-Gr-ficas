import pygame
from pygame.locals import *
from gl import Renderer, Model
import shaders


width = 960
height = 540

deltaTime = 0.0

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

face = Model('model.obj', 'model.bmp')
face.position.z = -5

rend.scene.append( face )


isRunning = True
while isRunning:


    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        rend.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        rend.camPosition.z -= 1 * deltaTime
    if keys[K_s]:
        rend.camPosition.z += 1 * deltaTime
    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime

    if keys[K_LEFT]:
        if rend.valor > 0:
            rend.valor -= 0.1 * deltaTime

    if keys[K_RIGHT]:
        if rend.valor < 0.2:
            rend.valor += 0.1 * deltaTime

    # Rotacion de camara
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()

    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

pygame.quit()

