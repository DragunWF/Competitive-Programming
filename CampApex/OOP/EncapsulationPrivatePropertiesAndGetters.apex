public class BankAccount {
    // Add private balance variable
    private Decimal balance = 0;

    // Add getBalance() method
    public Decimal getBalance() {
        return this.balance;
    }

    // Add deposit() method
    public Decimal deposit(Decimal amount) {
        this.balance += amount;
        return this.balance;
    }
}