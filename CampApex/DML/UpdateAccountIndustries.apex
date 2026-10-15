public class CampApexSolution {
    public List<Account> updateAccountIndustries(List<Id> accountIds, String newIndustry) {
        // Query accounts, update their industries, and save changes
        // Return the list of updated Accounts
        List<Account> accountsToUpdate = new List<Account>();
        for (Id accountId : accountIds) {
            accountsToUpdate.add(new Account(
                Id=accountId,
                Industry=newIndustry
            ));
        }
        update accountsToUpdate;
        return accountsToUpdate;
    }
}