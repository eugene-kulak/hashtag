import pickle


class Indexer:
    def __init__(self, source=None, serializer=pickle):
        self.serializer = serializer
        self.tags = {}
        # TODO
        self.source = source

    def index(self, content, tokenizer, skip):
        self.tags = {}
        for idx, sentence in enumerate(tokenizer.get_sentences(content)):
            words = tokenizer.get_words(sentence, skip)
            for word in words:
                # normalize
                key = word.lower()
                if key not in self.tags:
                    self.tags[key] = []
                self.tags[key].append(idx)
        return self.tags

    def save(self, filename):
        with open(filename, 'wb+') as f:
            f.write(self.serializer.dumps((self.source, self.tags)))

    def load(self, filename):
        with open(filename, 'rb') as f:
            (self.source, self.tags) = pickle.loads(f.read())

    def _transform_in_multisource(self):
        new_tags = {}
        for tag, occurrences in self.tags.items():
            if tag not in new_tags:
                new_tags[tag] = {}
            new_tags[tag][self.source] = occurrences
        self.tags = new_tags
        self.source = None

    def add(self, other_index):
        # upgrade this index to multi source index if needed
        if self.source is not None and self.source != other_index.source:
            self._transform_in_multisource()
        for tag, occurences in other_index.tags.items():
            if tag not in self.tags:
                self.tags[tag] = {}
            self.tags[tag][other_index.source] = occurences
