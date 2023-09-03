import streamlit as st

morse_code_dict = {
    'A': '._',
    'B': '_...',
    'C': '_._.',
    'D': '_..',
    'E': '.',
    'F': '.._.',
    'G': '__.',
    'H': '....',
    'I': '..',
    'J': '.___',
    'K': '_._',
    'L': '._..',
    'M': '__',
    'N': '_.',
    'O': '___',
    'P': '.__.',
    'Q': '__._',
    'R': '._.',
    'S': '...',
    'T': '_',
    'U': '.._',
    'V': '..._',
    'W': '.__',
    'X': '_.._',
    'Y': '_.__',
    'Z': '__..'
}

def morse_to_alphabet(morse_code):
    words = morse_code.split(' ')
    alphabet_text = ''
    for word in words:
        if word in morse_code_dict:
            alphabet_text += morse_code_dict[word]
        else:
            alphabet_text += '?'
    return alphabet_text

def alphabet_to_morse(alphabet_text):
    morse_code = ''
    for char in alphabet_text:
        if char == ' ':
            morse_code += ' '
        elif char.upper() in morse_code_dict:
            morse_code += morse_code_dict[char.upper()] + ' '
        else:
            morse_code += '? '
    return morse_code.strip()

st.title("Morse Code Converter")

conversion_choice = st.radio("Choose conversion:", ('Message to Morse Code', 'Morse Code to Message'))

if conversion_choice == 'Message to Morse Code':
    user_input = st.text_input("Enter a message to convert to Morse code:")
    result = alphabet_to_morse(user_input)
    st.write(f"Converted to Morse code: {result}")
elif conversion_choice == 'Morse Code to Message':
    user_input = st.text_input("Enter Morse code (use '.' for dot and '-' for dash, separate letters with spaces):")
    result = morse_to_alphabet(user_input)
    st.write(f"Converted to alphabet: {result}")
