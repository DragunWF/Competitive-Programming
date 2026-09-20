class Solution {
    public Set<Id> filterByZipCode(List<Contact> allContacts, List<String> zipCodes){
        Set<Id> matchedContacts = new Set<Id>();
        for (Contact contact : allContacts) {
            if (zipCodes.contains(contact.MailingPostalCode)) {
                matchedContacts.add(contact.Id);
            }
        }
        return matchedContacts;
    }
}