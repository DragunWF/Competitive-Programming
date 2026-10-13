public class CampApexSolution {
    public List<Contact> createContactsWithLastNames(List<String> lastNames) {
        // Create Contact records from the last names list and insert them
        // Return the list of inserted Contacts
        List<Contact> contactsToInsert = new List<Contact>();
        for (String name : lastNames) {
            contactsToInsert.add(new Contact(LastName=name));
        }
        insert contactsToInsert;
        return contactsToInsert;
    }
}