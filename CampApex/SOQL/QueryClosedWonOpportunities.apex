public class CampApexSolution {
    public List<Opportunity> getClosedWonOpps() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, StageName
            FROM Opportunity
            WHERE StageName = 'Closed Won'
        ];
    }
}