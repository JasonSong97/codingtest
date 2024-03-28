/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode fast = head;
        
        while (n > 0 && fast.next != null) {
            fast = fast.next;
            n--;
        }
        
        ListNode slow = head;
        ListNode pre = head;
        
        while (fast != null) {
            pre = slow;
            slow = slow.next;
            fast = fast.next;
        }
        
        pre.next = slow.next;
        
        if (slow == pre) {
            head = head.next;
            return head;
        }
        else {
            return head;
        }
    } 
}