// https://www.codewars.com/kata/577a98a6ae28071780000989/train/java

public class Kata {
    public int min(int[] list) {
        int output = list[0];
        for (int i = 1; i < list.length; i++)
            if (list[i] < output)
                output = list[i];
        return output;
    }

    public int max(int[] list) {
        int output = list[0];
        for (int i = 1; i < list.length; i++)
            if (list[i] > output)
                output = list[i];
        return output;
    }
}
