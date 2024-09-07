// https://www.codewars.com/kata/62ad72443809a4006998218a/train/java

import preloaded.Button;
import static preloaded.Button.*; // Like, Dislike, Nothing

public class Solution {
    public static Button likeOrDislike(Button[] buttons) {
      if (buttons.length == 0) return Nothing;
      Button selected = buttons[0];
      for (int i = 1; i < buttons.length; i++) {
        if (selected != buttons[i]) {
          selected = buttons[i];
        } else {
          selected = Nothing;
        }
      }
      return selected;
    }
}