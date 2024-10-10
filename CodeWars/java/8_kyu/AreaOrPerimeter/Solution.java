// https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/java

public class Solution {
    public static int areaOrPerimeter(int length, int width) {
        return length == width ? width * length : 2 * (length + width);
    }
}