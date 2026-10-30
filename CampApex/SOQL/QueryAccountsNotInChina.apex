public class CampApexSolution {
    public List<Account> getAccountsNotInChina() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, BillingCountry
            FROM Account
            WHERE BillingCountry != 'China'
        ];
    }
}