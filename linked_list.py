class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    def __init__(self, asc=True):
        self._head = None
        self._tail = None
        if not asc: asc = -1
        self._asc = asc

    def insert(self, val):
        asc = self._asc

        # No Nodes in list
        if self._head is None:
            node = Node(val)
            self._head = node
            self._tail = node
            return

        # Node should exist before Head
        elif asc*val <= asc*self._head.val:
            self._head = Node(val, self._head) 

        # Node should exist after Tail
        elif asc*val >= asc*self._tail.val: 
            self._tail.nxt = Node(val)
            self._tail = self._tail.nxt

        # Node is in between
        else:
            nd = self._head
            while nd.nxt != None:
                if asc*nd.val <= asc*val <= asc*nd.nxt.val:
                    nd.nxt = Node(val, nd.nxt)
                    return
                nd = nd.nxt

    def remove(self, val):
        if self._head is None: return False
        elif self._head.val is val:
            if self._head.nxt is not None:
                self._head = self._head.nxt
            else:
                self._head = self._tail = None
            return True
        else:
            prev = self._head
            nd = self._head.nxt
            while (nd is not None):
                if nd.val is val:
                    prev.nxt = nd.nxt
                    if nd.nxt is None:
                        self._tail = prev
                    return True
                prev = nd
                nd = nd.nxt
            return False
    def pop(self):
        head = False
        if self._head is not None:
            head = self._head.val
            if self._head.nxt is not None:
                self._head = self._head.nxt
            else:
                self._head = self._tail = None
        return head
    
    def print_list(self):
        nd = self._head
        print("[", end="")
        while nd != None:
            print(nd.val, end="")
            if nd.nxt != None:
                print(", ", end="")
            nd = nd.nxt
        print("]")

