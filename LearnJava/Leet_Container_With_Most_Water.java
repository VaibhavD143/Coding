class Solution {
    public int maxArea(int[] height) {
        int maxHeight = 3 * 10000 + 1;
        int encoded;
        int[] bitMax = new int[maxHeight + 1];
        // System.out.println(bitMax.length);
        int res = 0;
        for (int i = height.length - 1; i >= 0; i-- ) {
            encoded = -height[i] + maxHeight;
            // System.out.println(encoded);
            res = Math.max(res, height[i] * (getMax(bitMax, encoded) - i));
            updateMax(bitMax, encoded, i);
        }
        int[] bitMin = new int[maxHeight + 1];
        // System.out.println(bitMin.length);
        Arrays.fill(bitMin, height.length + 1 );
        for (int i = 0; i < height.length; i++) {
            encoded = -height[i] + maxHeight;
            // System.out.println((height[i] * (i - getMin(bitMin, encoded))) + " " + height[i] + " " + getMin(bitMin, encoded));
            // System.out.println(Arrays.toString(bitMin));
            res = Math.max(res, height[i] * (i - getMin(bitMin, encoded)));
            updateMin(bitMin, encoded, i);
        }
        return res;
    }
    
    public void updateMin(int[] bit, int ind, int value) {
        // ind += 1;
        while (ind < bit.length) {
            if (bit[ind] <= value) {
                break;
            }
            bit[ind] = value;
            ind += (ind & -ind);
        }
    }
    
    public int getMin(int[] bit, int ind) {
        // ind += 1;
        int res = Integer.MAX_VALUE;
        while (ind > 0) {
            res = Math.min(res, bit[ind]);
            ind -= (ind & -ind);
        }
        return res;
    }
    
    public void updateMax(int[] bit, int ind, int value) {
        // ind += 1;
        while (ind < bit.length) {
            if (bit[ind] >= value) {
                return;
            }
            bit[ind] = value;
            ind += (ind & -ind);
        }
    }
    
    public int getMax(int[] bit, int ind) {
        // ind += 1;
        int res = 0;
        while (ind > 0) {
            res = Math.max(res, bit[ind]);
            ind -= (ind & -ind);
        }
        return res;
    }
}

class Solution2 {
  public int maxArea(int[] height) {
      int res = 0;
      int l = 0;
      int r = height.length - 1;
      
      while (l < r) {
          res = Math.max(res, Math.min(height[l], height[r]) * (r - l));
          if (height[l] < height[r]) {
              l++;
          }
          else {
              r--;
          }
      }
      
      return res;
  }
  
}