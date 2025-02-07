// https://www.codewars.com/kata/566dc566f6ea9a14b500007b/train/java

import java.util.List;
import java.util.ArrayList;

public class Kata13December {
    public static List<Integer> filterOddNumber(List<Integer> listOfNumbers)
    {
        ArrayList<Integer> filteredNumbers = new ArrayList<>();
        for (int i = 0; i < listOfNumbers.size(); i++)
        {
            if (listOfNumbers.get(i) % 2 != 0)
            {
                filteredNumbers.add(listOfNumbers.get(i));
            }
        }
        return filteredNumbers;
    }
}