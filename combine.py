import sys
import argparse
import logging

from myindex.indexer import Indexer


def main():
    parser = argparse.ArgumentParser(description='Combine indexes and build final statistic')
    parser.add_argument('filenames', metavar='N', nargs='+', type=str, help='filenames')
    args = parser.parse_args()

    main_index = Indexer()
    for filename in args.filenames:
        indexer = Indexer()
        indexer.load(filename)
        main_index.add(indexer)
        logging.info('loaded %s from %s', len(indexer.tags), filename)
    main_index.save('output.idx')


if __name__ == '__main__':
    sys.exit(main())
