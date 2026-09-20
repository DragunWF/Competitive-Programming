class Solution {
    public Boolean hasDupes(List<Integer> nums){
        return new Set<Integer>(nums).size() != nums.size();
    }
}