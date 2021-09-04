def breadth_first_traversal(tree):
    traversal = []
    queue = []
    pointer = 0
    current = tree[0]
    queue.append(current)

    while(len(traversal) < len(tree)-1):
      traversal.append(current[0])
      exist = False
      for x in range(0, len(current[1])):
        for y in range(0, len(queue)):
          if(tree[current[1][x]] == queue[y]):
            exist = True
        if(exist == False):
          queue.append(tree[current[1][x]])
        exist = False
      pointer += 1
      current = queue[pointer]
    traversal.append(current[0])
    return traversal

    

def pre_order_traversal(tree):
  traversal=[]
  stack = [None]*len(tree)
  top = 0
  current = tree[0]
  stack.append(current)

  while(len(traversal) < len(tree)-1):
    traversal.append(current[0])
    exist = False
    for x in range(len(current[1])-1, -1, -1):
      for y in range(0, len(stack)):
        if(tree[current[1][x]]== stack[y]):
          exist = True
      if(exist == False):
        top += 1
        stack[top] = tree[current[1][x]]
      exist = False
    
    current = stack[top]
    top -= 1
  traversal.append(current[0])
  return traversal

  
def in_order_traversal(tree):
    traversal = []
    top = -1
    stack = [None]*len(tree)
    current = tree[0]

    while(top != -1 or current != None):
      if(current != None):
        top += 1
        stack[top] = current
        if(len(current[1]) > 0):
          current = tree[current[1][0]]
        else:
          current = None
          
      else:
        current = stack[top]
        top -= 1
        traversal.append(current[0])

        if(len(current[1]) > 2):
          for x in range(2, len(current[1])):
            top += 1
            stack[top] = tree[current[1][x]]

        if(len(current[1]) > 1):
          current = tree[current[1][1]]
        else:
          current = None
    return traversal


def post_order_traversal(tree):
  traversal = []
  stack = [None]*len(tree)
  top = 0
  counter = 0
  stack[top] = (tree[0])

  while(len(traversal) < len(tree)):
    current = stack[top]
    if(current == None):
      return counter
    counter += 1
    top -= 1
    traversal.append(current[0])
    
    for x in range(0, len(current[1])):
      top += 1
      stack[top] = (tree[current[1][x]])
      
  newArray = []
  for x in range(len(traversal)-1, -1, -1):
    newArray.append(traversal[x])

  return newArray