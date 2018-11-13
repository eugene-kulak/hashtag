import sys
import argparse

from myindex.content import get_content_by_offsets
from myindex.indexer import Indexer


def main():
    parser = argparse.ArgumentParser(description='Combine indexes and build final statistic')
    parser.add_argument('filename', type=str, help='filename of indexes')
    parser.add_argument('-t', '--top', type=int, default=10)
    parser.add_argument('-d', '--detailed', action='store_true')
    args = parser.parse_args()

    indexer = Indexer()
    indexer.load(args.filename)

    sorted_stats = sorted(indexer.tags.items(),
                          key=lambda x: sum([len(loc) for loc in x[1].values()]),
                          reverse=True)

    print_stats(sorted_stats[:args.top], detailed=args.detailed)


def print_stats(stats, detailed=False):
    for (tag, docs) in stats:
        print(tag)
        for filename, usages in docs.items():
            print('{} - {} occurrences'.format(filename, len(usages)))
            if detailed:
                print(get_content_by_offsets(filename, offsets=usages))


if __name__ == '__main__':
    sys.exit(main())
