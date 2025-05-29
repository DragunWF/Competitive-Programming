// https://www.codewars.com/kata/6071ef9cbe6ec400228d9531/train/java

class Solution {
    public static String calc(String text) {
        String[] values = text.split(" ");

        int firstOperandValue = values[0].length();
        String operator = values[1];
        int secondOperandValue = values[2].length();
        int result = 0;

        switch (operator) {
            case "+" -> result = firstOperandValue + secondOperandValue;
            case "-" -> result = firstOperandValue - secondOperandValue;
            case "*" -> result = firstOperandValue * secondOperandValue;
            case "//" -> result = firstOperandValue / secondOperandValue;
        }
        ;

        return generateDots(result);
    }

    private static String generateDots(int count) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < count; i++) {
            output.append('.');
        }
        return output.toString();
    }

    public static void main(String[] args) {
        System.out.println(calc("..... // ."));
    }
}