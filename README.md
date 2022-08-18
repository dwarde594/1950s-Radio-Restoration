# 1950s-Radio-Restoration
This code turned a Peto Scott radio from he 1950s into an MP3 player that plays random songs in a given channel. The project uses 2 potentiometers, a speaker, and a power switch, a Raspberry Pi Zero W, and a battery for the Raspberry Pi. One potentiometer controls the volume, while the other is used to change the channel that the Pi plays from. There are 4 channels. A classical channel, jazz channel, pop channel and a rock channel. When the tuning potnetiometer points to one of these channels, the genre of music is played through the speaker. When the channel changes, white noise is played to mimic the tuning noise in analogue radios. The music is stored in the "/home/pi/Music/" path. A folder for each channel can be found in this path containing all the songs that the radio plays. Songs can be downloaded into each of the folders and the radio will randomly select songs from the folders.
