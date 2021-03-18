

public class ShapePrinter {
    public void printTriangle(int height) {
        String star = "*";
        for (int i=1; i<=height; i++) {
            System.out.println(star);
            star += " *";
        }
    }
}
