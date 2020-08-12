def lca(root, v1, v2):
      # set our current node
  current = root
  
  # while current != null
  while current != None:
    if (v1 <= current.info and v2 >= current.info) or (v2 <= current.info and v1 >= current.info):
      return current
        # base case -> 
      # one value is on one side, the other is on the other side OR it's equal to it
        # we've found the lca
    
    if (v1 < current.info and v2 < current.info):
      current = current.left
    # how do we know if we want to go left?
    # if the both value are less than our node, then move left
    
    if (v1 > current.info and v2 > current.info):
      current = current.right
    # we got right if
    # both values are greater than our node


    