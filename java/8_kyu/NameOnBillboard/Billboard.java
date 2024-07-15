// https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/java

// Not allowed to use the "*" operator
// If it was then simply return name.length() * price

public class Billboard {
    public static int billboard(String name, int price) {
        int total = 0;
        for (int i = 0, n = name.length(); i < n; i++) {
            total += price;
        }
        return total;
    }
}