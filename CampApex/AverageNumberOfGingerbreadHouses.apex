/*Do not change the name of the class or the method signature.*/

public class CampApexSolution {
    public Decimal calculateAverageHousesPerStreet(List<Integer> streetHouseCounts){
        if (streetHouseCounts == null || streetHouseCounts.size() == 0) {
            return 0;
        }
        Decimal total = 0;
        for (Integer count : streetHouseCounts) {
            total += count;
        }
        return (Decimal) total / streetHouseCounts.size();
    }
}