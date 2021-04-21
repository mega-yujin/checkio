MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    decoded_list = []
    words = [word.split(" ") for word in code.split("   ")]
    for word in words:
        for letter in word:
            decoded_list.append(MORSE[letter])
        decoded_list.append(" ")
    decoded_text = "".join(decoded_list).rstrip()
    if decoded_text[0].isdigit():
        return decoded_text
    else:
        return decoded_text.capitalize()


if __name__ == '__main__':
    print("Example:")
    print(morse_decoder('... --- ...'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")