public class CampApexSolution {
    public List<Account> upsertAccountsByName(List<Account> accounts) {
        Set<String> names = new Set<String>();
        for (Account acc : accounts) {
            names.add(acc.Name);
        }
        Map<String, Id> existingByName = new Map<String, Id>();
        for (Account existing : [SELECT Id, Name FROM Account WHERE Name IN :names]) {
            existingByName.put(existing.Name, existing.Id);
        }
        for (Account acc : accounts) {
            if (existingByName.containsKey(acc.Name)) {
                acc.Id = existingByName.get(acc.Name);
            }
        }
        upsert accounts;
        return accounts;
    }
}