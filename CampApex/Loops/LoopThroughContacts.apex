public class CampApexSolution {
    public Contact findContactByEmail(List<Contact> contacts, String email) {
        for (Contact contact : contacts) {
            if (contact.Email == email) {
                return contact;
            }
        }
        return null;
    }
}