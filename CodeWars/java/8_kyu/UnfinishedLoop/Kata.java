// https://www.codewars.com/kata/55c28f7304e3eaebef0000da

import java.util.*;

class Kata {
    public static List CreateList(int number) {
        List list = new ArrayList();

        for (int count = 1; count <= number; count++) {
            list.add(count);
        }

        return list;
    }
}