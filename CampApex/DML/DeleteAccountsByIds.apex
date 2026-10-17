public class CampApexSolution {
    public Integer deleteAccountsByIds(List<Id> accountIds) {
        // Query and delete accounts with the given Ids
        // Return the number of accounts deleted
        List<Account> accounts = new List<Account>();
        for (Id accountId : accountIds) {
            accounts.add(new Account(Id=accountId));
        }
        delete accounts;
        return accounts.size();
    }
}