"""Text parsing functions for cleaning movie description text."""

from string import punctuation


def load_stopwords(filepath='data/stopwords.txt'):
    """Load stopwords from a text file into a set."""
    stopwords = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip().lower()
            if word:
                stopwords.add(word)
    return stopwords


def lowercase_text(text):
    """Return a text string with all characters lower-cased."""
    return text.lower()


def remove_punctuation(text, punctuation_chars=punctuation):
    """Return a text string without punctuation characters."""
    for character in punctuation_chars:
        text = text.replace(character, '')
    return text


def remove_newline(text):
    """Remove newline characters and trim leading/trailing whitespace."""
    return text.replace('\n', '').strip()


def split_text_into_words(text):
    """Split a text string into a list of words."""
    return text.split()


def remove_stopwords(word_lst, stopwords_set):
    """Remove words that are present in the stopwords set."""
    return [word for word in word_lst if word not in stopwords_set]


def replace_names(word_lst, name_set, replacement_val):
    """Replace names from a set with a placeholder value."""
    return [replacement_val if word in name_set else word for word in word_lst]


def create_cleaned_textline_from_words(words):
    """Join a list of words back into a single line of text."""
    return ' '.join(words)


def line_cleaning_pipeline(text, stopwords_set, name_set, replace_val):
    """Apply the full sequence of cleaning steps to a single text line."""
    text_lc = lowercase_text(text)
    text_np = remove_punctuation(text_lc)
    text_nnl = remove_newline(text_np)
    words = split_text_into_words(text_nnl)
    words_nsw = remove_stopwords(words, stopwords_set)
    words_cleaned = replace_names(words_nsw, name_set, replace_val)
    return create_cleaned_textline_from_words(words_cleaned)


if __name__ == '__main__':
    stopwords = load_stopwords('data/stopwords.txt')
    names = {
        'seokwoo',
        'suan',
        'yonsuk',
        'seongkyeong',
        'ingil',
        'yonghuk',
        'jinhee'
    }
    replacement = 'person'

    text = "pregnant wife Seong-kyeong, a high school baseball team, rich-yet-egotistical"
    cleaned = line_cleaning_pipeline(text, stopwords, names, replacement)
    print(cleaned)