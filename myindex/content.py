from .tokenize import Tokenizer


def get_content(uri):
    """ Responsible to decode file format and retrieve its content
    :param str uri:
    :return: str
    """
    with open(uri, 'r') as f:
        return f.read()


def get_content_by_offsets(uri, offsets):
    """ Special method that suppose to give us context of tag (i.e. sentence)
    :param str uri:
    :param list offsets: list of offsets (but in this case index of sentences)
    :return: str
    """
    # TODO: get info about original tokenizer or save context artifacts (start/end offsets in file)
    sentences = Tokenizer().get_sentences(get_content(uri))
    return [sentences[i] for i in offsets]
