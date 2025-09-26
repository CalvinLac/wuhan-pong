import time
import random
import pygame
import winsound

def random_interval():
    return random.uniform(7, 13)

def play_audio(file_path):
    pygame.mixer.init()
    time.sleep(0.3)
    pygame.mixer.music.load(file_path)
    time.sleep(0.3)
    pygame.mixer.music.play()

def beep():
    frequency = 3500 
    duration = 750 
    winsound.Beep(frequency, duration)

def main():
    try:
        audio_file = './pre-beep.mp3' 
        while True:
            interval = random_interval()
            print(f"Next audio and beep in {interval:.2f} seconds...")
            play_audio(audio_file)
            time.sleep(interval)
            beep()
            time.sleep(3)
    except KeyboardInterrupt:
        pygame.mixer.quit()
        print("Program terminated by user.")

if __name__ == "__main__":
    main()