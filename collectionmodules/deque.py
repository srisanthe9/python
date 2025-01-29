#deque pronounced as deck is an optimised list to perform insertion and deletion easily.
from collections import deque
a=deque([10,20,30,'s','r','ram'])
a.append('srisanth')#adds srisanth at right end my list
a.appendleft('sridhar')#adds sridhar at left end my list
a.pop()#removes srisanth from my list
a.popleft()#removes sridhar from my list
print(a)