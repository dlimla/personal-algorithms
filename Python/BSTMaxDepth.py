def height(root):
      # we could check all of the different paths, and find which one has the largest length
  # recursion -> depth first search
  return heightRecursive(root, 0)
    

def heightRecursive(node, currentHeight):
  # check if left is None and right is None
    # we've hit the end of this route, so return the height
  if node == None:
    return currentHeight - 1

  # to go left:
    # leftHeight = call our recursive function and pass in node.left and also the height
  return max(heightRecursive(node.left, currentHeight+1), heightRecursive(node.right, currentHeight+1))

  # to go right:
    # rightHeight = call our recursive function and pass in node.right and also the height
    
  # return the larger one
  # return max of left and right