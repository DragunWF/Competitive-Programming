class Solution {
    public Integer findSmallest(List<Integer> nums){
        Integer minNum = nums[0];
        for (Integer i = 1; i < nums.size(); i++) {
            if (nums[i] < minNum) {
                minNum = nums[i];
            }
        }
        return minNum;
    }
}