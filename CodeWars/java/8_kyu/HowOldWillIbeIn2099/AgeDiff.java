// https://www.codewars.com/kata/5761a717780f8950ce001473/train/java

public class AgeDiff {
    public static String CalculateAge(int birth, int yearTo) {
        int result = yearTo - birth;
        String yearStr = Math.abs(result) > 1 ? "years" : "year";
        if (result == 0)
            return "You were born this very year!";
        return String.format(result < 0 ? "You will be born in %s %s." : "You are %s %s old.", Math.abs(result), yearStr);
    }
}
