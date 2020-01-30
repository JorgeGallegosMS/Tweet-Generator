def histogram(source_text):
    """Takes in the name of the file and returns a 
       histogram of how often words appear in the text"""
    with open(source_text, 'r') as file:
        lines = file.read()
        words = lines.split()
        
        word_frequency = {}

        for word in words:
            word = word.lower().rstrip('.,')
            if word in word_frequency.keys():
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        return word_frequency

def unique_words(histogram):
    """Returns the number of unique words in the histogram"""
    return len(histogram)


def frequency(word, histogram):
    """Returns the number of times the word appears
       in the histogram"""
    return histogram[word]

if __name__ == "__main__":
    source_text = 'words.txt'
    words = histogram(source_text)
    print(words)
    print(unique_words(words))
    print(frequency('exalted', words))