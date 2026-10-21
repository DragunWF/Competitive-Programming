public class CampApexSolution {
    public Integer mergeAccountsReparentContacts(Id masterAccountId, Id duplicateAccountId) {
        // Merge accounts and return count of contacts on master
        Account masterAccount = [SELECT Id, Name FROM Account WHERE Id = :masterAccountId];
        Account duplicateAccount = [SELECT Id, Name FROM Account WHERE Id = :duplicateAccountId];
        merge masterAccount duplicateAccount;
        return [SELECT COUNT() FROM Contact WHERE AccountId = :masterAccountId];
    }
}