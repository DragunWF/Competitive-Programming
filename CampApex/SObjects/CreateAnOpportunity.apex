public class CampApexSolution {
    public Opportunity createOpportunity(String oppName, String stageName, Date closeDate, Decimal amount) {
        // Create and return a new Opportunity with Name, StageName, CloseDate, and Amount fields set
        return new Opportunity(
            Name=oppName,
            StageName=stageName,
            CloseDate=closeDate,
            Amount=amount
        );
    }
}