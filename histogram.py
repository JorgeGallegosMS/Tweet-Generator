from random import randint

def get_index(word, word_list):
    """Finds the index of a word in a given list. 
       Returns -1 if no index was found"""
    index = 0
    for item in word_list:
        if item[0] == word:
            return index
        else:
            index += 1

    return -1

def histogram(source_text):
    """Takes in the name of the file and returns a 
       dictionary of how often words appear in the text"""
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

def list_histogram(source_text):
    """Takes in the name of the file and returns a sorted 
       list of how often words appear in the text"""
    with open(source_text, 'r') as file:
        lines = file.read()
        words = lines.split()

        word_frequency = []

        for word in words:
            word = word.lower().rstrip(',.')
            index = get_index(word, word_frequency)

            if index == -1:
                word_frequency.append([word, 1])
            else:
                word_frequency[index][1] += 1

        word_frequency.sort()

        return word_frequency

def sample(histogram):
    tokens = sum([count for word, count in histogram.items()])
    dart = randint(1, tokens)

    fence = 0
    for word, count in histogram.items():
        fence += count
        if fence >= dart:
            return word

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
    print(sample(words))