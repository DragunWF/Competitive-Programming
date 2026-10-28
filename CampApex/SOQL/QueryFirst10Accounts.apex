public class CampApexSolution {
    public List<Account> getFirst10Accounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name
            FROM Account
            LIMIT 10
        ];
    }
}