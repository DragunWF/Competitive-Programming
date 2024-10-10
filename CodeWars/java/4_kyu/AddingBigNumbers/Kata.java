// https://www.codewars.com/kata/525f4206b73515bffb000b21/train/java

public class Kata {
    public static String add(String a, String b) {
        StringBuilder output = new StringBuilder();
        a = removeStartingZeros(a);
        b = removeStartingZeros(b);
        if (a.length() != b.length()) {
            if (a.length() > b.length()) {
                b = balanceLengths(b, a.length());
            } else {
                a = balanceLengths(a, b.length());
            }
        }

        boolean carryOne = false;
        for (int i = a.length() - 1; i >= 0; i--) {
            int sum = (Integer.parseInt(String.valueOf(a.charAt(i))) +
                    Integer.parseInt(String.valueOf(b.charAt(i))));
            if (carryOne) {
                sum += 1;
                carryOne = false;
            }
            if (sum >= 10 && i != 0) {
                carryOne = true;
                sum %= 10;
            }
            output.insert(0, sum);
        }

        return output.toString();
    }

    private static String removeStartingZeros(String str) {
        int numIndex = 0;
        for (int i = 0, n = str.length(); i < n; i++) {
            if (str.charAt(i) != '0') {
                numIndex = i;
                break;
            }
        }
        return str.substring(numIndex);
    }

    private static String balanceLengths(String str, int targetLength) {
        StringBuilder output = new StringBuilder();
        for (int i = 0, n = str.length(); i < targetLength; i++) {
            if (i < n) {
                output.append(str.charAt(i));
            } else {
                output.insert(0, "0");
            }
        }
        return output.toString();
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        System.out.println(add("123", "321")); // 444
        System.out.println(add("11", "99")); // 110
        System.out.println(add("123", "456")); // 579
        System.out.println(add("888", "222")); // 1110
        System.out.println(add("1372", "69")); // 1441
        System.out.println(add("9961", "07311017844050"));
    }
}
