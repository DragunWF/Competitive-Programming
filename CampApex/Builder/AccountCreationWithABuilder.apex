public class AccountService {
    
    public Account createCustomerAccount(String name) {
        AccountBuilder builder = new AccountBuilder();
        builder.withName(name).withType('Customer');
        return builder.build();
    }
    
    public Account createProspectAccount(String name) {
        AccountBuilder builder = new AccountBuilder();
        builder.withName(name)
               .withType('Prospect')
               .withIndustry('Technology')
               .withAnnualRevenue(1000000)
               .withBillingCity('San Francisco')
               .withBillingState('CA');
        return builder.build();
    }
}

public class AccountBuilder {
     private Account account;
     
     public AccountBuilder() {
          this.account = new Account();
     }

     public AccountBuilder withName(String name) { 
          this.account.Name = name;
          return this;
     }
     public AccountBuilder withType(String accountType) {
          this.account.Type = accountType;
          return this;
     }
     public AccountBuilder withIndustry(String industry) {  
          this.account.Industry = industry;
          return this;
     }
     public AccountBuilder withAnnualRevenue(Decimal revenue) {
          this.account.AnnualRevenue = revenue;
          return this;
     }
     public AccountBuilder withBillingCity(String city) {
          this.account.BillingCity = city;
          return this;
     }
     public AccountBuilder withBillingState(String state) {       
          this.account.BillingState = state;
          return this;
     }
     public Account build() {
          return this.account;
     }
}