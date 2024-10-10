// https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/java

public class Block {
    private int width, length, height;

    public Block(int[] values) {
        this.width = values[0];
        this.length = values[1];
        this.height = values[2];
    }

    public int getWidth() {
        return width;
    }

    public int getLength() {
        return length;
    }

    public int getHeight() {
        return height;
    }

    public int getVolume() {
        return width * length * height;
    }

    public int getSurfaceArea() {
        return 2 * (width * length + width * height + length * height);
    }
}