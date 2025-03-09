# Python Plays Pokémon
[🇫🇷 Français](README.md) | [🇬🇧 English](README.en.md)

## Overview
This project is a Python script that simulates playing Pokémon through a Twitch live chat!. The script interacts with a Pokémon game(or any gameboy games) by sending commands through the chat to control the game, such as moving the character, battling, and navigating menus. The goal was to make a fun project where I can interract with different people and see their choices in game..
I made it in 2023/2024 while finishing highschool.

## Features
- **Automated Gameplay**: The script can simulate button presses to control the game.
- **Customizable Actions**: Users can define sequences of actions to perform specific tasks in the game.
- **Integration with Emulators**: The script is designed to work with popular emulators that allow external input control.
- - **Vote retrieving**: I used pandas to retrieve the votes inside a csv file. >> It's actually not needed and anything related to that can be deleted. <<

## Requirements
- Python 3.x
- A GBA Pokémon game ROM 
- An emulator that supports external input control (I used Visual Boy Advance personally. link: https://visualboyadvance.org/)
- A livestreaming service such as OBS or Streamlabs
- - Required Python libraries: pyautogui, pandas (if you didn't remove the lines of code)
Just run in a terminal:
   ```bash
   pip install pyautogui
   ```
   ```bash
   pip install pandas
   ```

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ehallou/newton-plays-pokemon.git
   cd newton-plays-pokemon
   ```
1. **Set Up the Emulator**:
   - Ensure your emulator is configured to accept external inputs.
   - Load the Pokémon ROM into the emulator.
   - Change or keep the controls the same (ex. z, q , s , d).

3. **Change the OAuth key and USER, PASS to your own**:
You will find your OAuth key here after logging into twitch!: https://twitchtokengenerator.com/
The website should be working. However if it doesn't work, other websites are available.

5. **Run the Script**:
   ```bash
   python newton-plays-pokemon-ENG.py
   ```
6. **Livestream**
There are many tutorials online on how to setup your livestream.
https://www.lifewire.com/twitch-streaming-with-obs-studio-4151808


## Usage
- **Running the Script**: Execute the script while the emulator is running. The script will send inputs to the emulator to control the game through the twitch chat.
(the emulator should be the selected window to receive inputs)

## Example
Here’s a simple example of how the script might send a sequence of button presses:
![image](https://github.com/user-attachments/assets/591f3316-ac08-4ee1-bec3-fae67e5eab3c)


## Contributing
Since this is a project I finished in 2024, I don't mind contributions.
So contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is not licensed, feel free to use it however you want.

## Acknowledgments
- Special thanks to my Computer Science teacher for this project idea!
- Thanks to the creators of the Pokémon games and the emulator developers.
- Inspired by various automation communities AND the Social experiment "Twitch Plays Pokemon". learn more about it here: https://fr.wikipedia.org/wiki/Twitch_Plays_Pok%C3%A9mon

## Disclaimer
This project is for educational and entertainment purposes only. 
