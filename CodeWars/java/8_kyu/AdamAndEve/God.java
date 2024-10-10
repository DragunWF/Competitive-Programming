// https://www.codewars.com/kata/547274e24481cfc469000416/train/java

public class God {
    public static Human[] create() {
        return new Human[] { new Man(), new Woman() };
    }
}

class Human {}
class Man extends Human {}
class Woman extends Human {}
