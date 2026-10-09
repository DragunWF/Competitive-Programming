public class CampApexSolution {
    public Decimal applyDiscount(Decimal price, Integer discount) {
        return price - (price * discount / 100);
    }
}