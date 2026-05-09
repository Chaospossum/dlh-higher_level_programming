#!/usr/bin/python3
"""Returns the length of a sentence and its first character."""


def multiple_returns(sentence):
    """Return a tuple of (length, first character) of a sentence.

    If the sentence is empty, the first character is None.

    Args:
        sentence: The input string.

    Returns:
        A tuple of (length, first character).
    """
    first = sentence[0] if len(sentence) > 0 else None
    return (len(sentence), first)
