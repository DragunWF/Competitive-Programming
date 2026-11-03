// https://www.codewars.com/kata/5ab349e01aaf060cd0000069/train/java

public class JomoPipi {
    public static String antiString(String str) {
        String swapped = swapCase(str);
        String digitComplementOutput = digitComplement(swapped);
        String alphabetComplementOutput = alphabetComplement(digitComplementOutput);
        return reverseString(alphabetComplementOutput);
    }

    private static String swapCase(String str) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char chr = str.charAt(i);
            if (Character.isLetter(chr)) {
                if (Character.isUpperCase(chr)) {
                    output.append(Character.toLowerCase(chr));
                } else {
                    output.append(Character.toUpperCase(chr));
                }
                continue;
            }
            output.append(chr);
        }
        return output.toString();
    }

    private static String digitComplement(String str) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char chr = str.charAt(i);
            if (Character.isDigit(chr)) {
                output.append(9 - (chr - 48));
            } else {
                output.append(chr);
            }
        }
        return output.toString();
    }

    private static String alphabetComplement(String str) {
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char chr = str.charAt(i);
            if (Character.isLetter(chr)) {
                if (Character.isUpperCase(chr)) {
                    output.append((char) ('Z' - (chr - 'A')));
                } else {
                    output.append((char) ('z' - (chr - 'a')));
                }
                continue;
            }
            output.append(chr);
        }
        return output.toString();
    }

    private static String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}