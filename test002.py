class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        # 创建一个虚拟头节点和虚拟尾节点
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 移动节点到链表头部
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    # 移除链表中的某个节点
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    # 将节点添加到链表头部
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 删除链表尾部节点
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 将该节点移动到链表头部
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # 将该节点移动到链表头部
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                # 删除链表尾部节点（即最久未使用的节点）
                tail = self._pop_tail()
                del self.cache[tail.key]

# 测试代码
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       # 返回 1
cache.put(3, 3)           # 删除键 2
print(cache.get(2))       # 返回 -1（未找到）
cache.put(4, 4)           # 删除键 1
print(cache.get(1))       # 返回 -1（未找到）
print(cache.get(3))       # 返回 3
print(cache.get(4))       # 返回 4
