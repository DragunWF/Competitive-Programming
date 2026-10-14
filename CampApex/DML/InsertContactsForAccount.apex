public class CampApexSolution {
    public List<Contact> createContactsForAccount(Id accountId, List<String> lastNames) {
        // Create Contact records linked to the account with the given last names
        // Return the list of inserted Contacts
        List<Contact> contacts = new List<Contact>();
        for (String name : lastNames) {
            contacts.add(new Contact(LastName=name, AccountId=accountId));
        }
        insert contacts;
        return contacts;
    }
}