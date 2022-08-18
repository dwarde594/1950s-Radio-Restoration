#This version of the code works with a power button/switch. V1 doesn't have this feature

from os import listdir, system
import pygame
from random import randint
from time import sleep
from gpiozero import MCP3008, Button

#Initiates pygame
pygame.init()

#On variable stays True until device is turned off
on = True

#Power button
power_button = Button(3)


#Initiates MCP3008 analogue inputs
vol_potentiometer = MCP3008(0)
tuning_potentiometer = MCP3008(1)


#Directory for music files depends on value of tuning potentiometer
if tuning_potentiometer.value < 0.25:
    #Path variable stores the playing music channel (the one in action at the moment)
    path = "/home/pi/Music/Classical/"
    #Current_path variable stores current music channel (the variable that updates in the while loop)
    current_path = "/home/pi/Music/Classical/"
elif tuning_potentiometer.value >= 0.25 and tuning_potentiometer.value < 0.5:
    path = "/home/pi/Music/Jazz/"
    current_path = "/home/pi/Music/Jazz/"
elif tuning_potentiometer.value >= 0.5 and tuning_potentiometer.value < 0.75:
    path = "/home/pi/Music/Pop/"
    current_path = "/home/pi/Music/Pop/"
elif tuning_potentiometer.value >= 0.75 and tuning_potentiometer.value <= 1:
    path = "/home/pi/Music/Rock/"
    current_path = "/home/pi/Music/Rock/"



#Searches for all files in the directory
sound_files = listdir(path)


#Initialises the music end event
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)


#List that stores all played pieces during the session
played_pieces = []



#Creates speaker volume and rounds it to 2 decimal places
speaker_volume = round(vol_potentiometer.value, 2)
pygame.mixer.music.set_volume(speaker_volume)



#Function that plays a new random piece
def new_piece():
    global played_pieces
    
    #Piece played variable becomes True if it has been played and false if it hasn't
    piece_played = True
    
    
    #Checks if all the pieces have been played in the session
    if len(played_pieces) >= len(sound_files):
        #If all pieces have been played, reset the played pieces list and start again
        played_pieces = []
        
    
    while piece_played == True:

        #Generate random piece
        piece = randint(0, len(sound_files) - 1)
        
        #Checks if the piece has been played
        if sound_files[piece] in played_pieces:
            piece_played = True
            
        else:
            piece_played = False
    
        

    #Loads the random piece
    pygame.mixer.music.load(path + sound_files[piece])
    
    #Prints the name of the piece
    print(sound_files[piece])
    
    #Plays the piece
    pygame.mixer.music.play()
    
    
    #Adds piece to the played pieces list
    played_pieces.append(sound_files[piece])
    
    


#Function that shuts down the computer
def shut_down():
    print("Shutting down")
    #On variable fetched and defined as False
    global on
    on = False

    #Music fades out and is unloaded
    pygame.mixer.music.fadeout(2000)
    sleep(2)
    
    #Uninitialises all pygame modules
    pygame.quit()

    #System shuts down
    system("shutdown -h now")


#When the power button is pressed, shut the pi down
power_button.when_released = shut_down


    
#Function called when channel is changed
def tune():
    
    #Sets temporary lower volume for the white noise
    pygame.mixer.music.set_volume(0.05)
    
    #Loads and plays white noise for 3 seconds
    pygame.mixer.music.load("/home/pi/Music/white_noise.wav")
    pygame.mixer.music.play()
    
    #Sleeps for 3 seconds
    sleep(3)
    
    #Resets volume to original value
    pygame.mixer.music.set_volume(speaker_volume)


    

#Plays new song when program starts
new_piece()



#Main loop
while on == True:
    
    
    #Sleeps for 0.01 seconds
    sleep(0.01)
    
    #Current tuning value of potentiometer
    current_tuning_value = round(tuning_potentiometer.value,2)
    
    
    
    
    #Directory for music files depends on value of tuning potentiometer
    if current_tuning_value < 0.25:
        current_path = "/home/pi/Music/Classical/"
    elif current_tuning_value >= 0.25 and current_tuning_value < 0.5:
        current_path = "/home/pi/Music/Jazz/"
    elif current_tuning_value >= 0.5 and current_tuning_value < 0.75:
        current_path = "/home/pi/Music/Pop/"
    elif current_tuning_value >= 0.75 and current_tuning_value <= 1:
        current_path = "/home/pi/Music/Rock/"
        
        
    #Checks if the current_path is not equal to the path
    if current_path != path:
        
        #If so, change the main path and play a new song
        path = current_path
        
        #Updates the sound_files array with the new path
        sound_files = listdir(path)
        
        #Resets played pieces array
        played_pieces = []
        
        #White noise plays for 3 seconds through the tune function
        tune()
        
        #Calls the new_piece function
        new_piece()
        

    
    
    #Sets volume as value of volume potentiometer every tick
    speaker_volume = round(vol_potentiometer.value, 2)
    pygame.mixer.music.set_volume(speaker_volume)


    
    #Checks if the song has ended. If so, it plays a new song
    for event in pygame.event.get():
        if event.type == SONG_END and on == True:
            new_piece()
            
            

