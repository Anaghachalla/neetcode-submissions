
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> hashset = new HashSet<>();
        for(int i : nums) {
            if(!hashset.add(i)) {
                return true;
            }
        }
        return false;
    }
}