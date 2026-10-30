public class CampApexSolution {
    public List<Opportunity> getNewCustomerOpps() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, Type
            FROM Opportunity
            WHERE Type = 'New Customer'
        ];
    }
}