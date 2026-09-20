public class CampApexSolution {
    public Boolean isEligibleForDiscount(Boolean isMember, Integer orderAmount) {
        return isMember || orderAmount >= 100;
    }
}