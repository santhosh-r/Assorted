/*
https://hyperskill.org/learn/step/3791#solutions-858979

Processing strings
Create an euphonious word
Hard 29 minutes
1411 users solved this problem. Latest completion was 1 day ago.

All the letters of the English alphabet are divided into vowels and consonants.
The vowels are: a, e, i, o, u, y.
The remaining letters are consonants.

A word is considered euphonious (pleasant-sounding) if it doesn't have three or more vowels or consonants in a row. Otherwise, it is considered discordant (harsh-sounding).

Your task is to create euphonious words from discordant. You can insert any letters inside the word. You should output the minimum number of characters needed to create a euphonious word from a given word.

For example, the word "schedule" is considered discordant because it has three consonants "sch" in a row. To create a euphonious word you need to add any vowel between 's' and 'c' or between 'c' and 'h'.
*/

import java.util.Scanner;

public class EuphoniousWord {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] letters = scanner.next().split("");
        scanner.close();
        int insertionsNeeded = 0;
        int count = 0;
        for (int i = 0; i < letters.length; i++) {
            count++;
            if (i == letters.length - 1 || "aeiouy".contains(letters[i]) != "aeiouy".contains(letters[i + 1])) {
                insertionsNeeded += (count - 1) / 2;
                count = 0;
            }
        }
        System.out.println(insertionsNeeded);
    }
}
