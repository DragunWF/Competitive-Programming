public class PricingHelper {
    Decimal discount = 0.10;

    public Decimal applyDiscount(Decimal amount) {
        // Decimal discount = 0.20; // shadows class variable
        System.debug('Applied discount: ' + discount);
        return amount - (amount * discount);
    }
}