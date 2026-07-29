import java.util.ArrayList;
import java.util.Scanner;

class Task {
    String name;
    String priority;
    String status;
    
    Task(String name) {
        this.name = name;
        this.priority = "MEDIUM";
        this.status = "PENDING";
    }
    
    public String toString() {
        return name + " | " + priority + " | " + status;
    }
}

public class TaskManagerCli {
    static ArrayList<Task> tasks = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        System.out.println("TaskManager CLI is running!");
        while(true) {
            System.out.println("\n1. Add Task 2. List Tasks 3. Exit");
            System.out.print("Choose: ");
            String choice = scanner.nextLine();
            
            if(choice.equals("1")) {
                System.out.print("Task name: ");
                String name = scanner.nextLine();
                tasks.add(new Task(name));
                System.out.println("Added!");
            } else if(choice.equals("2")) {
                if(tasks.size() == 0) {
                    System.out.println("No tasks yet");
                } else {
                    for(int i=0; i<tasks.size(); i++) {
                        System.out.println((i+1) + ". " + tasks.get(i));
                    }
                }
            } else if(choice.equals("3")) {
                System.out.println("Goodbye!");
                break;
            } else {
                System.out.println("Invalid choice");
            }
        }
    }
}
