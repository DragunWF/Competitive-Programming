public class CampApexSolution {
    public List<Account> getUSAccounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, BillingCountry
            FROM Account
            WHERE BillingCountry = 'United States'
        ];
    }
}