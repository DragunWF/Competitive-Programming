public class CampApexSolution {
    public Integer deleteContactsByLastNames(List<String> lastNames) {
        // Query contacts by last name and delete them
        // Return the number of contacts deleted
        List<Contact> contacts = [SELECT Id FROM Contact WHERE LastName IN :lastNames];
        delete contacts;
        return contacts.size();
    }
}