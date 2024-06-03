// https://www.codewars.com/kata/58649884a1659ed6cb000072/train/java

public class TrafficLights {
    public static String updateLight(String current) {
        if (current.equals("green")) {
            return "yellow";
        }
        return current.equals("yellow") ? "red" : "green";
    }
}