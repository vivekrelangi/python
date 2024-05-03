from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
a=queue.popleft()
b=queue.popleft()
print(queue," ",a," ",b)