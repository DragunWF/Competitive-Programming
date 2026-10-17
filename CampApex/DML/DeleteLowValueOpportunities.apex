public class CampApexSolution {
    public Integer deleteLowValueOpportunities(Decimal threshold) {
        // Query opportunities below threshold and delete them
        // Return the number of opportunities deleted
        List<Opportunity> opportunitiesToDelete = [
            SELECT Id
            FROM Opportunity 
            WHERE Amount < :threshold
        ];
        delete opportunitiesToDelete;
        return opportunitiesToDelete.size();
    }
}