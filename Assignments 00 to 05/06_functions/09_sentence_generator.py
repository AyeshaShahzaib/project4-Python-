def make_sentence(word, part_of_speech):
    # Check the part of speech and create a sentence accordingly
    if part_of_speech == 0:
        # Noun template
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        # Verb template
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        # Adjective template
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    # Prompt user for word and part of speech
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    
    # Call make_sentence to print the appropriate sentence
    make_sentence(word, part_of_speech)

# Call main() to run the program
main()
