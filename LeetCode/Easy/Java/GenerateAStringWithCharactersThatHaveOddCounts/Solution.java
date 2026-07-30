// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution {
    public String generateTheString(int n) {
        return switch (n) {
            case 1 -> "a";
            case 2 -> "ab";
            default -> {
                StringBuilder output = new StringBuilder();
                for (int i = 0; i < n; i++) {
                    if (n % 2 == 0) {
                        output.append(i + 1 != n ? 'a' : 'b');
                    } else {
                        if (i + 1 == n) {
                            output.append('c');
                        } else if (i + 2 == n) {
                            output.append('b');
                        } else {
                            output.append('a');
                        }
                    }
                }
                yield output.toString();
            }
        };
    }
}