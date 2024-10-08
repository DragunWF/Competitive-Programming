// https://www.codewars.com/kata/591588d49f4056e13f000001/train/java

public class HQ {
    public static String HQ9(char code) {
        switch (code) {
            case 'H':
                return "Hello World!";
            case 'Q':
                return String.valueOf(code);
            case '9':
                return bottlesOfBeer();
            default:
                return null;
        }
    }

    private static String bottlesOfBeer() {
        StringBuilder output = new StringBuilder();
        for (int i = 99; i >= 2; i--) {
            output.append(String.format("%s bottles of beer on the wall, %s bottles of beer.\n", i, i));
            if (i != 2) {
                output.append(
                        String.format("Take one down and pass it around, %s bottles of beer on the wall.\n", i - 1));
            }
        }
        output.append("Take one down and pass it around, 1 bottle of beer on the wall.\n");
        output.append("1 bottle of beer on the wall, 1 bottle of beer.\n");
        output.append("Take one down and pass it around, no more bottles of beer on the wall.\n");
        output.append("No more bottles of beer on the wall, no more bottles of beer.\n");
        output.append("Go to the store and buy some more, 99 bottles of beer on the wall.");
        return output.toString();
    }
}