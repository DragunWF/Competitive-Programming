public class Person {
    // Declare public String properties for firstName and lastName
    private String firstName;
    private String lastName;

    // Create a constructor that takes firstName and lastName parameters
    public Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Create a getFullName method that returns 'firstName lastName'
    public String getFullName() {
        return this.firstName + ' ' + this.lastName;
    }
}