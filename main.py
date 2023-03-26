import streamlit as st
import random

st.title('Wonderful Words')
st.caption('A simple experiment to select and display some wonderful words.')

x = st.slider('How many words would you like?', 1, 20, 5)

def generate_words():
    # Create a list of words.
    words = ["nature", "love", "avocado","utopia","gratitude","beauty", "life", "death","adventure","home","play","peace", "war", "hope", "despair", "joy", "sorrow", "happiness", "euphoria"]

    # Generate a random number to select a word.
    index = random.randint(0, len(words) - 1)

    # Return the word at the given index.
    return words[index]

def main():
    for _ in range(x):
        # Generate a list of words.
        listwords = generate_words()

        # Print the haiku.
        st.write(listwords)

if __name__ == "__main__":
    main()


st.caption('Enjoy your day!')
st.markdown("Other [sketches by logikblok](https://logikblok.github.io/sketches)")