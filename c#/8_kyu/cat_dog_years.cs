public class Dinglemouse {
  public static int[] humanYearsCatYearsDogYears(int humanYears) {
    var catYears = CalculateYears(humanYears, "cat");
    var dogYears = CalculateYears(humanYears, "dog");
    return new int[]{humanYears, catYears, dogYears};
  }
  
  static int CalculateYears(int humanYears, string type) {
    var animalYears = 0;
    for (var i = 1; i <= humanYears; i++) {
      if (i == 1) animalYears += 15;
      else if (i == 2) animalYears += 9;
      else animalYears += type == "cat" ? 4 : 5; 
    }
    return animalYears;
  }
}

// https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/csharp