// https://www.codewars.com/kata/582afcadac2d9baa0900054c/train/java

import java.util.Collections;
import java.util.ArrayList;
import java.util.HashSet;

public final class PokerHand {
    public static boolean IsStraight(ArrayList<Integer> cards) {
        if (cards.size() < 5) {
            return false;
        }
        cards = removeDuplicates(cards);

        Collections.sort(cards);
        boolean isSecondSetStraight = false;
        if (cards.contains(14)) {
            ArrayList<Integer> secondCardSet = new ArrayList<>(cards);
            secondCardSet.set(secondCardSet.size() - 1, 1);
            Collections.sort(secondCardSet);
            System.out.println(secondCardSet);
            isSecondSetStraight = isFiveInOrder(secondCardSet);
        }
        return isSecondSetStraight || isFiveInOrder(cards);
    }

    public static ArrayList<Integer> removeDuplicates(ArrayList<Integer> cards) {
        HashSet<Integer> unique = new HashSet<>(cards);
        return new ArrayList<>(unique);
    }

    public static boolean isFiveInOrder(ArrayList<Integer> cards) {
        int prevNum = cards.get(0);
        int inOrder = 1;

        for (int i = 1; i < cards.size(); i++) {
            int currentNum = cards.get(i);
            if (currentNum - prevNum == 1) {
                inOrder++;
            } else {
                inOrder = 1;
            }
            if (inOrder == 5) {
                return true;
            }
            prevNum = currentNum;
        }

        return inOrder >= 5;
    }

    public static void main(String[] args) {
        // This is for testing. It is not part of the solution!
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(7);
        arr.add(8);
        arr.add(9);
        arr.add(10);
        arr.add(11);
        System.out.println(IsStraight(arr)); // true

        arr.clear();
        arr.add(7);
        arr.add(7);
        arr.add(12);
        arr.add(11);
        arr.add(14);
        System.out.println(IsStraight(arr)); // false

        arr.clear();
        arr.add(14);
        arr.add(5);
        arr.add(4);
        arr.add(2);
        arr.add(3);
        System.out.println(IsStraight(arr)); // true

        arr.clear();
        arr.add(13);
        arr.add(14);
        arr.add(4);
        arr.add(3);
        arr.add(5);
        arr.add(2);
        arr.add(2);
        System.out.println(IsStraight(arr)); // true
    }
}