public class CampApexSolution {
    public List<Account> updateAccountNames(Map<Id, String> accountIdToNewName) {
        // Query accounts, update their names, and save changes
        // Return the list of updated Accounts
        List<Account> accountsToUpdate = new List<Account>();
        for (Id accountId : accountIdToNewName.keySet()) {
            accountsToUpdate.add(new Account(
                Id=accountId,
                Name=accountIdToNewName.get(accountId)
            ));
        }
        update accountsToUpdate;
        return accountsToUpdate;
    }
}