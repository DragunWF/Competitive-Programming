// https://www.codewars.com/kata/58941fec8afa3618c9000184/train/java

public class SimpleFun {
    public static int growingPlant(int upSpeed, int downSpeed, int desiredHeight) {
        int days = 0, plantHeight = 0;
        while (true) {
            plantHeight += upSpeed;
            days++;
            if (plantHeight >= desiredHeight)
                break;
            plantHeight -= downSpeed;
        }
        return days;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(growingPlant(100, 10, 910));
    }
}