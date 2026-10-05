public class CampApexSolution {
    public String createColorMap(String colorName) {
        // Create a Map and add color entries using put()
        // Return the hex code for colorName using get()
        Map<String, String> colorMap = new Map<String, String>();
        colorMap.put('Red', 'FF0000');
        colorMap.put('Green', '00FF00');
        colorMap.put('Blue', '0000FF');
        return colorMap.get(colorName);
    }
}