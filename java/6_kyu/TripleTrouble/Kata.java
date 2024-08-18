// https://www.codewars.com/kata/55d5434f269c0c3f1b000058/train/java

public class Kata {
    private static char previousLastNum = 'n'; // default value

    public static int TripleDouble(long num1, long num2) {
        boolean straightTriple = isConsecutive(num1, 3);
        boolean straightDouble = isConsecutive(num2, 2);
        previousLastNum = 'n';
        return straightTriple && straightDouble ? 1 : 0;
    }

    private static boolean isConsecutive(long num, int occurence) {
        String strNum = String.valueOf(num);
        int sameNumCount = previousLastNum == 'n' ? 1 : 0;
        char lastNum = strNum.charAt(0);
        for (int i = 1; i < strNum.length(); i++) {
            if (previousLastNum == 'n' && lastNum == strNum.charAt(i) || previousLastNum == strNum.charAt(i)) {
                sameNumCount++;
            } else {
                lastNum = strNum.charAt(i);
                sameNumCount = 1;
            }
            if (sameNumCount == occurence) {
                if (occurence == 3)
                    previousLastNum = lastNum;
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(TripleDouble(451999277L, 41177722899L)); // 1
        System.out.println(TripleDouble(1222345L, 12345L)); // 0
    }
}