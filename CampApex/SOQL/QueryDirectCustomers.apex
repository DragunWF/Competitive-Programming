public class CampApexSolution {
    public List<Account> getDirectCustomers() {
        // Write your SOQL query here
        return [
            SELECT Id, Name, Type
            FROM Account
            WHERE Type = 'Customer - Direct'
        ];
    }
}