// https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/java

public class GrassHopper {
    public static char getGrade(int s1, int s2, int s3) {
        double avg = (s1 + s2 + s3) / 3;
        if (avg < 60)
            return 'F';
        if (avg < 70)
            return 'D';
        if (avg < 80)
            return 'C';
        if (avg < 90)
            return 'B';
        return 'A';
    }
}
