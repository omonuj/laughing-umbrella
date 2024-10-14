import java.util.Scanner;

public class OnlyFloats {

	public static double onlyFloats(Object a, Object b){
	
	
	if (a instanceof Float && b instanceof Float) {
		return 2;
	}
	else if (a instanceof Float || b instanceof Float) {
		return 1;
	}
	else {
		return 0;
	}

	}

	public static void main(String [] args) {

	Scanner scanner = new Scanner(System.in);

	System.out.print("Enter the first values: ");
	String firstValue = scanner.nextLine();
	System.out.print("Enter the second values: ");
	String secondValue = scanner.nextLine();

	Object a, b;
	try {
		a = Float.parseFloat(firstValue);
	}
	catch (NumberFormatException e) {
		a = firstValue;
	}

	try {
		b = Float.parseFloat(secondValue);
	}
	catch (NumberFormatException e) {
		b = secondValue;
	}

	double result = onlyFloats(a, b);
	System.out.println("The Result is: " + result);

	}

}