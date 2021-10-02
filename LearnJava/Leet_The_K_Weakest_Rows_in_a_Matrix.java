class Solution {
    
    public int[] kWeakestRows(int[][] mat, int k) {
        Queue<int[]> pq = new PriorityQueue<>(new MyComp());
        int c = 0;
        for (int i = 0; i < mat.length; i++) {
            c = 0;
            for (int j = 0; j < mat[0].length && mat[i][j] == 1; j++) {
                c++;
            }
            pq.offer(new int[]{c,i});
        }
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = pq.poll()[1];
        }
        return res;
    }
}

public class MyComp implements Comparator<int[]> {
    public int compare(int[] a, int[] b) {
        if (a[0] != b[0]) {
            return a[0] - b[0];
        }
        return a[1] - b[1];
    }
}