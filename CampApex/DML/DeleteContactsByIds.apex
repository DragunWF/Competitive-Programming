public class CampApexSolution {
    public Integer deleteContactsByIds(List<Id> contactIds) {
        // Query and delete contacts with the given Ids
        // Return the number of contacts deleted
        List<Contact> contacts = new List<Contact>();
        for (Id contactId : contactIds) {
            contacts.add(new Contact(Id=contactId));
        }
        delete contacts;
        return contacts.size();
    }
}