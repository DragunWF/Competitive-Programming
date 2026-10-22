public class CampApexSolution {
    public List<Account> getLargeAccounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, NumberOfEmployees
            FROM Account
            WHERE NumberOfEmployees >= 50
        ];
    }
}