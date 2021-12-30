from typing import Optional


class Node:
    def __init__(self, item, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer: Optional["Node"] = pointer


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        else:
            pass


class Stack(LinkedList):
    def push(self, item) -> Optional[Node]:
        self.last: Optional[Node] = Node(item, self.last)

    def pop(self) -> T:
        item = self.last.item
        self.pointer: Optional[Node] = self.last.pointer
        return item
