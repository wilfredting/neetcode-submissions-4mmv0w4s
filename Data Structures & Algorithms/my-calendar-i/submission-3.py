class Node:
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.is_booked = False  # True if ANY interval inside [l, r] is booked
        self.lazy = False       # True if the ENTIRE interval [l, r] is booked
        self.left = None
        self.right = None

class MyCalendar:

    def __init__(self):
        self.root = Node(0, 10**9)

    def _push(self, node: Node):
        mid = (node.l + node.r) // 2
        if not node.left:
            node.left = Node(node.l, mid)
        if not node.right:
            node.right = Node(mid + 1, node.r)
            
        if node.lazy:
            node.left.is_booked = True
            node.left.lazy = True
            node.right.is_booked = True
            node.right.lazy = True
            node.lazy = False

    def _has_overlap(self, node: Node, ql: int, qr: int) -> bool:
        # No overlap with this node's range
        if ql > node.r or qr < node.l:
            return False
            
        # If this node has no bookings at all in its entire range
        if not node.is_booked:
            return False

        # If the entire node is lazy-booked, or if query fully covers a booked node
        if node.lazy or (ql <= node.l and node.r <= qr):
            return node.is_booked

        self._push(node)
        mid = (node.l + node.r) // 2
        
        res = False
        if ql <= mid:
            res = res or self._has_overlap(node.left, ql, qr)
        if qr > mid:
            res = res or self._has_overlap(node.right, ql, qr)
        return res

    def _update(self, node: Node, ql: int, qr: int):
        if ql <= node.l and node.r <= qr:
            node.is_booked = True
            node.lazy = True
            return

        self._push(node)
        mid = (node.l + node.r) // 2

        if ql <= mid:
            self._update(node.left, ql, qr)
        if qr > mid:
            self._update(node.right, ql, qr)

        node.is_booked = node.left.is_booked or node.right.is_booked

    def book(self, startTime: int, endTime: int) -> bool:
        if self._has_overlap(self.root, startTime, endTime - 1):
            return False
        
        self._update(self.root, startTime, endTime - 1)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)