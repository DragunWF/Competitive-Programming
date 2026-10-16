public class CampApexSolution {
    public List<Contact> updateContactPhones(Map<Id, String> contactIdToPhone) {
        // Query contacts, update their phone numbers, and save changes
        // Return the list of updated Contacts
        List<Contact> contactsToUpdate = new List<Contact>();
        for (Id contactId : contactIdToPhone.keySet()) {
            contactsToUpdate.add(new Contact(
                Id=contactId,
                Phone=contactIdToPhone.get(contactId)
            ));
        }
        update contactsToUpdate;
        return contactsToUpdate;
    }
}