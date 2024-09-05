import java.util.Scanner;

public class Metrlar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int L = scanner.nextInt();
        System.out.println(L / 100);
        scanner.close();
    }
}