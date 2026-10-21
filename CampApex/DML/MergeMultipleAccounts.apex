public class CampApexSolution {
    public Account mergeMultipleAccounts(Id masterAccountId, List<Id> duplicateAccountIds) {
        // Query accounts and merge all duplicates into the master
        // Return the master Account
        Account masterAccount = [SELECT Id, Name FROM Account WHERE Id = :masterAccountId];
        List<Account> duplicateAccounts = [SELECT Id, Name FROM Account WHERE Id IN :duplicateAccountIds];
        merge masterAccount duplicateAccountIds;
        return masterAccount;
    }
}