public class CampApexSolution {
    public String getAccountName(sObject record) {
        // Cast the sObject to Account and return the Name
        return ((Account)record).Name;
    }
}