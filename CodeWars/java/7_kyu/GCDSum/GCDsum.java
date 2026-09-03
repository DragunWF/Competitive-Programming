// https://www.codewars.com/kata/5dd259444228280032b1ed2a/train/java

class GCDsum{
    public static int[] solve(int s, int g){        
        int secondNumber = s - g;
        if (secondNumber % g != 0) {
            return new int[] { -1, -1 };
        }
        return new int[] { g, secondNumber };
    }
}