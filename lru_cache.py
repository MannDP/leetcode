from typing import List


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy_head = Node(-1)
        self.dummy_tail = Node(-1)
        self.node_ptrs = {}

        # link up dummy nodes
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.node_ptrs:
            return -1
        node = self.node_ptrs[key]
        self.move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if node exists
        if key in self.node_ptrs:
            node = self.node_ptrs[key]
            self.move_to_front(node)
            node.val = value
            return
        
        new_node = Node(key=key, val=value)
        if len(self.node_ptrs) == self.capacity:
            # evict from the tail
            evict_node = self.dummy_tail.prev
            evict_node.prev.next = self.dummy_tail
            self.dummy_tail.prev = evict_node.prev
            self.node_ptrs.pop(evict_node.key)
        self.node_ptrs[key] = new_node
        self.move_to_front(new_node)


    def move_to_front(self, n: Node) -> None:
        n_prev, n_next = n.prev, n.next
        # remove from current spot
        if n_prev:
            n_prev.next = n_next
        if n_next:
            n_next.prev = n_prev

        # insert at head
        n.next = self.dummy_head.next
        n.prev = self.dummy_head
        self.dummy_head.next.prev = n
        self.dummy_head.next = n
