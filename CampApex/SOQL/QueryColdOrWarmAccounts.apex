public class CampApexSolution {
    public List<Account> getColdOrWarmAccounts() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, Rating
            FROM Account
            WHERE Rating = 'Cold' OR Rating = 'Warm'
        ];
    }
}