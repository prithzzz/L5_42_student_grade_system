# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type / Severity | Location in Original Code | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `eval()` usage | Security / High | `compute_weighted_gpa()` | Evaluating an expression supplied as a string can execute arbitrary Python code. | Removed `eval()` and implemented the GPA formula directly. |
| Shell command execution | Security / Medium | `export_grade_sheet()` | `os.system()` executes a shell command using a filename that could contain malicious input. | Removed shell execution and used `pathlib` for file handling. |
| Weak MD5 hashing | Security / Medium | `generate_student_hash()` | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Predictable PIN generation | Security / Medium | `generate_registration_pin()` | The standard `random` module is not designed for security-sensitive tokens. | Used the `secrets` module to generate the PIN. |
| Mutable default argument | Bug / Medium | `addGrade()` | The default `grade_list=[]` is shared across function calls. | Changed the default to `None` and initialize a new list inside the function. |
| Bare exception handler | Code quality / Medium | `record_attendance()` | `except:` catches every exception and hides unexpected errors. | Removed broad exception handling and added explicit input and record validation. |
| Unclosed file handling | Code quality / Low | `export_grade_sheet()` | Manual file handling can leave resources open if an error occurs. | Used a `with` statement to manage the file safely. |
| Hardcoded token | Security / High | `main()` | A portal token is embedded in the source code and printed to the terminal. | Removed the hardcoded token and its output. |
| Inconsistent formatting and naming | Style / Low | Multiple functions | Non-standard naming, spacing, and string formatting reduce readability. | Used snake_case, f-strings where appropriate, and consistent formatting. |

## Verification

The corrected program was analyzed again using Pylint, Bandit, and Flake8. The final reports were generated after the fixes. The results should be checked against the actual report files before submission.