public class CampApexSolution {
    public List<Opportunity> getHighValueOpps() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, Amount
            FROM Opportunity
            WHERE Amount > 50000
        ];
    }
}