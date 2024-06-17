# modify your text file input
file_path = r'D:\AIO\Exercise--git\AIO-Exercises\Week-2\P1_data.txt'


def count_chars_from_input_file(file_path: str = file_path):
    """Count the number of characters in a string,

    Args:
        file_path (str): file to be split
    """
    # initialize the dictionary
    char_dict: dict = {}

    # counting characters in string
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                if word not in char_dict:
                    char_dict[word] = 0
                char_dict[word] += 1
        print(char_dict)


def main():
    count_chars_from_input_file()


if __name__ == '__main__':
    main()
