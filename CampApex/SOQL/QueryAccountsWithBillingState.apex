public class CampApexSolution {
    public List<Account> getAccountsWithState() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, BillingState
            FROM Account
            WHERE BillingState != null
        ];
    }
}