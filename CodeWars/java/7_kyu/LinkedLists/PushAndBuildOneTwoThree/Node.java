// https://www.codewars.com/kata/55be95786abade3c71000079/train/java

class Node {
    int data;
    Node next = null;

    Node(final int data) {
        this.data = data;
    }

    public static Node push(final Node head, final int data) {
        if (head == null) {
            return new Node(data);
        }
        Node createdNode = new Node(data);
        createdNode.next = head;
        return createdNode;
    }

    public static Node buildOneTwoThree() {
        Node head = new Node(1);
        Node node = head;
        for (int i = 2; i <= 3; i++) {
            node.next = new Node(i);
            node = node.next;
        }
        return head;
    }

    public static void main(String[] args) {
        // test code, not part of the solution
        System.out.println(Node.push(new Node(1), 2).next.data);
    }
}
