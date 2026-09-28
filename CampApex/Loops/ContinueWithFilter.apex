public class CampApexSolution {
    public Decimal sumClosedWonAmount(List<Opportunity> opportunities) {
        Decimal total = 0;
        for (Opportunity opp : opportunities) {
            if (opp.StageName == 'Closed Won') {
                total += opp.Amount;
            }
        }
        return total;
    }
}