# Speak and Spell
#### Video Demo:  <https://www.youtube.com/watch?v=vcc8c1wCYIU>
## Description:
This command-line program aims to replicate the experience of using the popular **Speak and Spell** toy.

I made this as my final project for [CS50P](https://cs50.harvard.edu/python/).

&nbsp;

**Speak and Spell** has five modes available:

- **Spell**

    In this mode, you will be asked to spell ten words. At the start, you can select between four levels of difficulty using the `A`, `B`, `C`, and `D` keys.

- **Say It**

    This mode is similar to *Spell*, but you will first be shown each of the words and asked to say them aloud. As in the *Spell* mode, you can select the difficulty using the `A`, `B`, `C`, and `D` keys.

- **Mystery Word**

    This mode plays similar to hangman. You try to reveal a word, by guessing one letter at a time. If you guess incorrectly seven times, you lose.


- **Secret Code**

    You can type freely in this mode. When you press Enter, your text will be converted into a secret code. Pressing Enter again will change it back.

- **Letter**

    This mode functions the same as *Secret Code*, but the computer will choose a random letter to start you off with.


## Files
The project consists of these files:

- **speakandspell.py**

    This is the program itself. It's all contained in a single file.

- **test_speakandspell.py**

    This file contains tests that can be used with `pytest` to test three of the functions in `project.py`.

## Dependencies
This project uses the following standard libraries:

- **sys**

    *sys.exit* gives us the ability to end the program whenever we wish.

- **random**

    *random.sample* provides the ability to choose random words and letters.

- **time**

    *time.sleep* is used to momentarily pause the program, so that the text-to-speech doesn't speak too fast.

&nbsp;


The following third-party libraries are also needed:

- **py3-tts**

    This is a text-to-speech library used for generating speech.
    This is a fork of the more well-known *pyttsx3*. I used it because *pyttsx3* kept giving me ALSA errors in Linux.

- **get-key**

    This library is used for detecting keystrokes. This allows the program to immediately respond when you press a key, without the need to press Enter afterward.

&nbsp;

Both libraries can be installed using `pip`:

 ```
 pip install py3-tts

 pip install get-key
 ```

&nbsp;

In addition, Linux users may need to install the following programs using their system's package manager in order for `py3-tts` to work:

- `espeak`

- `ffmpeg`

- `libespeak1`

In Debian/Ubuntu:

```shell
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

&nbsp;

## Usage
Starting the program is easy. Simply run:

`python speakandspell.py`

&nbsp;




### Controls

The number keys can be used to change modes and perform other functions:

1. **Off** - This exits the program and returns you to your command prompt.
2. **Go** - In the *Spell* and *Say It* modes, this begins a new game at the currently selected difficulty.
3. **Replay** - In the *Spell* and *Say It* modes, this will allow you to start over using the same word list.
4. **Repeat** - In the *Spell* and *Say It* modes, the current word will be stated again.
5. **Clue** - In the *Mystery Word* mode, this will reveal one of the letters for you. Using a clue will use up two of your seven chances.
6. **Mystery Word** - Switch to the *Mystery Word* mode.
7. **Letter** - Switch to the *Letter* mode.
8. **Secret Code** - Switch to the *Secret Code* mode.
9. **Say It** - Switch to the *Say It* mode.
0. **Spell** - Switch to the *Spell* mode.

All of the relevant functions will also be displayed on screen.

## Limitations
On Linux, the text to speech may not work if there are other programs trying to play audio at the same time.
