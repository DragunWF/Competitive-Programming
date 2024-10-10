// https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/java

public class Movie {
    public static int movie(int card, int ticket, double perc) {
        int ticketCount = 1;
        double totalTicketPrice = card + ticket * perc;
        while (ticketCount * ticket < Math.ceil(totalTicketPrice)) {
            int cardTicketPrice = ticket;
            for (int i = 0; i < ticketCount; i++) {
                cardTicketPrice *= perc;
            }
            totalTicketPrice += cardTicketPrice;
            ticketCount++;
        }
        return ticketCount;
    }

    public static void main(String[] args) {
        // Not part of the solution, just testing
        System.out.println(movie(500, 3, 0.9));
    }
}