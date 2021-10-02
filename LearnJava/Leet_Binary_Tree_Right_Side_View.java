public class TreeNode {
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
    public List<Integer> rightSideView(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        rightSideViewUtil(root, 0, result);
        return result;
    }
    
    public void rightSideViewUtil(TreeNode node, int level, ArrayList<Integer> result) {
        if (node == null) {
            return;
        }
        
        if (level == result.size()) {
            result.add(node.val);
        }
//         else {
//             result.set(level, node.val);
//         }
        
        rightSideViewUtil(node.right, level+1, result);
        rightSideViewUtil(node.left, level+1, result);
        
    }
}