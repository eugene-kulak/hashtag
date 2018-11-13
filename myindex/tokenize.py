from nltk import sent_tokenize, word_tokenize


class Tokenizer:
    def __init__(self, language='english'):
        self.lang = language

    def get_sentences(self, content):
        return sent_tokenize(content, language=self.lang)

    def get_words(self, content, filter):
        return word_tokenize(content, language=self.lang, preserve_line=True)
