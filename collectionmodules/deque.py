#deque pronounced as deck is an optimised list to perform insertion and deletion easily.
from collections import deque
a=deque([10,20,30,'s','r','ram'])
a.append('srisanth')
a.appendleft('sridhar')
a.pop()
a.popleft()
print(a)