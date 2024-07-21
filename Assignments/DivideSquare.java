import java.util.Scanner;

public class DivideSquare {

	public static double divideOrSquare(int number) {

		if (number % 5 == 0) {
			return Math.sqrt(number);
		}
		else{
			return number % 5;
		}
}


	public static void main(String [] args){
	
		Scanner scanner = new Scanner(System.in);
		

		System.out.print("Enter a number: ");
		int number = scanner.nextInt();

		double result = divideOrSquare(number);

		System.out.println("Result: " + result);
		

	}


}