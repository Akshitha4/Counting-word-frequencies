"""Count words."""
import string, re

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    #Convert to lowercase
    text = text.lower()
    #Split text into tokens (words), leaving out punctuation
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    text = regex.sub('', text)
    tokens = text.split()
    for token in tokens:
        text_token = regex.sub('', token)
        # print('token is ',text_token)
        # print('checking dict : ', counts.get(text_token))
        items_in_dict = counts.keys()
        # print('items_in_dict', items_in_dict)
        if text_token in counts.keys():
            counts[text_token] = int (counts.get(text_token)) + 1
        else:
            counts[text_token] = 1
    return counts

def test_run():
    with open("input.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()
