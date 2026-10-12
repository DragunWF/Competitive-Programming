public class Vehicle {
    // Add virtual getSpeed() method
    public virtual Integer getSpeed() {
        return 0;
    }
}

public class Car extends Vehicle {
    // Override getSpeed()
    public override Integer getSpeed() {
        return 120;
    }
}

public class Bicycle extends Vehicle {
    // Override getSpeed()
    public override Integer getSpeed() {
        return 25;
    }
}

public class SpeedCalculator {
    // Add getTotalSpeed() method
    public Integer getTotalSpeed(List<Vehicle> vehicles) {
        Integer totalSpeed = 0;
        for (Vehicle vehicle : vehicles) {
            totalSpeed += vehicle.getSpeed();
        }
        return totalSpeed;
    }
}