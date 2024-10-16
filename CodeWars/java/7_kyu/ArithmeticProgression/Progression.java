// https://www.codewars.com/kata/55caf1fd8063ddfa8e000018/train/java

class Progression {
    public static String arithmeticSequenceElements(int a, int d, long n) {
        int[] seq = new int[(int) n];
        for (int i = 0, seqNum = a; i < n; i++, seqNum += d) {
            seq[i] = seqNum;
        }

        StringBuilder output = new StringBuilder();
        for (int i = 0; i < seq.length; i++) {
            output.append(seq[i]);
            if (i != seq.length - 1) {
                output.append(", ");
            }
        }
        return output.toString();
    }
}