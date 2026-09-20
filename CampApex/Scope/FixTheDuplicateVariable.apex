public class InvoiceCalculator {
    public Decimal calculateTotal(List<Decimal> invoices) {
        Decimal total = 0;

        for (Decimal invoice : invoices) {
            total += invoice; // mistakenly re-declares total
        }

        return total;
    }
}