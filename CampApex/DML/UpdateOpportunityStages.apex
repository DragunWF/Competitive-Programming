public class CampApexSolution {
    public List<Opportunity> updateOpportunityStages(List<Id> opportunityIds, String newStage) {
        // Query opportunities, update their stages, and save changes
        // Return the list of updated Opportunities
        List<Opportunity> oppsToUpdate = new List<Opportunity>();
        for (Id oppId : opportunityIds) {
            oppsToUpdate.add(new Opportunity(
                Id=oppId,
                StageName=newStage
            ));
        }
        update oppsToUpdate;
        return oppsToUpdate;
    }
}