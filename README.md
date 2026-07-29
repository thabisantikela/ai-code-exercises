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

