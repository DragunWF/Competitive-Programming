// https://www.codewars.com/kata/597c684822bc9388f600010f/train/java

public class Dinglemouse {
    private String firstName;
    private String lastName;

    public Dinglemouse(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public String getFullName() {
        String separator = lastName.isEmpty() || firstName.isEmpty() ? "" : " ";
        return String.format("%s%s%s", firstName, separator, lastName);
    }
}