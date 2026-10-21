public class CampApexSolution {
    public Account mergeDuplicateAccounts(Id masterAccountId, Id duplicateAccountId) {
        // Query both accounts and merge the duplicate into the master
        // Return the master Account
        Account masterAccount = [SELECT Id, Name FROM Account WHERE Id = :masterAccountId];
        Account duplicateAccount = [SELECT Id, Name FROM Account WHERE Id = :duplicateAccountId];
        merge masterAccount duplicateAccount;
        return masterAccount;
    }
}