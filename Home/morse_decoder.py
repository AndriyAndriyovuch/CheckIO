MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    a = code.replace('   ', ' space ')

    code_list = a.split()
    res_list = []

    for i in code_list:
        if i in MORSE:
            res_list.append(MORSE[i])
        elif i == 'space':
            res_list.append('_')

    code_string = ''.join(res_list)
    done = code_string.replace('_', ' ')

    result = done.capitalize()

    return result


if __name__ == "__main__":
    print("Example:")
    print(morse_decoder("... --- -- .   - . -..- -"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert (
            morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")
            == "It was a good day"
    )
    print("Coding complete? Click 'Check' to earn cool rewards!")
