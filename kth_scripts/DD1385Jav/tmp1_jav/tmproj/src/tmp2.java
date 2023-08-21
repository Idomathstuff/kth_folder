
class Cube {
    private int width;
    private int height;
    private int length;

    public Cube(int width, int height, int length) {
        this.width = width;
        this.height = height;
        this.length = length;
    }

    public int area() {
        return this.width * this.length * this.height;
    }

    public String toString() {
        return "this cube has area: " + Integer.toString(this.area());
    }
}


class tmp2 {
    public static void main(String[] args) {
        // Cube cubeA = new Cube(1, 1, 1);
        Cube cubeB = new Cube(2, 2, 2);
        System.out.println(cubeB);
    }
}
