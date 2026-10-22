public class CampApexSolution {
    public List<Account> getHighRevenueAccounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, AnnualRevenue
            FROM Account
            WHERE AnnualRevenue > 500000
        ];
    }
}