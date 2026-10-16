public class CampApexSolution {
    public List<Account> updateAccountDescriptions(Map<Id, String> accountIdToDescription) {
        // Query accounts, update their descriptions, and save changes
        // Return the list of updated Accounts
        List<Account> accountsToUpdate = new List<Account>();
        for (Id accountId : accountIdToDescription.keySet()) {
            accountsToUpdate.add(new Account(
                Id=accountId,
                Description=accountIdToDescription.get(accountId)
            ));
        }
        update accountsToUpdate;
        return accountsToUpdate;
    }
}