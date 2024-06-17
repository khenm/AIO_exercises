"""classfication -- fi score calculation function"""


def calc_f1_score(tp, fp, fn):
    """ Function to determine the classification model
    by calculating f1-score from precision and recall.  
    """
    # parameters condition
    # all parameters' type must be integer
    # otherwise, end function
    if not isinstance(tp, int):
        print("tp must be int")
        return
    if not isinstance(fp, int):
        print("fp must be int")
        return
    if not isinstance(fn, int):
        print("fn must be int")
        return
    # all parameters must be greater than zero
    # otherwise, end function
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    # computing precision, recall and f1 score
    precision: float = tp / (tp + fp)
    recall: float = tp / (tp + fn)
    f1_score: float = 2 * (precision * recall) / (precision + recall)
    print('Precision is ', precision)
    print('Recall is ', recall)
    print('f1-score is ', f1_score)


def main():
    calc_f1_score(tp=2, fp=4, fn=3)


if __name__ == "__main__":
    main()
