// https://www.codewars.com/kata/56d49587df52101de70011e4/train/java

public class Kata {
    public static String leo(final int oscar) {
        if (oscar == 88)
            return "Leo finally won the oscar! Leo is happy";
        if (oscar == 86)
            return "Not even for Wolf of wallstreet?!";
        return oscar < 88 ? "When will you give Leo an Oscar?" : "Leo got one already!";
    }
}