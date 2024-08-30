// https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/java

public class CuboidVolumes {
    public static int findDifference(final int[] firstCuboid, final int[] secondCuboid) {
        int firstVolume = firstCuboid[0], secondVolume = secondCuboid[0];
        for (int i = 1; i < firstCuboid.length; i++) {
            firstVolume *= firstCuboid[i];
            secondVolume *= secondCuboid[i];
        }
        return Math.abs(firstVolume - secondVolume);
    }
}