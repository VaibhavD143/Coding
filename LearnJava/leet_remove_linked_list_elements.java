/**
 * Definition for singly-linked list.
 * */
 class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode node = new ListNode(val-1,head);
        head = node;
        while(node.next != null){
            if(node.next.val == val){
                node.next = node.next.next;
            }
            else{
                node = node.next;
            }
        }
        return head.next;
    }
    
    public void print(ListNode head){
        while(head != null){
            System.out.print(head.val+" ");
            head = head.next;
        }
        System.out.println();
    }
    public static void main(String[] args) {
        ListNode head = new ListNode(2,new ListNode(3,new ListNode(5,new ListNode(3,new ListNode(6,null)))));

        Solution obj = new Solution();
        obj.print(head);
        obj.print(obj.removeElements(head, 3));

    }


}