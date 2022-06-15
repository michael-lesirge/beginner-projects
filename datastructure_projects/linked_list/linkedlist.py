from linked_list import Node
from typing import Iterable


class LinkedList:
    __slots__ = ["head", "tail", "len"]

    def __init__(self, iterable: Iterable = None) -> None:
        self.head = self.tail = self.len = None
        self.clear()
        if iterable:
            self.extend(iterable)

    def append(self, _object, /) -> None:
        """
        Append object to end of LinkedList.
        """
        new = Node(_object)
        if self.is_empty():
            self.head = new
        else:
            self.tail.next = new
        self.tail = new
        self.len += 1

    def prepend(self, _object, /) -> None:
        """
        Prepend object to front of LinkedList.
        """
        self.head = Node(_object, self.head)
        self.len += 1

    def extend(self, iterable: Iterable, /) -> None:
        """
        extend LinkedList by appending elem from iterable.
        """
        for elem in iterable:
            self.append(elem)

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def copy(self) -> "LinkedList":
        """
        Return a copy of the list.
        """
        copy = LinkedList()
        copy.extend(self)
        return copy

    def count(self, value, /) -> int:
        """
        Return number of occurrences of value.
        """
        count = 0
        for item in self:
            count += (value == item)
        return count

    def display(self) -> str:
        nodes = []
        current = self.head

        while current is not None:
            if current is self.head:
                nodes.append("[Head: %s]" % str(current.data))
            elif current is self.tail:
                nodes.append("[Tail: %s]" % str(current.data))
            else:
                nodes.append("[%s]" % str(current.data))

            current = current.next

        return " -> ".join(nodes)

    def display_nodes(self) -> str:
        return repr(self.head)

    def index(self, value, /) -> int:
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        for index, item in enumerate(self):
            if value == item:
                return index
        raise ValueError(f"{value} is not in LinkedList")

    def insert(self, index, _object, /) -> None:
        """
        Insert object before index.
        """
        if index < 0:
            index += len(self)

        if index <= 0:
            self.prepend(_object)
        elif index >= len(self):
            self.append(_object)
        else:
            current = self.head
            previous = None
            for _ in range(index):
                previous = current
                current = current.next
            new = Node(_object, current)
            previous.next = new
            self.len += 1

    def is_empty(self) -> bool:
        return self.head is None

    def pop(self, index=-1, /):
        """
        Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range.
        """
        if index is None:
            index = len(self) - 1
        elif index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("pop " + ("index out of range", "from empty list")[self.is_empty()])

        if index == 0:
            val = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            previous = None
            for _ in range(index):
                previous = current
                current = current.next
            val = current.data
            previous.next = current.next
        self.len -= 1
        return val

    def remove(self, value, /) -> None:
        current = self.head
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next

        if current is None:
            raise ValueError(f"{value} not in LinkedList")

        if previous is None:
            self.head = self.head.next
        else:
            previous.next = current.next

        self.len -= 1

    def reverse(self) -> None:
        reversed_self = reversed(self)
        self.head, self.tail = reversed_self.head, reversed_self.tail

    # def sort(self, *, key=None, reverse: bool =False) -> None:
    #     pass

    def __add__(self, other):
        if isinstance(other, LinkedList):
            new = self.copy()
            new.extend(other)
            return new
        raise TypeError(f"can only concatenate LinkedList (not '{type(other).__name__}') to LinkedList")

    def __iadd__(self, other):
        if isinstance(other, LinkedList):
            self.extend(other)
            return self
        raise TypeError(f"can only concatenate LinkedList (not '{type(other).__name__}') to LinkedList")

    def __mul__(self, other: int):
        if isinstance(other, int):
            new = LinkedList()
            for i in range(other):
                new.extend(self)
            return new
        raise TypeError(f"can't multiply LinkedList by non-int of type '{type(other).__name__}'")

    def __rmul__(self, other: int):
        return self * other

    def __bool__(self) -> bool:
        return self.head is not None

    def __contains__(self, value) -> bool:
        for item in self:
            if item == value:
                return True
        return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        for item, other_item in zip(self, other):
            if item != other_item:
                return False
        return True

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return True
        if len(self) != len(other):
            return True
        for item, other_item in zip(self, other):
            if item != other_item:
                return True
        return False

    def __getitem__(self, key):
        if isinstance(key, int):
            if key < 0:
                key += len(self)
            if key < 0 or key >= len(self):
                raise IndexError("LinkedList index out of range")

            if key == len(self) - 1:
                return self.tail.data

            current = self.head
            for _ in range(key):
                current = current.next
            return current.data

        elif isinstance(key, slice):
            start, stop, step = key.start, key.stop, key.step

            start = 0 if (start is None) else start
            stop = len(self) if (stop is None) else stop
            step = 1 if (step is None) else step

            if start < 0:
                start += len(self)
            if stop < 0:
                stop += len(self)

            if step == 0:
                raise ValueError("slice step cannot be zero")
            elif step < 0:
                raise ValueError("reverse slice not implemented")

            start = max(start, 0)
            stop = min(stop, len(self))

            new = LinkedList()
            current = self.head
            for _ in range(start):
                current = current.next
            for _ in range(start, stop, step):
                new.append(current.data)
                for _ in range(step):
                    current = current.next
                    if current is None:
                        return new
            return new

        return NotImplemented

    def __setitem__(self, key, data):
        if key < 0:
            key += len(self)
        if key < 0 or key >= len(self):
            raise IndexError("LinkedList index out of range")

        if key == len(self) - 1:
            self.tail.data = data

        current = self.head
        for _ in range(key):
            current = current.next
        current.data = data

    def __delitem__(self, key):
        if key < 0:
            key += len(self)
        if key < 0 or key >= len(self):
            raise IndexError("LinkedList index out of range")

        if key == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(key - 1):
                current = current.next
            current.next = current.next.next

        self.len -= 1

    def __reversed__(self) -> "LinkedList":
        new = LinkedList()
        for data in self:
            new.prepend(data)
        return new

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self) -> int:
        return self.len

    def __repr__(self) -> str:
        return "[" + ", ".join(map(repr, self)) + "]"

    def __str__(self) -> str:
        return "[" + ", ".join(map(str, self)) + "]"
