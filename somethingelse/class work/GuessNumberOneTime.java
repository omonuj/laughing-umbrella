import java.util.Scanner;
public class GuessNumberOneTime {

	public static void main(String [] args) {
	Scanner scanner = new Scanner(System.in);

	int number = (int)(Math.random() * 101);

	System.out.print("Guess a magic number between 0 and 100");
	
	int guess = 0;	

	while (guess != number) {
	System.out.print("\nEnter your guess: ");
	guess = scanner.nextInt();

	if (guess == number)
	System.out.println("Yes, the number is: "+number);
	else if (guess > number)
	System.out.println("Your guess is too high");
	else 
	System.out.println("Your guess is too low");
	}

	}

}