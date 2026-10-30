public class CampApexSolution {
    public List<Contact> getMarketingContacts() {
        // Write your SOQL query here
        return [
            SELECT Id, FirstName, LastName, Department
            FROM Contact
            WHERE Department = 'Marketing'
        ];
    }
}