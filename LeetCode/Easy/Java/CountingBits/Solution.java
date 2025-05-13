// https://leetcode.com/problems/counting-bits/description/

class Solution {
    public int[] countBits(int n) {
        int[] output = new int[n + 1];
        for (int i = 0; i < output.length; i++) {
            output[i] = countZeros(i);
        }
        return output;
    }

    public int countZeros(int n) {
        String binary = Integer.toBinaryString(n);
        int count = 0;
        for (int i = 0; i < binary.length(); i++) {
            if (binary.chatAt(i) == '1') {
                count++;
            }
        }
        return count;
    }
}
