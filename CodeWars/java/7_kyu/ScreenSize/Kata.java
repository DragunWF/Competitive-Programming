// https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f/train/java

class Kata {
    public static String findScreenHeight(int width, String ratio) {
        String[] ratioNums = ratio.split(":");
        double firstRatioNum = Double.parseDouble(ratioNums[0]);
        double secondRatioNum = Double.parseDouble(ratioNums[1]);
        int calculatedHeight = (int) (width * (secondRatioNum / firstRatioNum));
        return String.format("%sx%s", width, calculatedHeight);
    }
}