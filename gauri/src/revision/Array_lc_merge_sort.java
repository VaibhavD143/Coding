package revision;
//https://leetcode.com/problems/sort-an-array/submissions/

public class Array_lc_merge_sort {

    public int[] sortArray(int[] nums) {
        innerSortArray(nums,0, nums.length-1);
        return nums;
    }

    public void innerSortArray(int arr[],int l, int r){
        if(l<r){
            int m= (l+r)/2;
            innerSortArray(arr, l, m);
            innerSortArray(arr, m+1, r);
            merge(arr, l, r, m);
        }
    }

    public void merge(int arr[], int l, int r, int m){
        // System.out.println(Arrays.toString(arr));
        if(l==r)
            return;
        // System.out.println(l+""+ r+""+m);
        int l1= m-l+1;
        int l2= r-m;
        int arr1[] = new int[l1];
        int arr2[]= new int[l2];
        int a=0, b= 0, k=l;
        for (int i=0; i<l1; ++i) {
            arr1[i]= arr[i+l];
        }

        for (int i=0; i<l2; ++i) {
            arr2[i]= arr[i+m+1];
        }
        // System.out.println(Arrays.toString(arr1));
        // System.out.println(Arrays.toString(arr2));

        while(a<l1 && b<l2){
            if(arr1[a]<=arr2[b])
                arr[k++]= arr1[a++];
            else
                arr[k++]=arr2[b++];
        }
        while(a<l1)
            arr[k++]=arr1[a++];
        while(b<l2)
            arr[k++]= arr2[b++];
    }

}