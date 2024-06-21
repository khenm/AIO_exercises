import torch
from torch import nn
from math import exp


class Softmax(nn.Module):
    def __init__(self, data=[]):
        super().__init__()

    def __call__(self, data) -> list[float]:
        """softmax function on the input list
        and return the array after the process.
        Args: 
            data (): data list
        Returns:
            list[float]: softmax list
        """
        self._data = data
        softmax_list: list[float] = []
        n: int = len(data)
        # calculate each softmax
        for i in range(n):
            softmax_list.append(exp(data[i]))

        # divide each number by the sum
        softmax_sum = sum(softmax_list)
        for i in range(n):
            softmax_list[i] = round(softmax_list[i] / softmax_sum, ndigits=5)
        return softmax_list


class softmax_stable(nn.Module):
    def __init__(self, data=[]):
        super().__init__()

    def __call__(self, data) -> list[float]:
        """Softmax stable function on the input list 
        and return the list after the process.

        Args:
            data (): data list

        Returns:
            list[float]: softmax stable list
        """
        self._data = data
        softmaxstable_list: list[float] = []
        n: int = len(data)
        # get max from the data
        max_value = max(data)
        # calculate each softmax stable
        for i in range(n):
            softmaxstable_list.append(exp(data[i] - max_value))

        # divide each number by the sum
        softmaxstable_sum = sum(softmaxstable_list)
        for i in range(n):
            softmaxstable_list[i] = round(
                softmaxstable_list[i] / softmaxstable_sum, ndigits=5)
        return softmaxstable_list


def main():
    data = torch.Tensor([1, 2, 3])
    print(f'Data: {data}')
    softmax = Softmax()
    softmax_output = softmax(data=data)
    print(f'Softmax output: {softmax_output}')

    softmax_stable_list = softmax_stable()
    stable_output = softmax_stable_list(data=data)
    print(f'Softmax stable output: {stable_output}')


if __name__ == '__main__':
    main()
