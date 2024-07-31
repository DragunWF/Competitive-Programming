// https://www.codewars.com/kata/55c90cad4b0fe31a7200001f/train/java

public class Kata {
    public static String buildString(String... args) {
        return String.format("I like %s!", String.join(", ", args));
    }
}