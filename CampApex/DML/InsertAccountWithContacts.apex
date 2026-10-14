public class CampApexSolution {
    public Account createAccountWithContacts(String accountName, List<String> contactLastNames) {
        // Insert an Account, then insert Contacts linked to it
        // Return the inserted Account
        Account account = new Account(Name=accountName);
        insert account;

        List<Contact> contacts = new List<Contact>();
        for (String name : contactLastNames) {
            contacts.add(new Contact(
                LastName=name,
                AccountId=account.Id
            ));
        }
        insert contacts;
        return account;
    }
}