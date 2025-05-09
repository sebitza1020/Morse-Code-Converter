import argparse
import sys

# International Morse Code mapping (ITU standard)
MORSE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',  "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',   ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.',
    '=': '-...-',  '+': '.-.-.',  '-': '-....-',  '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
}

WORD_GAP = ' / '  # separates words in output
CHAR_GAP = ' '     # separates characters in output

def text_to_morse(text: str) -> str:
    """Translate a text string to Morse code."""
    code_words = []
    for word in text.strip().split():
        coded_chars = []
        for ch in word:
            ch_up = ch.upper()
            if ch_up in MORSE:
                coded_chars.append(MORSE[ch_up])
            else: # keep unknowns as question marks
                coded_chars.append('¿')
        code_words.append(CHAR_GAP.join(coded_chars))
    return WORD_GAP.join(code_words)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert Text to Morse Code.",
        epilog="If no TEXT is provided, the program will prompt you."
    )
    parser.add_argument('text', nargs='*', help='Text to convert')
    args = parser.parse_args(argv)

    if args.text:
        input_text = ' '.join(args.text)
    else:
        try:
            input_text = input("Enter text to convert: ")
        except (EOFError, KeyboardInterrupt):
            print(file=sys.stderr)
            return 1

    print(text_to_morse(input_text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
