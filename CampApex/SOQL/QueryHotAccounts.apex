public class CampApexSolution {
    public List<Account> getHotAccounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, Rating
            FROM Account
            WHERE Rating = 'Hot'
        ];
    }
}