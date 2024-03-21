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
    public ListNode partition(ListNode head, int x) {
        
        ListNode res = new ListNode(-1);
        ListNode pivot = new ListNode(x);
        ListNode resPos = res, pivotPos = pivot;
        
        ListNode pos = head;
        while(pos != null){
            if(pos.val < x){
                resPos.next = pos;
                resPos = resPos.next;
            } else {
                pivotPos.next = pos;
                pivotPos = pivotPos.next;
                pivotPos.next = null;
            }
            pos = pos.next;
        }
        
        resPos.next = pivot.next;
        
        return res.next;
    }
}