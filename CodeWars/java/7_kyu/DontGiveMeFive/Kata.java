// https://www.codewars.com/kata/5813d19765d81c592200001a/train/java

public class Kata {
    public static int dontGiveMeFive(int start, int end) {
        int count = 0;
        for (int i = start; i <= end; i++) {
            String strNum = String.valueOf(i);
            if (strNum.charAt(strNum.length() - 1) != '5' &&
                    strNum.charAt(0) != '5') {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(dontGiveMeFive(1, 9));
        System.out.println(dontGiveMeFive(4, 17));
    }
}
