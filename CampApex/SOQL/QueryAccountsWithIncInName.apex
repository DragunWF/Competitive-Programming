public class CampApexSolution {
    public List<Account> getIncAccounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name
            FROM Account
            WHERE Name LIKE '%Inc%'
        ];
    }
}