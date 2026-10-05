public class CampApexSolution {
    public Integer removeAndReturn(Map<String, Integer> inventory, String item) 
        return inventory.containsKey(item) ? inventory.remove(item) : 0;
    }
}