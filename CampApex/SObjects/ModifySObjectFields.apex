public class CampApexSolution {
    public Contact updateContactEmail(Contact con, String newEmail) {
        // Update the Contact's Email field and return the Contact
        con.Email = newEmail;
        return con;
    }
}