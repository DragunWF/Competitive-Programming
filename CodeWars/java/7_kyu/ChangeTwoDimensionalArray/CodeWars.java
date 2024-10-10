// https://www.codewars.com/kata/581214d54624a8232100005f/train/java

class CodeWars {
    public static int[][] matrix(int[][] array) {
        int[][] output = new int[array.length][array[0].length];
        for (int i = 0; i < output.length; i++) {
            for (int j = 0; j < array.length; j++) {
                if (j == i) {
                    output[i][j] = array[i][j] < 0 ? 0 : 1;
                } else {
                    output[i][j] = array[i][j];
                }
            }
        }
        return output;
    }
}