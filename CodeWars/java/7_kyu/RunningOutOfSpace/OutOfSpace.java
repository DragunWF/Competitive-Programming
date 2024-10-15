// https://www.codewars.com/kata/56576f82ab83ee8268000059/train/java

import java.util.Arrays;

public class OutOfSpace {
    public static String[] spacey(String[] array) {
        String[] output = new String[array.length];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < output.length; i++) {
            sb.append(array[i]);
            output[i] = sb.toString();
        }
        return output;
    }

    public static void main(String[] args) {
        // Testing
        System.out.println(Arrays.toString(spacey(new String[] { "i", "have", "no", "cupcakes" })));
        // Expected Output: { "i", "ihave", "ihaveno", "ihavenocupcakes" }
    }
}