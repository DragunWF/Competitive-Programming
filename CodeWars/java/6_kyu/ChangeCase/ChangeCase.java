// https://www.codewars.com/kata/591cac98a6007e87d900013a/train/java

import java.util.ArrayList;

class ChangeCase {   
     public static String toSentenceCase(String string){
         if (string.isEmpty()) {
            return "";
         }
         StringBuilder sb = new StringBuilder();
         ArrayList<String> words = new ArrayList<>();
         for (int i = 0; i < string.length(); i++) {
            char currentChar = string.charAt(i);
            sb.append(currentChar);
            if (currentChar == '!' || currentChar == '.' || currentChar == '?') {
                words.add(ChangeCase.toTitleCase(sb.toString()));
                sb = new StringBuilder();
            }
         }

         if (sb.length() > 0) {
            words.add(ChangeCase.toTitleCase(sb.toString()));
         }
         return String.join("", words);
     }
     
     public static String toLowerCase(String string){
         return string.toLowerCase();
     }
     
     public static String toUpperCase(String string){
         return string.toUpperCase();
     }
    
     public static String capitalizeEachWord(String string){
         String[] words = string.split(" ");
         for (int i = 0; i < words.length; i++) {
            words[i] = ChangeCase.toTitleCase(words[i]);
         }
         return String.join(" ", words);
     }
     
     public static String toToggleCase(String string) {
         StringBuilder sb = new StringBuilder();
         for (int i = 0; i < string.length(); i++) {
            String strChar = String.valueOf(string.charAt(i));
            if (strChar.toUpperCase().equals(strChar)) {
                sb.append(strChar.toLowerCase());
            } else {
                sb.append(strChar.toUpperCase());
            }
         }
         return sb.toString();
     }

     private static String toTitleCase(String string) {
         if (string.isEmpty()) {
            return "";
         }
         int firstLetterIndex = 0;
         if (string.charAt(0) == ' ') {
            firstLetterIndex = 1;
         }
         String firstLetter = String.valueOf(string.charAt(firstLetterIndex)).toUpperCase();
         String output = firstLetter + string.substring(firstLetterIndex + 1).toLowerCase();
         if (firstLetterIndex != 0) {
            output = " " + output;
         }
         return output;
     }
}