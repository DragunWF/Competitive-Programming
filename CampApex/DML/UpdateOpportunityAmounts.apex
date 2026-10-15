public class CampApexSolution {
    public List<Opportunity> updateOpportunityAmounts(Map<Id, Decimal> oppIdToAmount) {
        // Query opportunities, update their amounts, and save changes
        // Return the list of updated Opportunities
        List<Opportunity> oppsToUpdate = new List<Opportunity>();
        for (Id oppId : oppIdToAmount.keySet()) {
            oppsToUpdate.add(new Opportunity(
                Id=oppId,
                Amount=oppIdToAmount.get(oppId)
            ));
        }
        update oppsToUpdate;
        return oppsToUpdate;
    }
}