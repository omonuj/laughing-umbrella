import java.util.Scanner;

public class Multiplication {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        
       
        System.out.print("Enter a number to create its multiplication table: ");
        int number = scanner.nextInt();
        
       
        System.out.println("Multiplication table for " + number + ":");
        for (int base = 1; base <= 10; base++) {
            System.out.println(number + " x " + base + " = " + (number * base));
        }
        
        
    }
}
