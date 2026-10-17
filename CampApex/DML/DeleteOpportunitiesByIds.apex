public class CampApexSolution {
    public Integer deleteOpportunitiesByIds(List<Id> opportunityIds) {
        // Query and delete opportunities with the given Ids
        // Return the number of opportunities deleted
        List<Opportunity> opps = new List<Opportunity>();
        for (Id id : opportunityIds) {
            opps.add(new Opportunity(Id=id));
        }
        delete opps;
        return opps.size();
    }
}