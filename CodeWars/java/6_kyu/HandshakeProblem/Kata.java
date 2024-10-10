// https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/java

public class Kata {
    public static int GetParticipants(int handshakes) {
        int farmers = 0;
        int combinations = 0;
        while (combinations < handshakes) {
            farmers++;
            combinations = 0;
            for (int i = farmers - 1; i >= 1; i--)
                combinations += i;
        }
        return farmers;
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        System.out.println();
        int[] testCases = { 0, 1, 3, 6, 7 };
        for (int num : testCases) {
            System.out.println(GetParticipants(num));
        }
    }
}
