public class CampApexSolution {
    public List<Contact> getPortugalContacts() {
        // Write your SOQL query here
        return [
            SELECT Id, FirstName, LastName, MailingCountry
            FROM Contact
            WHERE MailingCountry = 'Portugal'
        ];
    }
}