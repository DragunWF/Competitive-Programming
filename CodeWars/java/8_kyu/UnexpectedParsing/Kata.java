// https://www.codewars.com/kata/54fdaa4a50f167b5c000005f/train/java

import java.util.HashMap;

public class Kata {
    public static HashMap<String, String> getStatus(boolean isBusy) {
        HashMap<String, String> status = new HashMap<>();
        status.put("status", isBusy ? "busy" : "available");
        return status;
    }
}