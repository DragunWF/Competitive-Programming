public class CampApexSolution {
    public List<Account> getTopRevenueAccounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, AnnualRevenue
            FROM Account
            ORDER BY AnnualRevenue DESC
        ];
    }
}