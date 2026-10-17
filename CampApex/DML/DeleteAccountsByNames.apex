public class CampApexSolution {
    public Integer deleteAccountsByNames(List<String> accountNames) {
        // Query accounts by name and delete them
        // Return the number of accounts deleted
        List<Account> accounts = [SELECT Id FROM Account WHERE Name IN :accountNames];
        delete accounts;
        return accounts.size();
    }
}