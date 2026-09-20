public class CampApexSolution {
    public Boolean isPremiumCustomer(Integer totalPurchases, Integer yearsActive) {
        return totalPurchases > 5000 && yearsActive >= 2;
    }
}