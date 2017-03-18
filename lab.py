# Hi. I'm Rodrigo Nascimento.
# I created everything in this game from scratch by myself and own it's rights.
# Feel free to copy, modify and distribute it as long as you don't charge
# for it.
# I've worked on this game for three months after I started learning Python,
# my first commercial programming language. Because of # that, you may find
# lots of ways to improve this code.
# I'd like to say a huge thank you to sentdex and KidsCanCode, two YouTube
# channels who helped me a lot with their tutorials on python and pygame.
# I love video games ever since I was a kid and this was the first one I made.
# While certainly not the best video game ever, it's from the heart.
# Thank you for trying it out. Hope you enjoy it.
#
# Rodrigo Nascimento
#
# Version 2.0
# Built with Python 3.5.2 and Pygame 1.9.1.

import pygame
import sys
import random
import pandas as pd
import numpy as np
from os import path
pygame.init()
pygame.mixer.init()


FPS = 60
WIDTH = 1920
HEIGHT = 1080
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The color that fell from the sky')
clock = pygame.time.Clock()

BLACK = (38, 50, 56)
WHITE = (236, 239, 241)
BLUE = (41, 182, 246)
ORANGE = (255, 112, 67)
YELLOW = (255, 238, 88)
GREEN = (156, 204, 101)

# Paths
if getattr(sys, 'frozen', False):
    # Frozen
    CurrentPath = sys._MEIPASS
else:
    # Running in normal Python environment
    CurrentPath = path.dirname(__file__)

spriteFolderPath = path.join(CurrentPath, 'sprites')
music_dir = path.join(CurrentPath, 'music')

# Load graphics
# Title, game over and story screens
title_screen = pygame.image.load(path.join(spriteFolderPath, 'title_screen.png')).convert_alpha()
go_01 = pygame.image.load(path.join(spriteFolderPath, 'go_01.png')).convert_alpha()
go_02 = pygame.image.load(path.join(spriteFolderPath, 'go_02.png')).convert_alpha()
go_03 = pygame.image.load(path.join(spriteFolderPath, 'go_03.png')).convert_alpha()
pause_screen = pygame.image.load(path.join(spriteFolderPath, 'pause_screen.png')).convert_alpha()
controls_image = pygame.image.load(path.join(spriteFolderPath, 'controls_screen.png')).convert_alpha()
credits_screen = pygame.image.load(path.join(spriteFolderPath, 'credits_screen.png')).convert_alpha()
story = []
story.append(pygame.image.load(path.join(spriteFolderPath, 'story 1.png')).convert_alpha())
story.append(pygame.image.load(path.join(spriteFolderPath, 'story 2.png')).convert_alpha())
story.append(pygame.image.load(path.join(spriteFolderPath, 'story 3.png')).convert_alpha())
story.append(pygame.image.load(path.join(spriteFolderPath, 'story 4.png')).convert_alpha())
story.append(pygame.image.load(path.join(spriteFolderPath, 'story 5.png')).convert_alpha())
# Player 1
player1_sprites = [[], [], [], [], [], [], [], []]
player1_sprites[0].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_000.png')).convert_alpha())  # 0º
player1_sprites[0].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_000.png')).convert_alpha())
player1_sprites[0].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_000.png')).convert_alpha())
player1_sprites[0].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_000.png')).convert_alpha())
player1_sprites[0].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_000.png')).convert_alpha())
player1_sprites[1].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_090.png')).convert_alpha())  # 90º
player1_sprites[1].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_090.png')).convert_alpha())
player1_sprites[1].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_090.png')).convert_alpha())
player1_sprites[1].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_090.png')).convert_alpha())
player1_sprites[1].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_090.png')).convert_alpha())
player1_sprites[2].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_180.png')).convert_alpha())  # 180º
player1_sprites[2].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_180.png')).convert_alpha())
player1_sprites[2].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_180.png')).convert_alpha())
player1_sprites[2].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_180.png')).convert_alpha())
player1_sprites[2].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_180.png')).convert_alpha())
player1_sprites[3].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_270.png')).convert_alpha())  # 270º
player1_sprites[3].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_270.png')).convert_alpha())
player1_sprites[3].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_270.png')).convert_alpha())
player1_sprites[3].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_270.png')).convert_alpha())
player1_sprites[3].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_270.png')).convert_alpha())
player1_sprites[4].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_045.png')).convert_alpha())  # 45º
player1_sprites[4].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_045.png')).convert_alpha())
player1_sprites[4].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_045.png')).convert_alpha())
player1_sprites[4].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_045.png')).convert_alpha())
player1_sprites[4].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_045.png')).convert_alpha())
player1_sprites[5].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_135.png')).convert_alpha())  # 135º
player1_sprites[5].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_135.png')).convert_alpha())
player1_sprites[5].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_135.png')).convert_alpha())
player1_sprites[5].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_135.png')).convert_alpha())
player1_sprites[5].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_135.png')).convert_alpha())
player1_sprites[6].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_225.png')).convert_alpha())  # 225º
player1_sprites[6].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_225.png')).convert_alpha())
player1_sprites[6].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_225.png')).convert_alpha())
player1_sprites[6].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_225.png')).convert_alpha())
player1_sprites[6].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_225.png')).convert_alpha())
player1_sprites[7].append(pygame.image.load(path.join(spriteFolderPath, 'p_1_315.png')).convert_alpha())  # 315º
player1_sprites[7].append(pygame.image.load(path.join(spriteFolderPath, 'p_2_315.png')).convert_alpha())
player1_sprites[7].append(pygame.image.load(path.join(spriteFolderPath, 'p_3_315.png')).convert_alpha())
player1_sprites[7].append(pygame.image.load(path.join(spriteFolderPath, 'p_4_315.png')).convert_alpha())
player1_sprites[7].append(pygame.image.load(path.join(spriteFolderPath, 'p_5_315.png')).convert_alpha())
# Bullet
bullet_sprite = pygame.image.load(path.join(spriteFolderPath, 'bullet.png')).convert_alpha()
# Debris
debris_blue = pygame.image.load(path.join(spriteFolderPath, 'debris_blue.png')).convert_alpha()
debris_green = pygame.image.load(path.join(spriteFolderPath, 'debris_green.png')).convert_alpha()
debris_yellow = pygame.image.load(path.join(spriteFolderPath, 'debris_yellow.png')).convert_alpha()
debris_orange = pygame.image.load(path.join(spriteFolderPath, 'debris_orange.png')).convert_alpha()
# Stars
star_10 = pygame.image.load(path.join(spriteFolderPath, 'star_10.png')).convert_alpha()
star_05 = pygame.image.load(path.join(spriteFolderPath, 'star_05.png')).convert_alpha()
# Tea
tea_sprite = pygame.image.load(path.join(spriteFolderPath, 'tea.png')).convert_alpha()
# Crown
crown_sprite = pygame.image.load(path.join(spriteFolderPath, 'crown.png')).convert_alpha()
# Umbrella
umbrella_sprite = pygame.image.load(path.join(spriteFolderPath, 'umbrella.png')).convert_alpha()
# Shield
shield_sprite = []
shield_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'shield 1.png')).convert_alpha())
shield_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'shield 2.png')).convert_alpha())
shield_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'shield 3.png')).convert_alpha())
shield_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'shield 4.png')).convert_alpha())
shield_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'shield 5.png')).convert_alpha())
shield_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'shield 6.png')).convert_alpha())
shield_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'shield 7.png')).convert_alpha())
# Tardis
tardis_sprite = pygame.image.load(path.join(spriteFolderPath, 'tardis.png')).convert_alpha()
# Talk bubbles
bubble_sprite = []
bubble_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'bubble_1.png')).convert_alpha())
bubble_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'bubble_2.png')).convert_alpha())
bubble_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'bubble_3.png')).convert_alpha())
bubble_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'bubble_4.png')).convert_alpha())
bubble_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'bubble_5.png')).convert_alpha())
# Planet
planet_sprite = []
planet_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'planet_01.png')).convert_alpha())
planet_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'planet_02.png')).convert_alpha())
planet_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'planet_03.png')).convert_alpha())
planet_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'planet_04.png')).convert_alpha())
planet_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'planet_05.png')).convert_alpha())
planet_sprite.append(pygame.image.load(path.join(spriteFolderPath, 'planet_06.png')).convert_alpha())
# Enemies
ringo_sprite = pygame.image.load(path.join(spriteFolderPath, 'ringo.png')).convert_alpha()
george_sprite = pygame.image.load(path.join(spriteFolderPath, 'george.png')).convert_alpha()
john_sprite = pygame.image.load(path.join(spriteFolderPath, 'john.png')).convert_alpha()
paul_sprite = pygame.image.load(path.join(spriteFolderPath, 'paul.png')).convert_alpha()
# Icon
pygame.display.set_icon(player1_sprites[0][4])

# Audio
# FX
shot_sound = pygame.mixer.Sound(path.join(music_dir, 'shot.wav'))
shield_sound = pygame.mixer.Sound(path.join(music_dir, 'shield.wav'))
crown_sound = pygame.mixer.Sound(path.join(music_dir, 'crown.wav'))
tea_sound = pygame.mixer.Sound(path.join(music_dir, 'tea.wav'))
planet_recovery_sound = pygame.mixer.Sound(path.join(music_dir, 'planet recovery.wav'))
player_explosion_sound = pygame.mixer.Sound(path.join(music_dir, 'player_explosion.wav'))
ringo_explosion_sound = pygame.mixer.Sound(path.join(music_dir, 'ringo_explosion.wav'))
george_explosion_sound = pygame.mixer.Sound(path.join(music_dir, 'george_explosion.wav'))
john_explosion_sound = pygame.mixer.Sound(path.join(music_dir, 'john_explosion.wav'))
paul_explosion_sound = pygame.mixer.Sound(path.join(music_dir, 'paul_explosion.wav'))
planet_explosion_sound = pygame.mixer.Sound(path.join(music_dir, 'planet_explosion.wav'))
# Music
start_screen_music = pygame.mixer.Sound(path.join(music_dir, 'start screen.wav'))
main_theme = pygame.mixer.Sound(path.join(music_dir, 'main theme.wav'))
game_over_sound = pygame.mixer.Sound(path.join(music_dir, 'game over.wav'))

# Cursors default positions
music_cursor = 9
fx_cursor = 7


def reset_scores(reset=False):
    if reset:
        data = {'Player': ['rod', 'nya', 'chl', 'jck', 'thr'],
                'Points': [2000, 1500, 1000, 800, 600]}
        scores = pd.DataFrame(data, columns=['Player', 'Points'])
        scores.index += 1
        scores.to_csv('high scores.csv', index=False)


def show_message(message, alignment, size, coordinate_1, coordinate_2, color=WHITE, font='Heavitas.ttf'):
    if hasattr(sys, '_MEIPASS'):  # the same logic used to set the image directory
        font = path.join(sys._MEIPASS, font)  # specially useful to make a singlefile .exe
    font = pygame.font.Font(font, size)
    text_surface = font.render(message, False, color)
    text_rect = text_surface.get_rect()
    if alignment == 'left':
        text_rect.x = coordinate_1
        text_rect.y = coordinate_2
    elif alignment == 'center':
        text_rect.centerx = coordinate_1
        text_rect.y = coordinate_2
    elif alignment == 'right':
        text_rect.right = coordinate_1
        text_rect.y = coordinate_2
    game_display.blit(text_surface, text_rect)


# One function to rule all fades
def fade(color, alpha):
    block = pygame.Surface((1920, 1080))
    block.fill(color)
    block.set_alpha(alpha)
    game_display.blit(block, (0, 0))


def draw_cursor(topcenterx, centery, width, thickness=8):
    # centery should be the height of the text minus 28
    pygame.draw.lines(game_display, BLUE, False, [(topcenterx + width / 2, centery), (topcenterx - width / 2, centery)], thickness)
    centery -= thickness
    pygame.draw.lines(game_display, GREEN, False, [(topcenterx + width / 2, centery), (topcenterx - width / 2, centery)], thickness)
    centery -= thickness
    pygame.draw.lines(game_display, YELLOW, False, [(topcenterx + width / 2, centery), (topcenterx - width / 2, centery)], thickness)
    centery -= thickness
    pygame.draw.lines(game_display, ORANGE, False, [(topcenterx + width / 2, centery), (topcenterx - width / 2, centery)], thickness)


def sound_volume(volume=1.0):
    global shot_sound, shield_sound, crown_sound, tea_sound
    global planet_recovery_sound, player_explosion_sound, ringo_explosion_sound
    global george_explosion_sound, john_explosion_sound, paul_explosion_sound
    global planet_explosion_sound
    shot_sound.set_volume(volume)
    shield_sound.set_volume(volume)
    crown_sound.set_volume(volume)
    tea_sound.set_volume(volume)
    planet_recovery_sound.set_volume(volume)
    player_explosion_sound.set_volume(volume)
    ringo_explosion_sound.set_volume(volume)
    george_explosion_sound.set_volume(volume)
    john_explosion_sound.set_volume(volume)
    paul_explosion_sound.set_volume(volume)
    planet_explosion_sound.set_volume(volume)


def music_volume(volume=1.0):
    global game_over_sound, main_theme, start_screen_music
    game_over_sound.set_volume(volume)
    main_theme.set_volume(volume)
    start_screen_music.set_volume(volume)


def start_screen():
    global stars
    counter = cursor_position = 0
    in_alpha = 255
    start = story = scores = settings = False
    reset_scores()
    reset()
    start_screen_music.play(-1)
    while True:
        counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cursor_position -= 1
                    if cursor_position < 0:
                        cursor_position = 3
                elif event.key == pygame.K_DOWN:
                    cursor_position += 1
                    if cursor_position > 3:
                        cursor_position = 0
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and cursor_position == 0:
                    start = True
                    out_alpha = 0
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and cursor_position == 1:
                    story = True
                    out_alpha = 0
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and cursor_position == 2:
                    settings = True
                    out_alpha = 0
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and cursor_position == 3:
                    pygame.quit()
                    sys.exit()

        game_display.fill(BLACK)
        stars.draw(game_display)
        stars.update()
        game_display.blit(title_screen, (0, 0))

        show_message('START', 'center', 45, WIDTH - 250, HEIGHT - 360, color=WHITE)
        show_message('STORY', 'center', 45, WIDTH - 250, HEIGHT - 290, color=WHITE)
        show_message('SETTINGS', 'center', 45, WIDTH - 250, HEIGHT - 220, color=WHITE)
        show_message('EXIT', 'center', 45, WIDTH - 250, HEIGHT - 150, color=WHITE)
        if cursor_position == 0:
            draw_cursor(WIDTH - 250, HEIGHT - 332, 180)
            show_message('START', 'center', 45, WIDTH - 250, HEIGHT - 360, color=BLACK)
        elif cursor_position == 1:
            draw_cursor(WIDTH - 250, HEIGHT - 262, 190)
            show_message('STORY', 'center', 45, WIDTH - 250, HEIGHT - 290, color=BLACK)
        elif cursor_position == 2:
            draw_cursor(WIDTH - 250, HEIGHT - 192, 270)
            show_message('SETTINGS', 'center', 45, WIDTH - 250, HEIGHT - 220, color=BLACK)
        elif cursor_position == 3:
            draw_cursor(WIDTH - 250, HEIGHT - 122, 140)
            show_message('EXIT', 'center', 45, WIDTH - 250, HEIGHT - 150, color=BLACK)
        # menu text

        # fade in
        if in_alpha > 0:
            in_alpha -= 8
            fade(WHITE, in_alpha)
        # fade out in case the player has pressed start
        if start:
            if out_alpha < 255:
                out_alpha += 45
                fade(BLACK, out_alpha)
            else:
                main()
                start = False
        elif story:
            if out_alpha < 255:
                out_alpha += 85
                fade(BLACK, out_alpha)
            else:
                story_screen()
                story = False
        elif settings:
            if out_alpha < 255:
                out_alpha += 85
                fade(BLACK, out_alpha)
            else:
                settings_screen()
                settings = False
        pygame.display.flip()


def story_screen():
    global stars
    counter = current_screen = out_alpha = 0
    in_alpha = 255
    show_story = True
    while show_story:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    show_story = False
                elif event.key == pygame.K_RIGHT:
                    current_screen += 1
                elif event.key == pygame.K_LEFT:
                    current_screen -= 1
        # set a specific delay for each screen
        if current_screen == 0:
            delay = 100
        elif current_screen == 1:
            delay = 300
        elif current_screen == 2:
            delay = 500
        elif current_screen == 3:
            delay = 400
        elif current_screen == 4:
            delay = 600
        # change screen
        counter += 1
        if counter >= delay:
            counter = 0
            current_screen += 1
            in_alpha = 255
            out_alpha = 0
        if current_screen >= 5:
            show_story = False
        else:
            game_display.fill(BLACK)
            stars.draw(game_display)
            stars.update()
            game_display.blit(story[current_screen], (0, 0))
        # Fade in
        if in_alpha > 0:
            in_alpha -= 25
            fade(BLACK, in_alpha)
        # fade out
        if out_alpha < 255:
            out_alpha += 10
            fade(BLACK, in_alpha)
        pygame.display.flip()


def pause(paused=True):
    counter = out_alpha = cursor_position = 0
    pygame.mixer.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    cursor_position += 1
                    if cursor_position >= 5:
                        cursor_position = 0
                if event.key == pygame.K_UP:
                    cursor_position -= 1
                    if cursor_position < 0:
                        cursor_position = 4
                if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    if cursor_position == 0:
                        paused = False
                    elif cursor_position == 1:
                        main()
                    elif cursor_position == 2:
                        settings_screen(True)
                    elif cursor_position == 3:
                        start_screen()
                    elif cursor_position == 4:
                        pygame.quit()
                        sys.exit()
        counter += 1
        game_display.blit(pause_screen, (0, 0))
        # menu
        # cursor
        if cursor_position == 0:
            draw_cursor(WIDTH / 2, HEIGHT - 382, 280)
        if cursor_position == 1:
            draw_cursor(WIDTH / 2, HEIGHT - 312, 240)
        elif cursor_position == 2:
            draw_cursor(WIDTH / 2, HEIGHT - 242, 270)
        elif cursor_position == 3:
            draw_cursor(WIDTH / 2, HEIGHT - 172, 320)
        elif cursor_position == 4:
            draw_cursor(WIDTH / 2, HEIGHT - 102, 140)
        # menu text
        show_message('CONTINUE', 'center', 45, WIDTH / 2, HEIGHT - 410, color=BLACK)
        show_message('RESTART', 'center', 45, WIDTH / 2, HEIGHT - 340, color=BLACK)
        show_message('SETTINGS', 'center', 45, WIDTH / 2, HEIGHT - 270, color=BLACK)
        show_message('MAIN MENU', 'center', 45, WIDTH / 2, HEIGHT - 200, color=BLACK)
        show_message('EXIT', 'center', 45, WIDTH / 2, HEIGHT - 130, color=BLACK)
        # handles fade out:
        if not paused:
            while out_alpha < 255:
                fade(BLACK, out_alpha)
                out_alpha += 25
                pygame.display.flip()
        pygame.display.flip()
    pygame.mixer.unpause()


def game_over(go=True):
    global timer
    go_choice = random.choice([go_01, go_02, go_03])
    out_alpha = cursor_position = 0
    in_alpha = 255
    high_scores(True)
    pygame.mixer.stop()
    game_over_sound.play()
    while go or out_alpha < 255:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    if cursor_position == 0:
                        main()
                    elif cursor_position == 1:
                        start_screen()
                    elif cursor_position == 2:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_UP:
                    cursor_position -= 1
                    if cursor_position < 0:
                        cursor_position = 2
                elif event.key == pygame.K_DOWN:
                    cursor_position += 1
                    if cursor_position > 2:
                        cursor_position = 0
        game_display.blit(go_choice, (0, 0))
        show_message('SCORE: ' + str(timer), 'center', 60, WIDTH / 2, 100, color=BLACK)
        # menu
        # cursor
        if cursor_position == 0:
            draw_cursor(WIDTH / 2, HEIGHT - 222, 240)
        elif cursor_position == 1:
            draw_cursor(WIDTH / 2, HEIGHT - 152, 320)
        elif cursor_position == 2:
            draw_cursor(WIDTH / 2, HEIGHT - 82, 140)
        # menu text
        show_message('RESTART', 'center', 45, WIDTH / 2, HEIGHT - 250, color=BLACK)
        show_message('MAIN MENU', 'center', 45, WIDTH / 2, HEIGHT - 180, color=BLACK)
        show_message('EXIT', 'center', 45, WIDTH / 2, HEIGHT - 110, color=BLACK)
        # Fade in:
        if in_alpha > 0:
            in_alpha -= 25
            fade(WHITE, in_alpha)
        # This fades out the the screen after the player has pressed start:
        if not go:
            out_alpha += 25
            fade(BLACK, out_alpha)
        pygame.display.flip()


def settings_screen(paused=False):
    global difficulty, fx_cursor, music_cursor
    out_alpha = left_cursor_position = 0
    in_alpha = 255
    settings = True
    pygame.key.set_repeat(150, 150)
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    if left_cursor_position == 3:
                        high_scores()
                    elif left_cursor_position == 4:
                        controls_screen()
                    elif left_cursor_position == 5:
                        credits()
                    elif left_cursor_position == 6:
                        settings = False
                # move left cursor
                elif event.key == pygame.K_UP:
                    left_cursor_position -= 1
                    if left_cursor_position < 0:
                        left_cursor_position = 6
                elif event.key == pygame.K_DOWN:
                    left_cursor_position += 1
                    if left_cursor_position > 6:
                        left_cursor_position = 0
                # move right cursor
                elif event.key == pygame.K_RIGHT:
                    if left_cursor_position == 0 and not paused:
                        if difficulty == 'easy':
                            difficulty = 'normal'
                        elif difficulty == 'normal':
                            difficulty = 'hard'
                        else:
                            difficulty = 'easy'
                    elif left_cursor_position == 1:
                        if music_cursor < 9:
                            music_cursor += 1
                    elif left_cursor_position == 2:
                        if fx_cursor < 9:
                            fx_cursor += 1
                elif event.key == pygame.K_LEFT:
                    if left_cursor_position == 0 and not paused:
                        if difficulty == 'hard':
                            difficulty = 'normal'
                        elif difficulty == 'normal':
                            difficulty = 'easy'
                        else:
                            difficulty = 'hard'
                    elif left_cursor_position == 1:
                        if music_cursor > 0:
                            music_cursor -= 1
                    elif left_cursor_position == 2:
                        if fx_cursor > 0:
                            fx_cursor -= 1
        game_display.fill(WHITE)
        # menu
        # left cursor
        if left_cursor_position == 0:
            draw_cursor(450, 253, 570, 15)
        elif left_cursor_position == 1:
            draw_cursor(450, 353, 660, 15)
        elif left_cursor_position == 2:
            draw_cursor(450, 453, 830, 15)
        elif left_cursor_position == 3:
            draw_cursor(450, 553, 680, 15)
        elif left_cursor_position == 4:
            draw_cursor(450, 653, 530, 15)
        elif left_cursor_position == 5:
            draw_cursor(450, 753, 420, 15)
        elif left_cursor_position == 6:
            if not paused:
                draw_cursor(450, 853, 600, 15)
            else:
                draw_cursor(450, 853, 315, 15)
        # difficulty cursor
        if difficulty == 'easy':
            draw_cursor(1070, 237, 220)
        elif difficulty == 'normal':
            draw_cursor(1355, 237, 235)
        elif difficulty == 'hard':
            draw_cursor(1700, 237, 320)
        # music level cursor
        if music_cursor == 1:
            draw_cursor(1010, 353, 100, 15)
        elif music_cursor == 2:
            draw_cursor(1060, 353, 200, 15)
        elif music_cursor == 3:
            draw_cursor(1110, 353, 300, 15)
        elif music_cursor == 4:
            draw_cursor(1160, 353, 400, 15)
        elif music_cursor == 5:
            draw_cursor(1210, 353, 500, 15)
        elif music_cursor == 6:
            draw_cursor(1260, 353, 600, 15)
        elif music_cursor == 7:
            draw_cursor(1310, 353, 700, 15)
        elif music_cursor == 8:
            draw_cursor(1360, 353, 800, 15)
        elif music_cursor == 9:
            draw_cursor(1410, 353, 900, 15)
        music_volume(float('0.' + str(music_cursor)))
        # effects level cursor
        if fx_cursor == 1:
            draw_cursor(1010, 453, 100, 15)
        elif fx_cursor == 2:
            draw_cursor(1060, 453, 200, 15)
        elif fx_cursor == 3:
            draw_cursor(1110, 453, 300, 15)
        elif fx_cursor == 4:
            draw_cursor(1160, 453, 400, 15)
        elif fx_cursor == 5:
            draw_cursor(1210, 453, 500, 15)
        elif fx_cursor == 6:
            draw_cursor(1260, 453, 600, 15)
        elif fx_cursor == 7:
            draw_cursor(1310, 453, 700, 15)
        elif fx_cursor == 8:
            draw_cursor(1360, 453, 800, 15)
        elif fx_cursor == 9:
            draw_cursor(1410, 453, 900, 15)
        sound_volume(float('0.' + str(fx_cursor)))
        # left menu text
        show_message('DIFFICULTY', 'center', 80, 450, 200, color=BLACK)
        show_message('MUSIC LEVEL', 'center', 80, 450, 300, color=BLACK)
        show_message('SOUND FX LEVEL', 'center', 80, 450, 400, color=BLACK)
        show_message('HIGH SCORES', 'center', 80, 450, 500, color=BLACK)
        show_message('CONTROLS', 'center', 80, 450, 600, color=BLACK)
        show_message('CREDITS', 'center', 80, 450, 700, color=BLACK)
        if not paused:
            show_message('MAIN MENU', 'center', 80, 450, 800, color=BLACK)
        else:
            show_message('BACK', 'center', 80, 450, 800, color=BLACK)
        # right menu text
        show_message('RUBBISH', 'center', 45, 1070, 200, color=BLACK, font='Roboto-Light.ttf')
        show_message('AVERAGE', 'center', 45, 1355, 200, color=BLACK, font='Roboto-Light.ttf')
        show_message('BLOODY HELL', 'center', 45, 1700, 200, color=BLACK, font='Roboto-Light.ttf')
        # Fade in:
        if in_alpha > 0:
            in_alpha -= 25
            fade(WHITE, in_alpha)
        pygame.display.flip()


def controls_screen():
    in_alpha = 255
    controls = True
    while controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                controls = False
        game_display.fill(BLACK)
        game_display.blit(controls_image, (0, 0))
        draw_cursor(WIDTH / 2, 978, 176)
        show_message('BACK', 'center', 45, WIDTH / 2, 950, color=BLACK)
        if in_alpha > 0:
            in_alpha -= 25
            fade(BLACK, in_alpha)
        pygame.display.flip()


def credits():
    in_alpha = 255
    credits = True
    while credits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                credits = False
        game_display.fill(WHITE)
        game_display.blit(credits_screen, (0, 0))
        draw_cursor(WIDTH / 2, 978, 176)
        show_message('BACK', 'center', 45, WIDTH / 2, 950, color=BLACK)
        if in_alpha > 0:
            in_alpha -= 25
            fade(BLACK, in_alpha)
        pygame.display.flip()


def high_scores(new_entry=False):
    global timer
    if hasattr(sys, '_MEIPASS'):  # In case you make a single file exe
        scores = pd.read_csv(path.join(sys._MEIPASS, 'high scores.csv'))
    else:
        scores = pd.read_csv('high scores.csv')
    scores.index += 1
    in_alpha = 255
    show_scores = True
    if not new_entry:
        while show_scores:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    show_scores = False
            game_display.fill(WHITE)
            y = 300
            for row in range(1, 6):
                show_message(str(row), 'center', 70, 560, y, color=BLACK)
                show_message(str(scores.loc[row, 'Player']), 'center', 70, 960, y, color=BLACK)
                show_message(str(scores.loc[row, 'Points']), 'center', 70, 1360, y, color=BLACK)
                y += 100
            draw_cursor(WIDTH / 2, 978, 176)
            show_message('BACK', 'center', 45, WIDTH / 2, 950, color=BLACK)
            if in_alpha > 0:
                in_alpha -= 25
                fade(BLACK, in_alpha)
            pygame.display.flip()
    if new_entry:
        data = {'Player': ['empty'],
                'Points': [match_time]}
        new_score = pd.DataFrame(data, columns=['Player', 'Points'])
        scores.loc[5] = new_score.loc[0]
        scores = scores.sort_values(['Points'], ascending=False).reset_index(drop=True).loc[0:4, :]
        scores.index += 1
        if any(scores.Player == 'empty'):
            name_cursor = main_cursor = 0
            initials = [None, None, None]
            while show_scores:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if 91 <= event.key <= 126 or 33 <= event.key <= 64:
                            if main_cursor == 0 and name_cursor == 0:
                                initials[0] = pygame.key.name(event.key)
                                name_cursor += 1
                                if name_cursor > 2:
                                    name_cursor = 2
                            elif main_cursor == 0 and name_cursor == 1:
                                initials[1] = pygame.key.name(event.key)
                                name_cursor += 1
                                if name_cursor > 2:
                                    name_cursor = 2
                            else:
                                initials[2] = pygame.key.name(event.key)
                                name_cursor += 1
                                if name_cursor > 2:
                                    name_cursor = 2
                        elif event.key == pygame.K_BACKSPACE:
                            for i in range(2, -1, -1):
                                if initials[i] is not None:
                                    initials[i] = None
                                    break
                                else:
                                    name_cursor -= 1
                                    if name_cursor < 0:
                                        name_cursor = 0
                        elif event.key == pygame.K_DOWN:
                            main_cursor += 1
                            if main_cursor > 1:
                                main_cursor = 0
                        elif event.key == pygame.K_UP:
                            main_cursor -= 1
                            if main_cursor < 0:
                                main_cursor = 1
                        elif main_cursor == 0 and event.key == pygame.K_RIGHT:
                            name_cursor += 1
                            if name_cursor > 2:
                                name_cursor = 0
                        elif main_cursor == 0 and event.key == pygame.K_LEFT:
                            name_cursor -= 1
                            if name_cursor < 0:
                                name_cursor = 2
                        elif main_cursor == 1 and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE):
                            scores.replace('empty', ''.join(initials), inplace=True)
                            scores.to_csv('high scores.csv', index=False)
                            show_scores = False
                game_display.fill(WHITE)
                y = 300
                for row in range(1, 6):
                    if scores.loc[row, 'Player'] == 'empty':
                        show_message(str(row), 'center', 70, 560, y, color=BLACK)
                        if initials[0] is not None:
                            show_message(initials[0], 'center', 70, 900, y, color=BLACK)
                        if initials[1] is not None:
                            show_message(initials[1], 'center', 70, 960, y, color=BLACK)
                        if initials[2] is not None:
                            show_message(initials[2], 'center', 70, 1020, y, color=BLACK)
                        show_message(str(match_time), 'center', 70, 1360, y, color=BLACK)
                        name_cursor_y = y
                        y += 100
                    else:
                        show_message(str(row), 'center', 70, 560, y, color=BLACK)
                        show_message(str(scores.loc[row, 'Player']), 'center', 70, 960, y, color=BLACK)
                        show_message(str(scores.loc[row, 'Points']), 'center', 70, 1360, y, color=BLACK)
                        y += 100
                if main_cursor == 1:
                    draw_cursor(WIDTH / 2, 978, 300)
                else:
                    pygame.draw.line(game_display, BLACK, (860, name_cursor_y + 70), (1060, name_cursor_y + 70), 5)
                show_message('CONTINUE', 'center', 45, WIDTH / 2, 950, color=BLACK)
                if in_alpha > 0:
                    in_alpha -= 25
                    fade(BLACK, in_alpha)
                pygame.display.flip()


def spawn_enemies(difficulty_level):
    if difficulty_level == 'easy':
        number_of_enemies = 4
    elif difficulty_level == 'normal':
        number_of_enemies = 6
    elif difficulty_level == 'hard':
        number_of_enemies = 8
    for i in range(number_of_enemies):
        enemy_choice = random.randint(1, 4)
        if enemy_choice == 1:
            ringos.add(Ringo())
        elif enemy_choice == 2:
            georges.add(George())
        elif enemy_choice == 3:
            johns.add(John())
        elif enemy_choice == 4:
            pauls.add(Paul())


def spawn_one_enemy():
    enemy_choice = random.randint(1, 4)
    if enemy_choice == 1:
        ringos.add(Ringo())
    elif enemy_choice == 2:
        georges.add(George())
    elif enemy_choice == 3:
        johns.add(John())
    elif enemy_choice == 4:
        pauls.add(Paul())


def spawn_stars(number_of_stars):
    [stars.add(Star()) for i in range(number_of_stars)]


def spawn_random_item(game_time, last_spawn):
    if game_time - last_spawn > random.randint(500, 1000):
        item = random.choice(['tea', 'crown', 'umbrella'])
        if item == 'tea':
            tea.add(Tea())
        elif item == 'crown':
            crown.add(Crown())
        else:
            umbrella.add(Umbrella())
        return game_time
    else:
        return last_spawn


def random_position(enemy):
    global HEIGHT, WIDTH
    position = random.choice(['left', 'right', 'up', 'down'])
    if position == 'left':
        enemy.rect.right = 0
        enemy.rect.bottom = random.randrange(0, HEIGHT + enemy.image.get_height())
    elif position == 'right':
        enemy.rect.left = WIDTH
        enemy.rect.bottom = random.randrange(0, HEIGHT + enemy.image.get_height())
    elif position == 'up':
        enemy.rect.bottom = 0
        enemy.rect.right = random.randrange(0, WIDTH + enemy.image.get_width())
    elif position == 'down':
        enemy.rect.top = HEIGHT
        enemy.rect.right = random.randrange(0, WIDTH + enemy.image.get_width())


def random_direction(enemy):
    enemy.speedx *= random.choice([-1, 1])
    enemy.speedy *= random.choice([-1, 1])


def respawn_enemy(enemy):
    if enemy.rect.top > HEIGHT:
        random_position(enemy)
        random_direction(enemy)
    elif enemy.rect.bottom < 0:
        random_position(enemy)
        random_direction(enemy)
    elif enemy.rect.left > WIDTH:
        random_position(enemy)
        random_direction(enemy)
    elif enemy.rect.right < 0:
        random_position(enemy)
        random_direction(enemy)


def bounce(item):
    if WIDTH <= item.rect.right or item.rect.left <= 0:
        item.speedx *= -1
    elif item.rect.bottom >= HEIGHT or item.rect.top <= 0:
        item.speedy *= -1


def rotate(item, original_image):
    item.rotation += item.rotation_speed
    old_center = item.rect.center
    item.image = pygame.transform.rotate(original_image, item.rotation)
    item.rect = item.image.get_rect()
    item.rect.center = old_center


def move(item):
    item.rect.y += item.speedy
    item.rect.x += item.speedx


def explode(explosion_list):
    new_list = []
    for item in explosion_list:
        if 'player' != item[1] != 'england':
            if item[1] == 'ringo':
                ringo_explosion_sound.play()
            elif item[1] == 'george':
                george_explosion_sound.play()
            elif item[1] == 'john':
                john_explosion_sound.play()
            else:
                paul_explosion_sound.play()
            new_list.append(item + ['N'])
            new_list.append(item + ['E'])
            new_list.append(item + ['S'])
            new_list.append(item + ['W'])
            new_list.append(item + ['NE'])
            new_list.append(item + ['SE'])
            new_list.append(item + ['SW'])
            new_list.append(item + ['NW'])
        else:
            if len(item) == 2:
                # explosion_data + direction, explosion number, counter
                # the counter serves as a delay between explosions
                new_list.append(item + ['N', 1, 0])
                new_list.append(item + ['E', 1, 0])
                new_list.append(item + ['S', 1, 0])
                new_list.append(item + ['W', 1, 0])
                new_list.append(item + ['NE', 1, 0])
                new_list.append(item + ['SE', 1, 0])
                new_list.append(item + ['SW', 1, 0])
                new_list.append(item + ['NW', 1, 0])
            else:
                new_list.append(item)

    for item in new_list:
        if 'player' != item[1] != 'england':
            debris.add(Debris(item))
        else:
            if item[4] == 0:
                debris.add(Debris(item))
            item[4] += 1
            if item[4] == 15:
                item[4] = 0
                item[3] += 1
    return [item for item in new_list if item[1] == 'player' and item[3] <= 4 or item[1] == 'england' and item[3] <= 4]


def show_bubble():
    show_bubble = random.choice([True] + [False] * 2)
    if show_bubble:
        bubbles.add(Bubble(p1))


def delay(original_time, intended_delay):
    if pygame.time.get_ticks() - original_time >= intended_delay:
        return True
    else:
        return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player1_sprites[0][0]
        self.current_life = 0
        self.current_angle = 0
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.radius = 30
        self.speed = 6
        self.speed_boost = 0
        self.last_shot = 0
        self.shot_delay = 100
        self.lives = 5
        self.dead = False

    def hit(self):
        global explosion_list
        self.lives -= 1
        if self.lives <= 0:
            player_explosion_sound.play()
            explosion_list.append([self.rect.center, 'player'])
            self.kill()
        else:
            self.current_life += 1
            self.image = player1_sprites[self.current_angle][self.current_life]

    def power_up(self):
        self.lives += 1
        if self.lives > 5:
            self.lives = 5
        self.current_life -= 1
        if self.current_life < 0:
            self.current_life = 0
        self.image = player1_sprites[self.current_angle][self.current_life]

    def rotate(self, degrees):
        if degrees == 0:
            self.current_angle = 0
        elif degrees == 90:
            self.current_angle = 1
        elif degrees == 180:
            self.current_angle = 2
        elif degrees == 270:
            self.current_angle = 3
        elif degrees == 45:
            self.current_angle = 4
        elif degrees == 135:
            self.current_angle = 5
        elif degrees == 225:
            self.current_angle = 6
        elif degrees == 315:
            self.current_angle = 7
        old_center = self.rect.center
        self.image = player1_sprites[self.current_angle][self.current_life]
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update(self):
        # Set screen limits
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        # Set speed boost limit
        if self.speed_boost > 10:
            self.speed_boost = 10

        keys = pygame.key.get_pressed()
        # Movement
        if keys[pygame.K_LEFT]:
            self.rect.centerx += (self.speed + self.speed_boost) * -1
        if keys[pygame.K_RIGHT]:
            self.rect.centerx += (self.speed + self.speed_boost)
        if keys[pygame.K_UP]:
            self.rect.centery += (self.speed + self.speed_boost) * -1
        if keys[pygame.K_DOWN]:
            self.rect.centery += (self.speed + self.speed_boost)
        # Rotation and shoot
        if keys[pygame.K_w] and keys[pygame.K_d]:
            self.rotate(315)
            self.shoot('NE')
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            self.rotate(225)
            self.shoot('SE')
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.rotate(135)
            self.shoot('SW')
        elif keys[pygame.K_a] and keys[pygame.K_w]:
            self.rotate(45)
            self.shoot('NW')
        else:
            if keys[pygame.K_w]:
                self.rotate(0)
                self.shoot('N')
            if keys[pygame.K_d]:
                self.rotate(270)
                self.shoot('E')
            if keys[pygame.K_s]:
                self.rotate(180)
                self.shoot('S')
            if keys[pygame.K_a]:
                self.rotate(90)
                self.shoot('W')

    def shoot(self, direction):
        if pygame.time.get_ticks() - self.last_shot > self.shot_delay:
            self.last_shot = pygame.time.get_ticks()
            shot_sound.stop()
            shot_sound.play()
            bullets.add(Bullets(self.rect.center, direction, self.speed_boost))


class Bullets(pygame.sprite.Sprite):
    def __init__(self, position, direction, speed_boost):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = bullet_sprite
        self.image = self.original_image.copy()
        self.direction = direction
        # rotates the bullets according to the direction that the player is facing
        if 'N' != direction != 'S' and 'E' != direction != 'W':
            self.image = pygame.transform.rotate(self.original_image, 45)
        self.rect = self.image.get_rect(centerx=position[0], centery=position[1])
        self.speed = 10
        self.speed_boost = speed_boost
        if self.speed_boost > 10:
            self.speed_boost = 10

    def update(self):
        if self.direction == 'N' or self.direction == 'NE' or self.direction == 'NW':
            self.rect.centery -= self.speed + self.speed_boost
        elif self.direction == 'S' or self.direction == 'SE' or self.direction == 'SW':
            self.rect.centery += self.speed + self.speed_boost
        if self.direction == 'E' or self.direction == 'NE' or self.direction == 'SE':
            self.rect.centerx += self.speed + self.speed_boost
        elif self.direction == 'W' or self.direction == 'NW' or self.direction == 'SW':
            self.rect.centerx -= self.speed + self.speed_boost

        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite
        self.rect = self.image.get_rect()
        random_position(self)
        self.speedx = speed * random.choice([-1, 1])
        self.speedy = speed * random.choice([-1, 1])

    def update(self):
        move(self)
        respawn_enemy(self)


class Ringo(Enemy):
    def __init__(self):
        Enemy.__init__(self, ringo_sprite, 2)

    def update(self):
        Enemy.update(self)


class George(Enemy):
    def __init__(self):
        Enemy.__init__(self, george_sprite, 6)

    def update(self):
        Enemy.update(self)


class John(Enemy):
    def __init__(self):
        Enemy.__init__(self, john_sprite, 8)

    def update(self):
        Enemy.update(self)


class Paul(Enemy):
    def __init__(self):
        Enemy.__init__(self, paul_sprite, 10)

    def update(self):
        Enemy.update(self)


class Debris(pygame.sprite.Sprite):
    def __init__(self, explosion_data):
        # explosion_data[0] == center of explosion (x ,y)
        # explosion_data[1] == type object to be exploded
        # explosion_data[2] == direction the debris should go
        # explosion_data[3] == determines the color of the debris based on the
        #                      number of the explosion
        pygame.sprite.Sprite.__init__(self)
        if explosion_data[1] == 'john':
            self.original_image = debris_blue
            self.player = False
        elif explosion_data[1] == 'ringo':
            self.original_image = debris_yellow
            self.player = False
        elif explosion_data[1] == 'george':
            self.original_image = debris_green
            self.player = False
        elif explosion_data[1] == 'paul':
            self.original_image = debris_orange
            self.player = False
        elif explosion_data[1] == 'player' or explosion_data[1] == 'england':
            self.player = True
            if explosion_data[3] == 1:
                self.original_image = debris_orange
            elif explosion_data[3] == 2:
                self.original_image = debris_blue
            elif explosion_data[3] == 3:
                self.original_image = debris_green
            elif explosion_data[3] == 4:
                self.original_image = debris_yellow
        self.image = self.original_image
        self.rect = self.image.get_rect(center=explosion_data[0])
        self.direction = explosion_data[2]
        self.size = 1
        self.distance = 0
        if self.player:
            self.speed = 6
            self.growth_rate = 2
            self.max_distance = 1000
            self.growth_peak = 150
        else:
            self.speed = 3
            self.growth_rate = 1
            self.max_distance = 100
            self.growth_peak = 25

    def update(self):
        self.distance += self.speed
        if self.distance >= self.max_distance:
            self.kill()
        self.size += self.growth_rate
        if self.size >= self.growth_peak:
            self.growth_rate *= -1
        if self.size <= 0:
            self.kill()

        # send the debris in a specific direction
        if self.direction == 'N':
            self.rect.centery += self.speed * -1
        elif self.direction == 'E':
            self.rect.centerx += self.speed
        elif self.direction == 'S':
            self.rect.centery += self.speed
        elif self.direction == 'W':
            self.rect.centerx += self.speed * -1
        elif self.direction == 'NE':
            self.rect.centerx += self.speed
            self.rect.centery += self.speed * -1
        elif self.direction == 'SE':
            self.rect.centerx += self.speed
            self.rect.centery += self.speed
        elif self.direction == 'SW':
            self.rect.centerx += self.speed * -1
            self.rect.centery += self.speed
        elif self.direction == 'NW':
            self.rect.centerx += self.speed * -1
            self.rect.centery += self.speed * -1

        # scales the debris
        old_center = self.rect.center
        self.image = pygame.transform.scale(self.original_image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.center = old_center


class Item(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 2 * random.choice([-1, 1])
        self.speedy = 2 * random.choice([-1, 1])
        self.rotation = 0
        self.rotation_speed = 0.1
        self.counter = 0

    def update(self):
        self.counter += 1
        move(self)
        bounce(self)
        if self.counter >= 1000:
            self.kill()  # kills the item after 1000 microseconds


class Tea(Item):
    def __init__(self):
        Item.__init__(self)
        self.image = tea_sprite  # 81 x 55
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    def update(self):
        Item.update(self)
        rotate(self, tea_sprite)


class Crown(Item):
    def __init__(self):
        Item.__init__(self)
        self.image = crown_sprite  # 75 X 76
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    def update(self):
        Item.update(self)
        rotate(self, crown_sprite)


class Umbrella(Item):
    def __init__(self):
        Item.__init__(self)
        self.image = umbrella_sprite
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    def update(self):
        Item.update(self)
        rotate(self, umbrella_sprite)


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = shield_sprite[0]
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.current_image = 0
        self.counter = 0
        shield_sound.play()

    def update(self):
        self.counter += 1
        if self.counter % 5 == 0:
            self.current_image += 1
            if self.current_image == 7:
                self.current_image = 0
        self.image = shield_sprite[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        if self.counter >= 400:
            self.kill()


class Tardis(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = tardis_sprite  # 153 x 141
        self.rect = self.image.get_rect()
        random_position(self)
        self.speedx = random.randint(1, 3) * random.choice([-1, 1])
        self.speedy = random.randint(1, 3) * random.choice([-1, 1])
        self.rotation = 0
        self.rotation_speed = 1

    def update(self):
        move(self)
        rotate(self, tardis_sprite)
        if self.rect.top >= HEIGHT or self.rect.bottom <= 0 or self.rect.right <= 0 or self.rect.left >= WIDTH:
            self.kill()


class Bubble(pygame.sprite.Sprite):
    def __init__(self, player, tardis=False):
        pygame.sprite.Sprite.__init__(self)
        if tardis:
            self.image = bubble_sprite[4]
        else:
            self.image = random.choice(bubble_sprite[:3])
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (player.rect.centerx + 45, player.rect.centery - 45)
        self.time = 0

    def update(self, player):
        self.rect.bottomleft = (player.rect.centerx + 45, player.rect.centery - 45)
        self.time += 1
        if self.time == 100:
            self.kill()


class Star(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice([star_05, star_10])
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(80, WIDTH - 80), random.randrange(80, HEIGHT - 80))
        self.last = 0

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last > random.randrange(600, 1500):
            old_center = self.rect.center
            self.image = random.choice([star_05, star_10])
            self.rect = self.image.get_rect(center=old_center)
            self.last = now


class Planet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_number = 0
        self.image = planet_sprite[0]
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))

    def hit(self):
        global explosion_list
        self.image_number += 1
        if self.image_number > 5:
            planet_explosion_sound.play()
            explosion_list.append([self.rect.center, 'england'])
            self.kill()
        else:
            self.image = planet_sprite[self.image_number]

    def heal(self):
        self.image_number -= 1
        if self.image_number < 0:
            self.image_number = 0
        self.image = planet_sprite[self.image_number]


def reset():
    global p1, england, timer, explosion_list, match_time
    player1.empty()
    ringos.empty()
    georges.empty()
    johns.empty()
    pauls.empty()
    bullets.empty()
    tea.empty()
    crown.empty()
    umbrella.empty()
    shield.empty()
    doctor.empty()
    planet.empty()
    debris.empty()
    bubbles.empty()

    p1 = Player()
    player1.add(p1)
    england = Planet()
    planet.add(england)

    explosion_list = []
    timer = 0
    match_time = 0
    pygame.mixer.stop()


def main():
    global explosion_list, timer, match_time
    last_tardis = last_item = last_heal = 0
    in_alpha = 255
    out_alpha = 0
    show_explosion = False
    reset()
    spawn_enemies(difficulty)
    main_theme.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                pause()

        stars.update()
        doctor.update()
        if timer > 100:
            ringos.update()
            georges.update()
            johns.update()
            pauls.update()
        planet.update()
        bullets.update()
        player1.update()
        tea.update()
        crown.update()
        umbrella.update()
        shield.update()
        debris.update()
        bubbles.update(p1)
        # check if bullets hit the enemies
        hits = pygame.sprite.groupcollide(ringos, bullets, True, True)
        for hit in hits:
            explosion_list.append([hit.rect.center, 'ringo'])
            spawn_one_enemy()
            p1.speed_boost += 0.2
        hits = pygame.sprite.groupcollide(georges, bullets, True, True)
        for hit in hits:
            explosion_list.append([hit.rect.center, 'george'])
            spawn_one_enemy()
            p1.speed_boost += 0.2
        hits = pygame.sprite.groupcollide(johns, bullets, True, True)
        for hit in hits:
            explosion_list.append([hit.rect.center, 'john'])
            spawn_one_enemy()
            p1.speed_boost += 0.2
        hits = pygame.sprite.groupcollide(pauls, bullets, True, True)
        for hit in hits:
            explosion_list.append([hit.rect.center, 'paul'])
            spawn_one_enemy()
            p1.speed_boost += 0.2
        # check if player touched enemy
        if len(player1) > 0:
            hits = pygame.sprite.spritecollide(p1, ringos, True, pygame.sprite.collide_circle)
            for hit in hits:
                show_bubble()
                p1.hit()
                # last_p1_hit saves the time of the last hit to be used on the
                # death delay:
                last_p1_hit = pygame.time.get_ticks()
                explosion_list.append([hit.rect.center, 'ringo'])
                spawn_one_enemy()
                p1.speed_boost = 0
            hits = pygame.sprite.spritecollide(p1, georges, True, pygame.sprite.collide_circle)
            for hit in hits:
                show_bubble()
                p1.hit()
                last_p1_hit = pygame.time.get_ticks()
                explosion_list.append([hit.rect.center, 'george'])
                spawn_one_enemy()
                p1.speed_boost = 0
            hits = pygame.sprite.spritecollide(p1, johns, True, pygame.sprite.collide_circle)
            for hit in hits:
                show_bubble()
                p1.hit()
                last_p1_hit = pygame.time.get_ticks()
                explosion_list.append([hit.rect.center, 'john'])
                spawn_one_enemy()
                p1.speed_boost = 0
            hits = pygame.sprite.spritecollide(p1, pauls, True, pygame.sprite.collide_circle)
            for hit in hits:
                show_bubble()
                p1.hit()
                last_p1_hit = pygame.time.get_ticks()
                explosion_list.append([hit.rect.center, 'paul'])
                spawn_one_enemy()
                p1.speed_boost = 0
            # check if player got tea
            hits = pygame.sprite.spritecollide(p1, tea, True, pygame.sprite.collide_circle)
            for hit in hits:
                tea_sound.play()
                p1.power_up()
            # check if player got crown
            hits = pygame.sprite.spritecollide(p1, crown, True, pygame.sprite.collide_circle)
            for hit in hits:
                show_explosion = True
                crown_sound.play()
                explosion = timer
                for paul in pauls:
                    explosion_list.append([paul.rect.center, 'paul'])
                    paul.kill()
                for ringo in ringos:
                    explosion_list.append([ringo.rect.center, 'ringo'])
                    ringo.kill()
                for george in georges:
                    explosion_list.append([george.rect.center, 'george'])
                    george.kill()
                for john in johns:
                    explosion_list.append([john.rect.center, 'john'])
                    john.kill()
            # spawn new enemies after the old ones exploded
            if len(ringos) == len(georges) == len(johns) == len(pauls) == 0:
                if timer - explosion == 100:
                    spawn_enemies(difficulty)
            # check if player got umbrella
            hits = pygame.sprite.spritecollide(p1, umbrella, True, pygame.sprite.collide_circle)
            for hit in hits:
                # used shld otherwise it wouldn't be possible to use
                # spritecollide and the collision wouldn't work the way
                # I wanted it to work
                if len(planet) > 0:
                    shield.empty()
                    shld = Shield()
                    shield.add(shld)
        # check if enemies hit shield
        if len(shield) > 0:
            hits = pygame.sprite.spritecollide(shld, ringos, False, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'ringo'])
                hit.kill()
                spawn_one_enemy()
            hits = pygame.sprite.spritecollide(shld, georges, False, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'george'])
                hit.kill()
                spawn_one_enemy()
            hits = pygame.sprite.spritecollide(shld, johns, False, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'john'])
                hit.kill()
                spawn_one_enemy()
            hits = pygame.sprite.spritecollide(shld, pauls, False, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'paul'])
                hit.kill()
                spawn_one_enemy()
        # check if enemies hit planet
        if len(planet) > 0:
            hits = pygame.sprite.spritecollide(england, ringos, True, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'ringo'])
                england.hit()
                last_england_hit = pygame.time.get_ticks()
                spawn_one_enemy()
            hits = pygame.sprite.spritecollide(england, georges, True, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'george'])
                england.hit()
                last_england_hit = pygame.time.get_ticks()
                spawn_one_enemy()
            hits = pygame.sprite.spritecollide(england, johns, True, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'john'])
                england.hit()
                last_england_hit = pygame.time.get_ticks()
                spawn_one_enemy()
            hits = pygame.sprite.spritecollide(england, pauls, True, pygame.sprite.collide_rect)
            for hit in hits:
                explosion_list.append([hit.rect.center, 'paul'])
                england.hit()
                last_england_hit = pygame.time.get_ticks()
                spawn_one_enemy()
            # spawns a random item
            last_item = spawn_random_item(timer, last_item)
            # Spawn tardis and power ups
            if timer - last_tardis == 4000:
                doctor.add(Tardis())
                last_tardis = timer
            # show tardis bubble
            if len(doctor) > 0 and len(player1) > 0:
                tardis_bubble = Bubble(p1, True)
                bubbles.add(tardis_bubble)
            # Heal England
            if timer - last_heal == 600:
                planet_recovery_sound.play()
                england.heal()
                last_heal = timer
            # stops
        # Explode everything
        explosion_list = explode(explosion_list)
        # Run the clock
        timer += 1
        # Draw to screen
        if show_explosion:
            game_display.fill(WHITE)
            show_explosion = False
        else:
            game_display.fill(BLACK)
            stars.draw(game_display)
            doctor.draw(game_display)
            planet.draw(game_display)
            bullets.draw(game_display)
            player1.draw(game_display)
            if len(player1) > 0:
                bubbles.draw(game_display)
            ringos.draw(game_display)
            georges.draw(game_display)
            johns.draw(game_display)
            pauls.draw(game_display)
            debris.draw(game_display)
            tea.draw(game_display)
            crown.draw(game_display)
            umbrella.draw(game_display)
            shield.draw(game_display)

        # handles fade in at the start of the round
        if in_alpha > 0:
            in_alpha -= 15
            fade(BLACK, in_alpha)
        else:
            # show countdown before starting the round
            if timer <= 25:
                show_message('3', 'center', 100, WIDTH / 2, 200)
            elif 25 <= timer < 50:
                show_message('2', 'center', 100, WIDTH / 2, 200)
            elif 50 <= timer < 75:
                show_message('1', 'center', 100, WIDTH / 2, 200)
            elif 75 <= timer < 100:
                show_message('GO!', 'center', 100, WIDTH / 2, 200)
            elif timer >= 100 and len(player1) > 0 and len(planet) > 0:
                # starts the match's clock after 'GO!' and stops
                # if either the planet or the player explode
                match_time += 1
                show_message(str(match_time), 'left', 40, 40, 40)
        # handles fade out when game over
        if len(player1) == 0:
            if len(planet) == 0:
                if last_p1_hit < last_england_hit:
                    if delay(last_p1_hit, 2000):
                        if out_alpha < 255:
                            out_alpha += 25
                            fade(WHITE, out_alpha)
                        else:
                            game_over()
                else:
                    if delay(last_england_hit, 2000):
                        if out_alpha < 255:
                            out_alpha += 25
                            fade(WHITE, out_alpha)
                        else:
                            game_over()
            if len(planet) == 1:
                if delay(last_p1_hit, 2000):
                    if out_alpha < 255:
                        out_alpha += 25
                        fade(WHITE, out_alpha)
                    else:
                        game_over()
        else:
            if len(planet) == 0:
                if delay(last_england_hit, 2000):
                    if out_alpha < 255:
                        out_alpha += 25
                        fade(WHITE, out_alpha)
                    else:
                        game_over()

        show_message(f'FPS = {str(clock)[11:-2]}', 'center', 40, WIDTH - 200, HEIGHT - 100)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    p1 = Player()
    england = Planet()

    player1 = pygame.sprite.GroupSingle(p1)
    ringos = pygame.sprite.Group()
    georges = pygame.sprite.Group()
    johns = pygame.sprite.Group()
    pauls = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    tea = pygame.sprite.Group()
    crown = pygame.sprite.Group()
    umbrella = pygame.sprite.Group()
    shield = pygame.sprite.GroupSingle()
    stars = pygame.sprite.Group()
    doctor = pygame.sprite.GroupSingle()
    planet = pygame.sprite.GroupSingle(england)
    debris = pygame.sprite.Group()
    bubbles = pygame.sprite.GroupSingle()

    spawn_stars(100)
    difficulty = 'normal'
    explosion_list = []
    timer = match_time = 0

    start_screen()
