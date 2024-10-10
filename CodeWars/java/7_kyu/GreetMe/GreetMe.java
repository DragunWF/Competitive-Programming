// https://www.codewars.com/kata/535474308bb336c9980006f2/train/java

public class GreetMe {
    public static String greet(String name) {
        return ("Hello " + String.valueOf(name.charAt(0)).toUpperCase() +
                name.substring(1).toLowerCase() + "!");
    }
}