public class CustomerHelper {
    private String customerName = 'Bob';

    public void greetCustomer() {
        String customerName = 'Bob';
        System.debug('Hello, ' + customerName + '!');
    }

    public void sendMessage() {
        System.debug('Message sent to ' + customerName);
    }
}