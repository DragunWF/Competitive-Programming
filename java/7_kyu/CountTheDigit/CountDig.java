// https://www.codewars.com/kata/566fc12495810954b1000030/train/java

public class CountDig {
    public static int nbDig(int n, int d) {
        int count = 0;
        for (int i = 0; i <= n; i++) {
            String squaredStr = String.valueOf(i * i);
            for (int j = 0; j < squaredStr.length(); j++) {
                if (squaredStr.charAt(j) - 48 == d) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(nbDig(10, 1));
    }
}
