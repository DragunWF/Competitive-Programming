// https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/java

class FirstNonConsecutive {
    static Integer find(final int[] array) {
        for (int i = 1; i < array.length; i++)
            if (array[i - 1] + 1 != array[i])
                return array[i];
        return null;
    }
}
