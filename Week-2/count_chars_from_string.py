def count_chars_from_string(string: str):
    """Count the number of characters in a string,

    Args:
        string (str): a word to be split
    """
    # initialize the dictionary
    char_dict: dict = {}

    # counting characters in string
    n: int = len(string)
    for i in range(n):
        if string[i] not in char_dict:
            char_dict[string[i]] = 0
        char_dict[string[i]] += 1
    print(char_dict)


def main():
    string: str = 'Perpendicular'
    count_chars_from_string(string=string)


if __name__ == '__main__':
    main()
