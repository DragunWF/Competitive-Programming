// https://www.codewars.com/kata/52f78966747862fc9a0009ae/train/java

import java.util.Stack;

public class Calc {
    public double evaluate(String expr) {
        if (expr.isEmpty())
            return 0;
        String[] tokens = expr.split(" ");
        if (tokens.length == 1)
            return Double.parseDouble(tokens[0]);

        Stack<String> stack = new Stack<>();
        for (String token : tokens) {
            if (token.equals("+") || token.equals("-") ||
                    token.equals("*") || token.equals("/")) {
                String secondToLast = stack.pop();
                stack.add(String.valueOf(calculate(stack.pop(), token, secondToLast)));
            } else {
                stack.add(token);
            }
        }
        return Double.parseDouble(stack.peek());
    }

    private double calculate(String firstNum, String operator, String secondNum) {
        double a = Double.parseDouble(firstNum), b = Double.parseDouble(secondNum);
        double output = 0;
        switch (operator) {
            case "+" -> output = a + b;
            case "-" -> output = a - b;
            case "*" -> output = a * b;
            case "/" -> output = a / b;
        }
        return output;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(new Calc().evaluate("5 1 2 + 4 * + 3 -"));
    }
}
