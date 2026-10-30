// https://www.campapex.org/practice/soql

public class CampApexSolution {
    public List<Account> getAccountsInCountries() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, BillingCountry
            FROM Account
            WHERE BillingCountry IN ('China', 'Indonesia', 'Brazil')
        ];
    }
}