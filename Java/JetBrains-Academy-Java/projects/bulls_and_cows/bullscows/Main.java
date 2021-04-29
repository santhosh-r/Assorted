package bullscows;

import java.util.Random;
import java.util.Scanner;

public class Main {
    public static String generateSecretCode(int length, int range) {
        if (range > 36 || length > range) {
            return "";
        }
        boolean[] symbols = new boolean[range];
        StringBuilder result = new StringBuilder();
        Random random = new Random(System.nanoTime());
        int j = 0;
        while (j < length) {
            int s = random.nextInt(range);
            if (symbols[s]) {
                continue;
            }
            symbols[s] = true;
            result.append((char) (s < 10 ? 48 + s : 87 + s));
            j++;
        }
        return result.toString();
    }

    public static boolean evaluateSecretCode(String secretCode, String guess) {
        int bulls = 0;
        int cows = 0;
        for (int i = 0; i < secretCode.length(); i++) {
            if (secretCode.charAt(i) == guess.charAt(i)) {
                bulls++;
            } else if (secretCode.indexOf(guess.charAt(i)) > -1) {
                cows++;
            }
        }
        System.out.print("Grade: ");
        System.out.print(bulls > 0 ? bulls + " bull(s)" : "");
        System.out.print(cows > 0 ? (bulls > 0 ? " and " : "") + cows + " cows(s)" : "");
        System.out.println(bulls == 0 && cows == 0 ? "None." : ".");
        return bulls == secretCode.length();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.println("Input the length of the secret code:");
            int length = scanner.nextInt(); // Possible exception
            System.out.println("Input the number of possible symbols in the code:");
            int range = scanner.nextInt(); // Possible exception
            String secretCode = generateSecretCode(length, range);
            if (secretCode.length() != length || length <= 0) { // Other errors
                System.out.println("Error generating secret code.");
                return;
            }
            System.out.print("The secret is prepared: " + secretCode.replaceAll(".", "*") + " (0-");
            System.out.println(range <= 10 ? range - 1 + ")" : "9, a-" + (char) (86 + range) + ").");
            System.out.println("Okay, let's start a game!");
            int turn = 0;
            do {
                System.out.println("Turn " + ++turn + ":");
            } while (!evaluateSecretCode(secretCode, scanner.next()));  // Possible exception
        } catch (RuntimeException e) {
            System.out.println("error " + e.getClass().getCanonicalName());
            return;
        }
        System.out.println("Congratulations! You guessed the secret code.");
    }
}