# hashtag
Test project to index words in files

# Installation and requirements

Python 3.6

```
pip3 install -r requirements.txt
```

to install NLTK [resources](https://www.nltk.org/data.html):
```
python3 -m nltk.downloader all
```

# Usage

to index files use:
```
python3 index.py docs/doc4.txt
python3 index.py docs/doc3.txt
```

to combine results use:
```
python3 combine.py docs/doc1.txt.idx docs/doc2.txt.idx docs/doc3.txt.idx docs/doc4.txt.idx docs/doc5.txt.idx docs/doc6.txt.idx
```

to display stats use:
```
python stats.py output.idx
```

detailed stats:
```
python stats.py -d output.idx
```

# Links
(https://nlpforhackers.io/splitting-text-into-sentences/)
(https://en.wikipedia.org/wiki/Search_engine_indexing)
