/*
 * For your reference:
 *
 * DoublyLinkedListNode {
 *     int data;
 *     DoublyLinkedListNode next;
 *     DoublyLinkedListNode prev;
 * }
 *
 */

function sortedInsert(head, data) {
    const newNode = new DoublyLinkedListNode(data);
    // what if head is null
    if (head === null) {
      return newNode;
    }
    // if it should be inserted at the front, handle that case
    if (data <= head.data) {
      newNode.next = head;
      head.prev = newNode;
      return newNode;
    }
      // new.n = head
      // head.p = new
      // return new
    
    let current = head;
    while (current !== null) {
      if (current.data > data) {
        newNode.prev = current.prev;
        newNode.next = current;
        current.prev.next = newNode;
        current.prev = newNode;
        return head;
      }
      if (current.next == null) {
        break;
      }
      current = current.next;
    }
    
    current.next = newNode;
    newNode.prev = current;
    
    return head;
    // the list is sorted already
    // go through the list and check if data is < > the item in the LL
      // if data is > , then go to the next node
      // if data is < , then we insert it before our current node
        // insertion
  
    // if we get to the end without inserting our node, then we want to insert it at the end
  
    // edge cases
      // what if the data is less than the head?
      // what if we need to insert it at the very end of the LL
  }