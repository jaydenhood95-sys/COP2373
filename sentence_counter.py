
import re


def get_paragraph():
    """Get a paragraph from the user."""
    
    # Ask the user to enter a paragraph
    paragraph = input("Enter a paragraph: ")
    
    return paragraph


def find_sentences(paragraph):
    """Find individual sentences using a regular expression."""
    
    # Allow sentences to begin with a capital letter or a number.
    # The look-ahead checks for the beginning of the next sentence.
    pattern = r'(?:[A-Z]|\d+\.).*?[.!?](?=\s+(?:[A-Z]|\d+\.)|$)'
    
    # Find all sentences in the paragraph
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL)
    
    return sentences


def display_sentences(sentences):
    """Display each sentence and the total number of sentences."""
    
    # Display each individual sentence
    print("\nIndividual sentences:")
    
    for number, sentence in enumerate(sentences, 1):
        print(f"{number}. {sentence.strip()}")
    
    # Display the total number of sentences
    print(f"\nNumber of sentences: {len(sentences)}")


def main():
    """Run the sentence counting program."""
    
    # Get the paragraph from the user
    paragraph = get_paragraph()
    
    # Find the sentences in the paragraph
    sentences = find_sentences(paragraph)
    
    # Display the sentences and count
    display_sentences(sentences)


# Start the program
if __name__ == "__main__":
    main()
