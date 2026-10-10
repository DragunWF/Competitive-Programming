public class BankAccount {
    public Decimal balance = 0;

    public void deposit(Decimal amount) {
        this.balance += amount;
    }

    public void withdraw(Decimal amount) {
        this.balance -= amount;
    }

    public Decimal getBalance() {
        return this.balance;
    }
}