public class Rectangle {
    public Integer width;
    public Integer height;

    public Rectangle(Integer width, Integer height) {
        this.width = width;
        this.height = height;
    }

    public Integer getArea() {
        return this.width * this.height;
    }

    public Integer getPerimeter() {
        return width * 2 + height * 2;
    }
}