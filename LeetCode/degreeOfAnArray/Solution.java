/**
* Given a non-empty array of non-negative integers nums, 
* the degree of this array is defined as the maximum frequency of any one of its elements.
* Input: [1, 2, 2, 3, 1] Output: 2
* Explanation: 
* The input array has a degree of 2 because both elements 1 and 2 appear twice.
* Of the subarrays that have the same degree:
* [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
* The shortest length is 2. So return 2.
* Answer
* The sub array must be atleast degree length.. cause at best the most frequent element
* occur next to each other..[1,4,0,0,0,0,5] [0,0,0,0] is the min length.. 
* or [1,0,4,0,0,0,5]..though 4 is the min possible length, this time it is unfortunately 5 [0,4,0,0,0]
* For each element in the given array, we store, the index of its first occurrence in a map; 
* and the index of its last occurrence in another map. For example, with nums = [1,2,3,2,5] we have first[2] = 1 and last[2] = 3.
* Then,for each element x that occurs the degree times, 
* first[x] - last[x] + 1 will be our candidate answer, and we'll take the minimum of those candidates.
*/

class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer, Integer> first = new HashMap<>(), last = new HashMap<>(), count = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            if(first.get(nums[i])==null)
                first.put(nums[i],i);
            last.put(nums[i],i+1);
            count.put(nums[i],count.getOrDefault(nums[i],0)+1);
        }
        int degree = Collections.max(count.values());
        int ans = Integer.MAX_VALUE;
        for(int n: count.keySet()){
            if(count.get(n) == degree){
                ans = Math.min(ans, last.get(n)-first.get(n));
            }
        }
        
        return ans;
    }
}