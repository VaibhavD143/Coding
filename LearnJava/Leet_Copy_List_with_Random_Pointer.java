/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        
        Node node = head;
        
        while (node != null) {
            Node dup = new Node(node.val);
            
            dup.next = node.next;
            node.next = dup;
            
            node = dup.next;
        }
        
        node = head;
        Node dnode = null;
        while (node != null) {
            dnode = node.next;
            if (node.random != null) {
                dnode.random = node.random.next;
            }
            
            node = dnode.next;
        }
        
        node = head;
        dnode = node.next;
        Node newRoot = node.next;
        while (dnode.next != null) {
            dnode = node.next;
            node.next = dnode.next;
            dnode.next = dnode.next.next;
            
            node = node.next;
            dnode = dnode.next;
        }
        node.next = null;
        return newRoot;
    }
}