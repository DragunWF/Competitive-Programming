public class CampApexSolution {
    public String getContactEmail(sObject record) {
        // Check if record is a Contact, then return Email or null
        if (record instanceof Contact) {
            return ((Contact)record).Email;
        }
        return null;
    }
}