class Node:
    __slots__ = ["data", "next"]
    def __init__(self, object=0, next_node: "Node" = None) -> None:
        self.data = object
        self.next = next_node

    def copy(self) -> "Node":
        return Node(self.data, self.next.copy() if self.next else None)

    def is_tail(self) -> bool:
        return self.next is None
    
    def __repr__(self) -> str:
        return f"Node(data={repr(self.data)}, next={repr(self.next)})"
