public class ZebulansNightmare {
    public static String zebulansNightmare(final String functionName) {
        StringBuilder camelCase = new StringBuilder();
        boolean isWordSeparatorNext = false;
        for (int i = 0, n = functionName.length(); i < n; i++) {
            char currentChar = functionName.charAt(i);
            if (currentChar == '_') {
                isWordSeparatorNext = true;
                continue;
            }
            camelCase.append(isWordSeparatorNext ? String.valueOf(currentChar).toUpperCase() : currentChar);
            isWordSeparatorNext = false;
        }
        return camelCase.toString();
    }
}