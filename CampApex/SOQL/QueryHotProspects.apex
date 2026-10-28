public class CampApexSolution {
    public List<Account> getHotProspects() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, Rating, Type
            FROM Account
            WHERE Rating = 'Hot' AND Type = 'Prospects'
        ];
    }
}