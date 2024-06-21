class Stack:
    __size = 0
    __stack = []

    def __init__(self, capacity: int):
        self.__capacity = capacity

    def is_empty(self) -> bool:
        if self.__size == 0:
            return True
        return False

    def is_full(self) -> bool:
        if self.__size == self.__capacity:
            return True
        return False

    def pop(self) -> int:
        """Remove the first element from the top of 
        the stack

        Returns:
            int: recently removed element
        """
        if (self.is_empty()):
            return -1
        removed_element = self.__stack[0]
        del self.__stack[0]
        self.__size -= 1
        return removed_element

    def push(self, value: int):
        """Add the element to the start of the stack

        Args:
            value (int)
        """
        self.__stack.insert(0, value)
        self.__size += 1

    def top(self) -> int:
        """Getting the first element without removing it

        Returns:
            int: the top element
        """
        return self.__stack[0]

    def __len__(self):
        return self.__size


def main():
    stack = Stack(capacity=5)
    stack.push(1)
    stack.push(2)
    print(f'Full: {stack.is_full()}')
    print(f'Top element: {stack.top()}')
    print(f'After popped, removed element: {stack.pop()}')
    print(f'After popped, top: {stack.top()}')
    print(f'Removed element: {stack.pop()}')
    print(f'Empty: {stack.is_empty()}')


if __name__ == '__main__':
    main()
