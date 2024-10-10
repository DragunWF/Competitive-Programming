// https://www.codewars.com/kata/55befc42bfe4d13ab1000007/train/java

class Node {
    public int data;
    public Node next = null;

    public static int getNth(Node head, int index) throws Exception {
        int i = 0;
        for (Node node = head; node != null; node = node.next, i++) {
            if (i == index) {
                return node.data;
            }
        }
        throw new Exception();
    }
}
