// https://www.codewars.com/kata/5a9c35e9ba1bb5c54a0001ac/train/java

public class Solution {
    public static int add(int x, int y) {
        StringBuilder sb = new StringBuilder();
        StringBuilder first = new StringBuilder();
        StringBuilder second = new StringBuilder();

        if (x < 0 && y > 0 || x > 0 && y < 0) {
            if (x > y) {
                
            }
        } else {
            while (first.length() < Math.abs(x)) {
                first.append("_");
                sb.append('_');
            }
            while (second.length() < Math.abs(y)) {
                second.append("_");
                sb.append('_');
            }
        }

        return x < 0 ? -sb.length() : sb.length();
    }
}