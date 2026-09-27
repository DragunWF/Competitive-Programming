public class CampApexSolution {
    public Integer countActiveAccounts(List<Account> accounts) {
        Integer count = 0;
        for (Account account : accounts) {
            if (account.Industry == 'Technology') {
                count++;
            }
        }
        return count;
    }
}