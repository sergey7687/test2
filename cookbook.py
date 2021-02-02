import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
p = q.pop()
print(p)

from collections import defaultdict, OrderedDict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(2)
print(d)

d = {
'a' : [1, 2, 3],
'b' : [4, 5],
'c' : [4, 7, 6]
}

for k, v in d.items():
    print(k, v)


b = OrderedDict()
b['foo'] = 1
b['bar'] = 2
b['spam'] = 3
b['grok'] = 4

for key in b:
    print(key, b[key])


a = [1, 5, 2, 1, 9, 1, 5, 10]
for i in a:
    if i not in [3]:
        print(i)

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(dedupe(a))
for i in dedupe(a):
    print(i)