public class Employee {
    // Add name and department variables
    public String name;
    public String department;

    // Add constructor
    public Employee(String name, String department) {
        this.name = name;
        this.department = department;
    }

    // Add virtual getDetails() method
    public virtual String getDetails() {
        return this.name + ' - ' + this.department;
    }
}

public class Manager extends Employee {
    // Add teamSize variable
    public Integer teamSize;
    
    // Add constructor
    public Manager(String name, String department, Integer teamSize) {
        super(name, department);
        this.teamSize = teamSize;
    }

    // Override getDetails() using super
    public override String getDetails() {
        List<String> formatted = new List<String> {
            super.getDetails(), String.valueOf(this.teamSize)
        };
        return String.format('{0} (Team: {1})', formatted);
    }
}