![Alt text](/LogPage.png)
![Alt text](/WorkoutsPage.png)
# MY FINAL PROJECT
A one or two sentence description of your project here.
- What does it do?

It's a gym application that contains exercises for 5 muscle groups, users can sign up on it, and save daily logs to their workouts.

- What is the "new feature" which you have implemented that
we haven't seen before?
Example: "Chart drawing library graphs the user data"
## Prerequisites
Did you add any additional modules that someone needs to
install (for instance anything in Python that you `pip
install-ed`)?

## Dependencies
```bash
pip3 install flask_login
pip3 install flask_sqlalchemy
```
## How to run
### Normal Mode
```bash
flask --app main run
```
### Debug Mode
```bash
flask --app main --debug run
```
## Project Checklist
- [*] It is available on GitHub. 
- [*] It uses the Flask web framework.
- [*] It uses at least one module from the Python Standard
Library other than the random module.
Please provide the name of the module you are using in your
app.

- Module names:

```python3
datetime
os
json
calendar
```
- [*] It contains at least one class written by you that has
both properties and methods. It uses `__init__()` to let the
class initialize the object's attributes (note that
`__init__()` doesn't count as a method). This includes
instantiating the class and using the methods in your app.
Please provide below the file name and the line number(s) of
at least one example of a class definition in your code as
well as the names of two properties and two methods.

- File name for the class definition:

** models.py **

- Line number(s) for the class definition:

4

- Name of two properties:

1- username 
2- email

- Name of two methods:

1- get_weight()
2- get_height()

- File name and line numbers where the methods are used:
profile.html, lines 39 and 40

- [*] It makes use of JavaScript in the front end and uses the
localStorage of the web browser.
- [*] It uses modern JavaScript (for example, let and const
rather than var).
- [*] It makes use of the reading and writing to the same file
feature.
- [] It contains conditional statements. Please provide below
the file name and the line number(s) of at least
one example of a conditional statement in your code.
- File name:

email_validation.py

- Line number(s):

5 

- [*] It contains loops. Please provide below the file name
and the line number(s) of at least
one example of a loop in your code.
- File name:

profile.html

- Line number(s):

55 

- [*] It lets the user enter a value in a text box at some
point.
This value is received and processed by your back end
Python code.
- [*] It doesn't generate any error message even if the user
enters a wrong input.
- [*] It is styled using your own CSS.
- [*] The code follows the code and style conventions as
introduced in the course, is fully documented using comments
and doesn't contain unused or experimental code.
In particular, the code should not use `print()` or
`console.log()` for any information the app user should see.
Instead, all user feedback needs to be visible in the
browser.
- [*] All exercises have been completed as per the
requirements and pushed to the respective GitHub repository.
