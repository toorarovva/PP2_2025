import pygame
import os

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

MUSIC_FOLDER = "C:\\Users\\User\\OneDrive\\Рабочий стол\\PP2_2025\\lab7"
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]

if not songs:
    print("No MP3 files found in the directory!")
    exit()

current_song = 0
is_paused = False 

def play_song():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
    else:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_song]))
        pygame.mixer.music.play()

def stop_song():
    global is_paused
    pygame.mixer.music.stop()
    is_paused = False  

def pause_song():
    global is_paused
    pygame.mixer.music.pause()
    is_paused = True

def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    play_song()

def previous_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    play_song()

play_song()

running = True
while running:
    screen.fill((30, 30, 30))  
    pygame.display.flip()  
    pygame.event.pump()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_song()
            elif event.key == pygame.K_s:
                stop_song()
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_b:
                previous_song()
            elif event.key == pygame.K_SPACE:
                pause_song()

pygame.quit()
