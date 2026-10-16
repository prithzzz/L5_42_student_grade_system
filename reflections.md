# Lab 5: Static Code Analysis - Reflections

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were formatting violations, inconsistent naming, and the mutable default argument. These required simple changes to improve code readability and prevent shared state between function calls. The hardest issues were security vulnerabilities such as unsafe `eval()` usage and shell command execution because they required replacing unsafe operations while preserving the program's functionality.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

A potential false positive could occur when a static analysis tool flags a code pattern that is safe in its specific context. For example, Bandit might flag a function that executes a shell command even when its arguments are controlled and validated. However, this does not necessarily mean the finding is a false positive, since unsafe input could still introduce vulnerabilities. Each warning should be reviewed before deciding whether it is a genuine issue.

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate Pylint, Bandit, and Flake8 into my development workflow by running them before committing code and including them in a CI/CD pipeline using GitHub Actions. Pylint would check code quality, Bandit would identify security vulnerabilities, and Flake8 would enforce consistent coding standards. This would help detect problems early and prevent code with serious issues from being merged into the main branch.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The fixes improved code readability through consistent naming, formatting, and documentation. Removing unsafe `eval()` usage and shell command execution reduced potential security risks. Replacing MD5 with SHA-256 and predictable random number generation with the `secrets` module improved the security of the relevant operations. Input validation and safer file handling also made the program more robust by reducing the likelihood of invalid inputs and unexpected failures.