from collections import deque
#empty deque
dq = deque([])
dq.append(1) #[1]
dq.append(2) #[1,2]
dq.append(3) #[1,2,3]
dq.append(4) #[1,2,3,4]
dq.append(5) #[1,2,3,4,5]

dq.popleft() #[2,3,4,5] pop 1
dq.popleft() #[3,4,5] pop 2
print(dq) #-> output [3,4,5]