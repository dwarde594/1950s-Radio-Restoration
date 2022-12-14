# 1950s-Radio-Restoration
This code turned a Peto Scott radio from he 1950s into an MP3 player that plays random songs in a given channel. The project uses 2 potentiometers, a speaker, a power switch, a [Hifiberry DAC Audio Amp SHIM](https://thepihut.com/products/audio-amp-shim-3w-mono-amp), a [Raspberry Pi Zero W](https://thepihut.com/products/raspberry-pi-zero-w), an [MCP3008 ADC](https://thepihut.com/products/adafruit-mcp3008-8-channel-10-bit-adc-with-spi-interface), and a [battery](https://thepihut.com/products/4-way-18650-battery-holder) for the Raspberry Pi. One potentiometer controls the volume, while the other is used to change the channel that the Pi plays from. There are 4 channels. A classical channel, jazz channel, pop channel and a rock channel. When the tuning potnetiometer points to one of these channels, the genre of music is played through the speaker. When the channel changes, white noise is played to mimic the tuning noise in analogue radios. The music is stored in the "/home/pi/Music/" path. A folder for each channel can be found in this path containing all the songs that the radio plays. Songs can be downloaded into each of the folders and the radio will randomly select songs from the folders.
## Setup
### Raspberry Pi software
Any Raspberry Pi can be used. I used a Zero W for my project. Install Raspian Buster onto the Pi using the Raspberry Pi imager (you can choose if you want to use SSH or Desktop) and make sure you enable SSH.
Edit the config.txt file using this command in the terminal.
```
sudo nano /boot/config.txt
```
At the bottom of the file, enter this line. This will configure the audio DAC to work with the Pi.
```
dtoverlay=hifiberry-dac
```
Enter this command into the terminal to enter the raspi-config. Then, enable SPI. This is found under Interface > SPI > Enable in the raspi-config settings.
```
sudo raspi-config
```
Make sure git is installed on your Raspberry Pi by typing this into the terminal.
```
sudo apt install git
```
Now, enter this command. Take note of the path to the python file (by default, this will be /home/pi/1950s-Radio-Restoration/music_playerv3.py)
```
git clone https://github.com/dwarde594/1950s-Radio-Restoration
```
Next, enter this command into the terminal making sure you don't use the sudo command at the front.
```
crontab -e
```
Scroll to the bottom of the file and enter this line. Replace the path with the path to your python file.
```
@reboot python3 /home/pi/1950s-Radio-Restoration/music_playerv3.py
```
## Circuit
![18_08_2022, 11_40 Microsoft Lens](https://user-images.githubusercontent.com/101138000/185376244-e8c34fa1-5a1a-44f4-978c-682e9fd31c91.jpg)
## Downloading songs
The best way of downloading songs onto the Pi is by using [FileZilla](https://filezilla-project.org/). To connect to the Pi through FileZilla, you need to find the IP address. Use the command below to find the Pi's IP address.
```
hostname -I
```
Then, enter this IP address into FileZilla and connect to the Pi using SFTP. You can start adding songs into the /home/pi/Music directory under the Classical, Jazz, Rock, and Pop folders.
