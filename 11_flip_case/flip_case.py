def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_lowered = to_swap.casefold()
    output = ""
    for char in phrase:
        if char.casefold() == to_swap_lowered:
            output+= char.swapcase()
        else:
            output+=char
    return output