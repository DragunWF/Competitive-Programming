public class CampApexSolution {
    public List<Opportunity> getTop5Opps() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, Amount
            FROM Opportunity
            ORDER BY Amount DESC
            LIMIT 5
        ];
    }
}