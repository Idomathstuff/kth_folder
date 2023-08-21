import java.util.Arrays;
import java.lang.Math;

public class Main {
    static double[] pointpos = {-4,4,-5};
    static double[] campos = {0,-4,0};
    static double S = 1;
    static double theta = (110/180)*Math.PI;
    static double d = S/(2*Math.tan(theta/2));
    static double x_c = campos[0], y_c = campos[1], z_c = campos[2];

    public static double[] proj(double[] pointpos, double[] campos, double S, double theta) {
        double d = S/(2*Math.tan(theta/2));
        double x_c = campos[0], y_c = campos[1], z_c = campos[2];
        double x_p = pointpos[0], y_p = pointpos[1], z_p = pointpos[2];
        double[] shift = {d*(x_p-x_c)/(y_p-y_c), d, d*(z_p-z_c)/(y_p-y_c)};
        double[] result = new double[3];
        for (int i = 0; i < 3; i++) {
            result[i] = campos[i] + shift[i];
        }
        return result;
    }

    public static class Screen {
        double stepsize = 0.04;
        int N = (int) (S/stepsize);
        double[] left_corner = {-S/2,y_c+d,S/2};
        char[][] grid = new char[N][N];

        public void project(double[] pointpos) {
            double[] points = proj(pointpos, campos, S, theta);
            if (-S/2 <= points[0] && points[0] <= S/2 && -S/2 <= points[2] && points[2] <= S/2) {
                // pass
            } else {
                return;
            }
            double shift_x = Math.abs(points[0] - left_corner[0]);
            double shift_z = Math.abs(points[2] - left_corner[2]);
            int shift_x_n = (int) (shift_x/stepsize);
            int shift_z_n = (int) (shift_z/stepsize);
            grid[shift_z_n][shift_x_n] = 'P';
        }

        public void display() {
            for (char[] row : grid) {
                for (char elmnt : row) {
                    System.out.print(elmnt + " ");
                }
                System.out.println();
            }
        }
    }

    public static void main(String[] args) {
        Screen scr = new Screen();
        scr.project(pointpos);
        scr.display();
    }
}