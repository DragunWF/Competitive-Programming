// https://www.campapex.org/practice/soql

public class CampApexSolution {
    public List<Account> getAccountsAlphabetically() {
        // Write your SOQL query here
        return [
            SELECT Id, Name
            FROM Account
            ORDER BY Name
        ];
    }
}