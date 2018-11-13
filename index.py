# https://nlpforhackers.io/splitting-text-into-sentences/
# https://en.wikipedia.org/wiki/Search_engine_indexing

import sys
import argparse
import string

from myindex.indexer import Indexer
from myindex.content import get_content
from myindex.tokenize import Tokenizer


def main():
    parser = argparse.ArgumentParser(description='Load file and tokenize tags')
    parser.add_argument('filename', type=str, help='filename to process')
    parser.add_argument('-f', '--filter', type=str, default=string.punctuation)
    parser.add_argument('-l', '--language', type=str, default='english')
    parser.add_argument('-o', '--output', type=str, help='output filename')
    args = parser.parse_args()

    tokenizer = Tokenizer(language=args.language)
    content = get_content(args.filename)
    indexer = Indexer(args.filename)
    indexer.index(content, tokenizer, skip=args.filter)
    indexer.save(args.filename + '.idx')


if __name__ == '__main__':
    sys.exit(main())
