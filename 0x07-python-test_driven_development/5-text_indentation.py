#!/usr/bin/python3
"""

A Module composed if function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ A function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        Nothing

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for f in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + f if s is "" else s + "\n\n" + i + f

    print(s[:-3], end="")
