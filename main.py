import simpleaudio as sa
import numpy as np
import time

# Morse code sound configuration
DOT_DURATION = 1.0  # Duration of a dot in seconds
DASH_DURATION = 1.5  # Duration of a dash in seconds
FREQUENCY = 440.0    # Frequency of the tone in Hz
SILENCE_DURATION = 2.0  # Silence between signals

morse_dictionary = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-",
    " ": " "
}

def get_text_input():
    print("\n")
    text_input = input("Please write the text to translate: ")
    return text_input

def translate_to_morse(input_text):
    output_morse = []
    for letter in input_text:
        if letter in morse_dictionary:
            output_morse.append(morse_dictionary[letter])
    return output_morse


# Function to generate a sound wave for a given duration
def generate_tone(duration):
    sample_rate = 44100  # Hz
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = 0.5 * np.sin(2 * np.pi * FREQUENCY * t)
    tone = (tone * 32767).astype(np.int16)  # Convert to 16-bit PCM format
    return sa.WaveObject(tone.tobytes(), 1, 2, sample_rate)


# Function to play Morse code
def play_morse(morse_list):
    dot_wave = generate_tone(DOT_DURATION)
    dash_wave = generate_tone(DASH_DURATION)

    for symbol in morse_list:
        if symbol == '.':
            dot_wave.play().wait_done()
        elif symbol == '-':
            dash_wave.play().wait_done()
        time.sleep(SILENCE_DURATION)  # Pause between symbols



if __name__ == '__main__':
    print("Code Morse Translator")
    user_text_input = get_text_input()
    output_morse = translate_to_morse(user_text_input)
    print(output_morse)
    # Flatten the list into individual symbols
    flattened_morse = [char for code in output_morse for char in code]
    # Play the Morse code
    play_morse(flattened_morse)

