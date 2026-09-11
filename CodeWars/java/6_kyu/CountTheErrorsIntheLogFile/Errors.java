// https://www.codewars.com/kata/69c3e9e48e6febc70467113d/train/java

import java.io.IOException;
import java.nio.file.*;
import java.util.*;
import java.util.stream.Collectors;

public class Errors {
  public static LinkedHashMap<String, Integer> mapErrors() {
    LinkedHashMap<String, Integer> errors = new LinkedHashMap<>();
    
    try {
      List<String> lines = Files.readAllLines(Paths.get("server.log"));
      for (String line : lines) {
        if (line.startsWith("ERROR: ")) {
            String key = line.substring(7).toLowerCase();
            if (errors.containsKey(key)) {
                errors.put(key, errors.get(key) + 1);
            } else {
                errors.put(key, 1);
            }
        }
      }
    } catch (IOException e) {
      System.err.println("Error reading the file: " + e.getMessage());
    }
    
    return errors.entrySet()
      .stream()
      .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
      .collect(Collectors.toMap(
          Map.Entry::getKey,
          Map.Entry::getValue,
          (oldValue, newValue) -> oldValue, 
          LinkedHashMap::new                
      ));
  }
}