# ai-code-exercises

Code Exercises for AI Course for Software Engineers.

This is still a work in progress - the idea is to capture the various exercise starter code examples in here.

## Exercises

 Use Case | Exercise | Instructions | Starter Code |
| --- | --- | --- | --- |
| Code Comprehension | Code Explore Challenge | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-code-comprehension-001/) | [Starter Code](use-cases/code-comprehension-001/README.md) |
| Code Comprehension | Algorithm Deconstruction Challenge | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-code-algorithms/) | [Starter Code](use-cases/code-algorithms/README.md) |
| Code Comprehension | Knowing Where to Start | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-code-comprehension-002/) | [Starter Code](use-cases/code-algorithms/README.md) |
| Documenting Code | Code Documentation | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-doc-code/) | [Starter Code](use-cases/code-algorithms/README.md) |
| Documenting Code |README documentation | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-doc-readme/) | [Starter Code](use-cases/code-algorithms/README.md) |
| Debugging | Error Diagnosis Challenge | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-debug-errors-001/) | [Starter Code](use-cases/debug-errors-001/README.md) |
| Debugging | Performance Optimization Challenge | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-code-performance/) | [Starter Code](use-cases/debug-performance/README.md) |
| Debugging | AI Solution Verification Challenge | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-debug-limitations/) | [Starter Code](use-cases/debug-limitations/README.md) |
| Testing | Using AI to help with testing | [Instructions](https://ai.wethinkco.de/ai-software/ai-use-cases/exercises/exercise-testing-001/) | [Starter Code](use-cases/testing-001) |
| [Starter Code]()
## My Code Explore Challenge Solution

**File**: [TaskManagerCli.java](./use-cases/TaskManagerCli.java)

**What it does:**
- Runs as a command-line Task Manager in Java
- Lets users add new tasks with a title
- Lists all tasks with status "PENDING" and priority "MEDIUM"
- Built for the WTC_AI Curriculum Code Explore Challenge
## Exercise 2: Algorithm Deconstruction Challenge

**Q1: What was the original problem, and what did you identify as the core components?**
The original problem was to sort a list of tasks by importance. The core components I identified were: the TaskPriority enum, the Task class with title/priority/dueDate/isCompleted, the calculateTaskScore method, and the sortTasksByPriority method.

**Q2: Explain the logic behind calculateTaskScore. Why does it work?**
The method gives points based on priority: LOW=1, MEDIUM=2, HIGH=4, URGENT=6. It adds +10 if the task is overdue and +5 if it's due today. It subtracts 50 if the task is already completed. It works because sorting by the highest score puts the most urgent tasks first.

**Q3: How could this algorithm be improved for a real-world application?**
It could be improved by adding more factors like task category, estimated time to complete, or letting users set custom weights. Also, instead of sorting the original list, it should return a new sorted list to avoid side effects.

## Exercise 3: Error Diagnosis Challenge

### Bug Selected: StackOverflowException in FactorialCalculator.java

**1. Error Description:**
`java.lang.StackOverflowError` means the program crashed because the call stack got full. The error kept repeating `at com.example.recursion.Factorial` over and over.

**2. Root Cause:**
The `calculateFactorial` method has no base case. It calls itself forever: `return num * calculateFactorial(num)` without ever stopping or making `num` smaller.

**3. Suggested Solution:**
Add a base case and decrease num in each recursive call.
```java
public static int calculateFactorial(int num) {
    // Base case - stops the recursion
    if (num <= 1) {
        return 1;
    }
    // Recursive case - gets closer to base case
    return num * calculateFactorial(num - 1);
}



## Reflection Questions

**Q1: How has your approach to using AI for code changed?**
I used to ask AI to just write code for me. Now I use it to explain errors, debug, and understand why code works. I use it as a learning partner.

**Q2: What challenges did you face and how did you overcome them?**
Understanding recursion and StackOverflow was hard. I overcame it by asking AI to explain the stack trace and what a "base case" means.

**Q3: How will you apply these skills in your projects?**
I will use AI to debug faster by pasting errors, to explain new algorithms, and to help me document my code better for my team.

**Q4: What was the most valuable thing you learned?**
That error messages tell you exactly what's wrong. When a method repeats 1000 times in the stack trace, it's infinite recursion. Also, asking specific questions to AI gives better answers.


