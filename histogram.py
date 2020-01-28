def histogram(source_text):
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
    return len(histogram)


def frequency(word, histogram):
    return histogram[word]

if __name__ == "__main__":
    source_text = 'words.txt'
    words = histogram(source_text)
    print(words)
    print(unique_words(words))
    print(frequency('beyond', words))