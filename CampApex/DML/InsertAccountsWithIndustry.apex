public class CampApexSolution {
    public List<Account> createAccountsWithIndustry(Map<String, String> nameToIndustry) {
        // Create Account records with names and industries from the map
        // Return the list of inserted Accounts
        List<Account> accountsToInsert = new List<Account>();
        for (String key : nameToIndustry.keySet()) {
            accountsToInsert.add(new Account(
                Name=key,
                Industry=nameToIndustry.get(key)
            ));
        }
        insert accountsToInsert;
        return accountsToInsert;
    }
}