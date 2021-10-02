import java.util.List;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Collections;
/**
 * Definition for a binary tree node.**/
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if(root == null) return new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        List<Integer> tmp = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        q.offer(root);
        q.offer(null);
        boolean dir = true;
        while(q.size()!=0){
            TreeNode node = q.poll();
            if(node == null){
                if(dir) {
                    res.add(tmp);
                    tmp= new ArrayList<>();
                }
                else{
                    Collections.reverse(tmp);
                    res.add(tmp);
                    tmp= new ArrayList<>();
                }
                if(q.size()!=0){
                    q.offer(null);
                }
                dir = !dir;
                continue;
            }
            tmp.add(node.val);
            if(node.left != null) q.offer(node.left);
            if(node.right != null) q.offer(node.right);
        }
        return res;
    }
}