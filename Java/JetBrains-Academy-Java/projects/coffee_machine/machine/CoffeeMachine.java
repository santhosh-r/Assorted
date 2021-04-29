package machine;
import java.util.Scanner;

public class CoffeeMachine {
    enum State {
        BUY, FILL, OFF, ON
    }

    int water = 400;
    int milk = 540;
    int coffeeBeans = 120;
    int cups = 9;
    int money = 550;
    State state = State.ON;

    private static int fillAction = 0;

    public boolean isTurnedOff() {
        return this.state == State.OFF;
    }

    public void prompt() {
        if (this.state == State.ON) {
            System.out.println("\nWrite action (buy, fill, take, remaining, exit):");
        }
    }

    public void handle(String input) {
        if (state == State.BUY) {
            switch (input) {
                case "1":
                    makeCoffee("espresso", 250, 0, 16, 4);
                    break;
                case "2":
                    makeCoffee("latte", 350, 75, 20, 7);
                    break;
                case "3":
                    makeCoffee("cappuccino", 200, 100, 12, 6);
                    break;
                case "back":
                    break;
                default:
                    System.out.println("Invalid choice");
            }
            this.state = State.ON;
            return;
        }
        if (state == State.FILL) {
            int amount = Integer.parseInt(input);
            fillAction++;
            switch (fillAction) {
                case 1:
                    this.water += amount;
                    System.out.println("\nWrite how many ml of milk do you want to add:");
                    break;
                case 2:
                    this.milk += amount;
                    System.out.println("\nWrite how many grams of coffee beans do you want to add:");
                    break;
                case 3:
                    this.coffeeBeans += amount;
                    System.out.println("\nWrite how many disposable cups of coffee do you want to add:");
                    break;
                default:
                    this.cups += amount;
                    fillAction = 0;
                    this.state = State.ON;
            }
            return;
        }
        switch (input) {
            case "buy":
                this.state = State.BUY;
                System.out.println("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:");
                break;
            case "fill":
                this.state = State.FILL;
                System.out.println("\nWrite how many ml of water do you want to add:");
                break;
            case "take":
                System.out.println("I gave you " + money);
                money = 0;
                break;
            case "remaining":
                displayStatus();
                break;
            case "exit":
                this.state = State.OFF;
                break;
            default:
                System.out.println("Invalid input");
        }
    }

    private void displayStatus() {
        System.out.println("The coffee machine has:");
        System.out.println(this.water + " of water");
        System.out.println(this.milk + " of milk");
        System.out.println(this.coffeeBeans + " of coffee beans");
        System.out.println(this.cups + " of disposable cups");
        System.out.println(this.money + " of money");
    }

    private void makeCoffee(String name, int water, int milk, int coffeeBeans, int money) {
        if (this.water < water || this.milk < milk || this.coffeeBeans < coffeeBeans) {
            System.out.println("Not enough ingredients for " + name);
            return;
        }
        this.water -= water;
        this.milk -= milk;
        this.coffeeBeans -= coffeeBeans;
        this.money += money;
        this.cups--;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CoffeeMachine machine = new CoffeeMachine();

        while (!machine.isTurnedOff()) {
            machine.prompt();
            machine.handle(scanner.next());
        }
    }
}