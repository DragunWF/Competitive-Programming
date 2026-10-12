public class Animal {
    // Add name variable
    public String name;

    // Add constructor
    public Animal(String name) {
        this.name = name;
    }

    // Add virtual speak() method
    public virtual String speak() {
        return '...';
    }
}

public class Dog extends Animal {
    // Add constructor that calls super()
    public Dog(String name) {
        super(name);
    }

    // Override speak() method
    public override String speak() {
        return 'Woof!';
    }
}