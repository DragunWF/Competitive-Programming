public class CampApexSolution {
    public List<Opportunity> createOpportunitiesForAccount(Id accountId, Map<String, Decimal> nameToAmount) {
        // Create Opportunity records linked to the account
        // Return the list of inserted Opportunities
        List<Opportunity> opportunities = new List<Opportunity>();
        for (String name : nameToAmount.keySet()) {
            opportunities.add(new Opportunity(
                Name=name,
                Amount=nameToAmount.get(name),
                StageName='Qualification',
                CloseDate=Date.today().addDays(60),
                AccountId=accountId
            ));
        }
        insert opportunities;
        return opportunities;
    }
}