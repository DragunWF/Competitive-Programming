// https://www.codewars.com/kata/58485a43d750d23bad0000e6/train/java

public class FizzBuzzCuckooClock {
    public static String fizzBuzzCuckooClock(String time) {
        String[] timeStr = time.split(":");
        int hour = Integer.parseInt(timeStr[0]);
        int minutes = Integer.parseInt(timeStr[1]);
        if (minutes == 0) {
            int cuckooCount;
            if (hour == 0) {
                cuckooCount = 12;
            } else {
                cuckooCount = hour > 12 ? hour % 12 : hour;
            }
            String[] cuckoos = new String[cuckooCount];
            for (int i = 0; i < cuckoos.length; i++) {
                cuckoos[i] = "Cuckoo";
            }
            return String.join(" ", cuckoos);
        } else if (minutes == 30) {
            return "Cuckoo";
        }
        return fizzBuzz(minutes);
    }

    private static String fizzBuzz(int num) {
        if (num % 3 == 0 && num % 5 == 0) {
            return "Fizz Buzz";
        }
        if (num % 3 == 0) {
            return "Fizz";
        }
        if (num % 5 == 0) {
            return "Buzz";
        }
        return "tick";
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        String[] testCases = {
                "13:34", // tick
                "12:00" //
        };
        for (int i = 0; i < testCases.length; i++) {
            System.out.println(fizzBuzzCuckooClock(testCases[i]));
        }
    }
}
