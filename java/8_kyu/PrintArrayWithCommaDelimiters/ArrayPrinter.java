// https://www.codewars.com/kata/56e2f59fb2ed128081001328/train/java

public class ArrayPrinter {
    public static String printArray(Object[] array) {
        String[] strArr = new String[array.length];
        for (int i = 0; i < array.length; i++) {
            strArr[i] = String.valueOf(array[i]);
        }
        return String.join(",", strArr);
    }
}