public class CampApexSolution {
    public List<Opportunity> createOpportunitiesWithAmounts(List<Decimal> amounts) {
        // Create Opportunity records with the given amounts
        // Return the list of inserted Opportunities
        List<Opportunity> oppsToInsert = new List<Opportunity>();
        for (Integer i = 0; i < amounts.size(); i++) {
            oppsToInsert.add(new Opportunity(
                Name='Opportunity ' + (i + 1),
                StageName='Prospecting',
                CloseDate=Date.today().addDays(30),
                Amount=amounts[i]
            ));
        }
        insert oppsToInsert;
        return oppsToInsert;
    }
}