def reverse_upper(text: str):
    """
    Examples:
        >>> # Basic usage.
        >>> reverse_upper('how is it?')
        '?TI SI WOH'

    :param text: text
    :type text: str
    :return: same text reversed and in upper letters
    :rtype: str
    """
    return text[::-1].upper()
