class Queue:
    __size = 0
    __queue = []

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

    def dequeue(self):
        """Remove the first element from the top of 
        the queue

        Returns:
            int: recently removed element
        """
        if (self.is_empty()):
            return -1
        removed_element = self.__queue[0]
        del self.__queue[0]
        self.__size -= 1
        return removed_element

    def enqueue(self, value):
        """Add the element to the end of the queue

        Args:
            value (int)
        """
        self.__queue.append(value)
        self.__size += 1

    def front(self) -> int:
        """Getting the first element without removing it

        Returns:
            int: the top element
        """
        return self.__queue[0]


def main():
    queue = Queue(capacity=5)
    queue.enqueue(1)
    queue.enqueue(2)
    print(f'Full: {queue.is_full()}')
    print(f'Front: {queue.front()}')
    print(f'Dequeue: {queue.dequeue()}')
    print(f'Front: {queue.front()}')
    print(f'Dequeue: {queue.dequeue()}')
    print(f'Empty: {queue.is_empty()}')


if __name__ == '__main__':
    main()
