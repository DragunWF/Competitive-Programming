public class CampApexSolution {
    public List<Contact> updateContactEmails(Map<Id, String> contactIdToEmail) {
        // Query contacts, update their emails, and save changes
        // Return the list of updated Contacts
        List<Contact> contactsToUpdate = new List<Contact>();
        for (Id contactId : contactIdToEmail.keySet()) {
            contactsToUpdate.add(new Contact(
                Id=contactId,
                Email=contactIdToEmail.get(contactId)
            ));
        }
        update contactsToUpdate;
        return contactsToUpdate;
    }
}