import java.util.Arrays;
import java.util.Scanner;

public class EqualStrings{

	public static Boolean equalStrings(String word1, String word2){

	if (word1.length() != word2.length()) {
		return false;
	}
	
	char[] charArray1 = word1.toCharArray();
	char[] charArray2 = word2.toCharArray();

	Arrays.sort(charArray1);
	Arrays.sort(charArray2);


	return Arrays.equals(charArray1, charArray2);	
}

	public static void main(String [] args){

	Scanner scanner = new Scanner(System.in);

	System.out.print("Enter the first string: ");
	String word1 = scanner.nextLine();

	System.out.print("Enter the second string: ");
	String word2 = scanner.nextLine();

	Boolean result = equalStrings(word1, word2);

	System.out.println("The strings are equal in characters and length: " + result);
}

}