# ============================================================
# Min-Heap Implementation (for FIFO Queue)
# ============================================================


class MinHeap:
    """Min-heap implementation for priority queue"""

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def min_heapify(self, i):
        """Maintain min-heap property at index i"""
        l = self.left(i)
        r = self.right(i)
        smallest = i

        if l < len(self.heap) and self.heap[l][0] < self.heap[smallest][0]:
            smallest = l
        if r < len(self.heap) and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r

        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def insert(self, priority, value):
        """Insert element with given priority"""
        self.heap.append((priority, value))
        i = len(self.heap) - 1

        # Bubble up to maintain heap property
        while i > 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_min(self):
        """Remove and return element with minimum priority"""
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.min_heapify(0)

        return min_item

    def is_empty(self):
        return len(self.heap) == 0


# ============================================================
# Max-Heap Implementation (for LIFO Stack)
# ============================================================


class MaxHeap:
    """Max-heap implementation for priority queue"""

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def max_heapify(self, i):
        """Maintain max-heap property at index i"""
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l < len(self.heap) and self.heap[l][0] > self.heap[largest][0]:
            largest = l
        if r < len(self.heap) and self.heap[r][0] > self.heap[largest][0]:
            largest = r

        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)

    def insert(self, priority, value):
        """Insert element with given priority"""
        self.heap.append((priority, value))
        i = len(self.heap) - 1

        # Bubble up to maintain heap property
        while i > 0 and self.heap[self.parent(i)][0] < self.heap[i][0]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_max(self):
        """Remove and return element with maximum priority"""
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.max_heapify(0)

        return max_item

    def is_empty(self):
        return len(self.heap) == 0


# ============================================================
# Priority Queue-Based FIFO Queue
# ============================================================


class PriorityQueue:
    """FIFO Queue implemented using a min-priority queue"""

    def __init__(self):
        self.min_heap = MinHeap()
        self.priority = 0

    def enqueue(self, value):
        """Add element to the back of the queue"""
        self.priority += 1
        self.min_heap.insert(self.priority, value)
        print("  Enqueued '" + str(value) + "' with priority " + str(self.priority))

    def dequeue(self):
        """Remove and return element from the front of the queue"""
        if self.min_heap.is_empty():
            return None
        priority, value = self.min_heap.extract_min()
        print("  Dequeued '" + str(value) + "' (priority " + str(priority) + ")")
        return value

    def is_empty(self):
        return self.min_heap.is_empty()


# ============================================================
# Priority Queue-Based LIFO Stack
# ============================================================


class PriorityStack:
    """LIFO Stack implemented using a max-priority queue"""

    def __init__(self):
        self.max_heap = MaxHeap()
        self.priority = 0

    def push(self, value):
        """Add element to the top of the stack"""
        self.priority += 1
        self.max_heap.insert(self.priority, value)
        print("  Pushed '" + str(value) + "' with priority " + str(self.priority))

    def pop(self):
        """Remove and return element from the top of the stack"""
        if self.max_heap.is_empty():
            return None
        priority, value = self.max_heap.extract_max()
        print("  Popped '" + str(value) + "' (priority " + str(priority) + ")")
        return value

    def is_empty(self):
        return self.max_heap.is_empty()


# ============================================================
# Demonstration
# ============================================================

print("=" * 60)
print("FIFO Queue using Priority Queue (Min-Heap)")
print("=" * 60)

q = PriorityQueue()

print("\nEnqueuing elements: A, B, C, D")
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")

print("\nDequeuing all elements (should be: A, B, C, D)")
while not q.is_empty():
    q.dequeue()

print("\n" + "=" * 60)
print("LIFO Stack using Priority Queue (Max-Heap)")
print("=" * 60)

s = PriorityStack()

print("\nPushing elements: A, B, C, D")
s.push("A")
s.push("B")
s.push("C")
s.push("D")

print("\nPopping all elements (should be: D, C, B, A)")
while not s.is_empty():
    s.pop()
