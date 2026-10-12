public class Shape {
    // Add virtual getArea() method
    public virtual Decimal getArea() {
        return 0;
    }

    // Add virtual getName() method
    public virtual String getName() {
        return 'Shape';
    }
}

public class Rectangle extends Shape {
    // Add width and height variables
    public Decimal width;
    public Decimal height;

    // Add constructor
    public Rectangle(Decimal width, Decimal height) {
        this.width = width;
        this.height = height;
    }

    // Override getArea() method
    public override Decimal getArea() {
        return width * height;
    }

    // Override getName() method
    public override String getName() {
        return 'Rectangle';
    }
}