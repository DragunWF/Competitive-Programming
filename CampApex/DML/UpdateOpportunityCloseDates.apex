public class CampApexSolution {
    public List<Opportunity> updateOpportunityCloseDates(List<Id> opportunityIds, Date newCloseDate) {
        // Query opportunities, update their close dates, and save changes
        // Return the list of updated Opportunities
        List<Opportunity> opps = new List<Opportunity>();
        for (Id oppId : opportunityIds) {
            opps.add(new Opportunity(
                Id=oppId,
                CloseDate=newCloseDate
            ));
        }
        update opps;
        return opps;
    }
}