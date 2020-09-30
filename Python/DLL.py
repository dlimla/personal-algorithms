# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def sortedInsert(head, data):
  # create our newNode
  newNode = DoublyLinkedListNode(data)
  
  # what if head is null?
    # return newNode
  if head is None:
    return newNode
  
  # what if it needs to be inserted at the beginning?
  if head.data > newNode.data:
    # link the node onto the front of the list
    newNode.next = head
    head.prev = newNode
    # return newNode
    return newNode
    
  current = head
  # iterator over the LL,
  while current is not None:
    # check each node's data against the data we want to insert
    # when the node's data becomes greater than the toInsert data, 
    if current.data > newNode.data:
      # we want to insert the node before
      newNode.prev = current.prev
      newNode.next = current
      current.prev = newNode
      newNode.prev.next = newNode
      # return head
      return head
    
    
    # if we get to a point where next is null, then this means we need to insert it at the end
    if current.next is None:
      current.next = newNode
      newNode.prev = current
      return head
      # curr.next = newNode
      # newNode.prev = curr
      
    current = current.next
      
  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      