# https://vjudge.net/problem/UVA-11995

from sys import stdin
from collections import deque
from heapq import *

def check(is_stack, is_queue, is_priotiry_queue):
  if not is_stack and not is_priotiry_queue and not is_queue:
    print("impossible")
  elif is_stack and not is_priotiry_queue and not is_queue:
    print("stack")
  elif is_priotiry_queue and not is_stack and not is_queue:
    print("priority queue")
  elif is_queue and not is_stack and not is_priotiry_queue:
    print("queue")
  else:
    print("not sure")

def main():
  stack = [] 
  queue = deque() 
  priority_queue = [] 
  is_stack = is_queue = is_priotiry_queue = True
  cant_elements = 0
  
  n = int(input())
  for i in range(n):
    query = list(map(int, stdin.readline().strip().split()))
    if query[0] == 1:
      if is_stack:
        stack.append(query[1])
      if is_queue:
        queue.appendleft(query[1])
      if is_priotiry_queue:
        heappush(priority_queue, -query[1])
      cant_elements += 1
    elif query[0] == 2:
      if cant_elements == 0:
        is_priotiry_queue = is_queue = is_stack = False
      else:
        if is_priotiry_queue and heappop(priority_queue) != -query[1]:
          is_priotiry_queue = False
        if is_queue and queue.pop() != query[1]:
          is_queue = False
        if is_stack and stack.pop() != query[1]:
          is_stack = False
      cant_elements -= 1
  check(is_stack, is_queue, is_priotiry_queue)


while True:
  try:
    main()
  except(EOFError):
    break