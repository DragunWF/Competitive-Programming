public class Person {
    // Add private age variable
    private Integer age;

    // Add setAge() method with validation
    public Boolean setAge(Integer newAge) {
        if (newAge >= 0 && newAge <= 150) {
            this.age = newAge;
            return true;
        }
        return false;
    }

    // Add getAge() method
    public Integer getAge() {
        return this.age;
    }
}