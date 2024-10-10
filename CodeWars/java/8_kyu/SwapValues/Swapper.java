// https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/train/java

class Swapper {
    public Object[] arguments;

    public Swapper(final Object[] args) {
        arguments = args;
    }

    public void swapValues() {
        Object temp = arguments[0];
        arguments[0] = arguments[1];
        arguments[1] = temp;
    }
}