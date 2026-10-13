public class CampApexSolution {
    public List<Contact> createContactsWithEmails(Map<String, String> lastNameToEmail) {
        // Create Contact records with last names and emails from the map
        // Return the list of inserted Contacts
        List<Contact> contacts = new List<Contact>();
        for (String key : lastNameToEmail.keySet()) {
            contacts.add(new Contact(
                LastName=key,
                Email=lastNameToEmail.get(key)
            ));
        }
        insert contacts;
        return contacts;
    }
}