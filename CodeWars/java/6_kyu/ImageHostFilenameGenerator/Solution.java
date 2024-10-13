// https://www.codewars.com/kata/586a933fc66d187b6e00031a/train/java

public class Solution {
    private static String pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~\r\n";

    public static String generateName(PhotoManager photoManager) {
        StringBuilder code = new StringBuilder();
        for (int i = 0; i < 6; i++) { // Fixed value of 6 characters per code
            code.append(pool.charAt((int) Math.floor(Math.random() * pool.length())));
        }
        return photoManager.nameExists(code.toString()) ? generateName(photoManager) : code.toString();
    }
}

class PhotoManager {
    public boolean nameExists(String name) {
        return false; // placeholder to avoid angering intellisense
    }
}