class Solution {
    public Id getAccountWithHighestTotalOppAmount(List<Opportunity> opportunityList){
        Id chosenAccountId;
        Decimal highestAmount = 0;
        for (Opportunity opportunity : opportunityList) {
            if (opportunity.Amount > highestAmount) {
                highestAmount = opportunity.Amount;
                chosenAccountId = opportunity.AccountId;
            }
        }
        return chosenAccountId;
    }
}