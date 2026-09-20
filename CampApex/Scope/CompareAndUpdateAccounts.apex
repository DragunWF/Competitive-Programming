public class AccountManager {
    private Account account;

    public AccountManager(Account acc) {
        this.account = acc;
    }

    public Boolean compareAccounts(Account account) {
        // TODO: Return true if the CLASS account's Name 
        // equals the PARAMETER account's Name
        // You need to access BOTH variables in one comparison!
        return this.account == account;
    }

    public void updateFromTemplate(Account account) {
        // TODO: Copy the parameter account's BillingCity 
        // to the CLASS account's BillingCity
        // TODO: Copy the parameter account's Phone
        // to the CLASS account's Phone
        this.account.BillingCity = account.BillingCity;
        this.account.Phone = account.Phone;
    }
}