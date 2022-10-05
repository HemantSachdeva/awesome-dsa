class Solution {
    public int trap(int[] arr) {
        return solve(arr);
    }
    
    // Two pointers approach
	// INTUITION - 
	// 1. At each step, update left max height and right max height.
	// 2. How much water can we get at each step? -> Min(leftMax, rightMax) - current height
    
	int solve(int[] arr) {
		int l = 0, r = arr.length - 1, sum = 0, lMax = 0, rMax = 0;
        while(l <= r){
            lMax = Math.max(arr[l], lMax);
            rMax = Math.max(arr[r], rMax);
			
            if(lMax < rMax){
                sum += lMax - arr[l++];
            }else{
                sum += rMax - arr[r--];
            }
        }
        return sum;
	}
}