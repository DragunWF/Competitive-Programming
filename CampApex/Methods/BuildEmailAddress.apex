public class CampApexSolution {
   public String buildEmail(String firstName, String lastName, String domain) {
      List<String> formatted = new List<String>{
         firstName, lastName, domain
      };
      return String.format('{0}.{1}@{2}', formatted).toLowerCase();
   }
}