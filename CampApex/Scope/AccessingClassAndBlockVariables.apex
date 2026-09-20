public class SimpleCalculator {
    // Do not change this
    private Decimal result = 0;

    public Decimal addNumbers(Decimal num1, Decimal num2) {
        Decimal sum = num1 + num2;
        // TODO: Set the class variable 'result' to equal 'sum'
        // TODO: Return the 
        result = sum;
        return sum;
    }

    public String getResultSummary() {
        // TODO: Return a string that says "Current result: [result]"
        // HINT: What class variable can you access here?
        return 'Current result: ' + result;
    }

    public Decimal processLoop() {
        Decimal total = 0;
        for(Integer i = 1; i <= 3; i++) {
            Decimal loopValue = i * 2;
            total += loopValue;
        }
        // TODO: Try to return 'loopValue' - what happens?
        // TODO: Instead, what should you return?
        return total;
    }
}