// https://www.codewars.com/kata/5a4d303f880385399b000001/train/java

class StrongNumber {
    public static String isStrongNumber(int num) {
        String strNum = String.valueOf(num);
        int sum = 0;
        for (int i = 0; i < strNum.length(); i++) {
            sum += factorial(Integer.parseInt(String.valueOf(strNum.charAt(i))));
        }
        return sum == num ? "STRONG!!!!" : "Not Strong !!";
    }

    private static int factorial(int num) {
        int product = num;
        for (int i = num - 1; i >= 2; i--) {
            product *= i;
        }
        return product;
    }
}