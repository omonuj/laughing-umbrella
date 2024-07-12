import java.util.Scanner;

public class BankAccount {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int balance = 0;

        System.out.println("Enter transaction Type (D for deposit, W for withdrawal). Type 'done' to finish:");

        while (true) {
            System.out.print("Enter transaction type (D/W) or 'done' to finish: ");
            String type = scanner.nextLine().trim();

            if (type.equalsIgnoreCase("done")) {
                break;
            }

            if (!type.equalsIgnoreCase("D") && !type.equalsIgnoreCase("W")) {
                System.out.println("Invalid transaction type. Please use 'D' for deposit and 'W' for withdrawal.");
                continue;
            }

            System.out.print("Enter amount: ");
            int amount;
            try {
                amount = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("Invalid amount. Please enter a valid number.");
                continue;
            }

            if (type.equalsIgnoreCase("D")) {
                balance += amount;
                System.out.println("Deposited: " + amount + ", Balance: " + balance);
            } else {
                if (amount > balance) {
                    System.out.println("Insufficient funds for withdrawal of " + amount + ". Current balance: " + balance);
                } else {
                    balance -= amount;
                    System.out.println("Withdrew: " + amount + ", Balance: " + balance);
                }
            }
        }

        System.out.println("Final net balance in the bank account: " + balance);

    }
}