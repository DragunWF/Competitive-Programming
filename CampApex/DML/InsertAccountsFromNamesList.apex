public class CampApexSolution {
    public List<Account> createAccountsFromNames(List<String> accountNames) {
        // Create Account records from the names list and insert them
        // Return the list of inserted Accounts
        List<Account> accountsToInsert = new List<Account>();
        for (String name : accountNames) {
            accountsToInsert.add(new Account(Name=name));
        }
        insert accountsToInsert;
        return accountsToInsert;
    }
}