public class CampApexSolution {
    public List<Contact> upsertContactsByEmail(List<Contact> contacts) {
        // Upsert contacts using Email as the external ID field
        // Return the list of upserted Contacts
        upsert contacts Contact.fields.Email;
        return contacts;
    }
}