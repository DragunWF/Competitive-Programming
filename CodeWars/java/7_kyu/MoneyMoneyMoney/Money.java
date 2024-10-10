// https://www.codewars.com/kata/563f037412e5ada593000114

public class Money {
    public static int calculateYears(double principal, double interest, double tax, double desired) {
        int years = 0;
        while (principal < desired) {
            double taxDeduction = principal * interest * tax;
            double income = principal * interest - taxDeduction;
            principal += income;
            years++;
        }
        return years;
    }
}
