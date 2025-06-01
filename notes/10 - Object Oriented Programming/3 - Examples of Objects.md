# Examples of Objects

_This section is not yet complete_

Most learners find it easy to understand the basic examples. You are perhaps also getting tired of hearing the same examples. Person contains Name, Address. I get this. Is there any use of Objects in the real world? Can you give me an example of Object Oriented Programming in the real world?

This is where programmers need to learn the art of thinking in abstractions.

# Example 1 - Windows, Menus and Buttons

Let us consider the browser where you are viewing this page. The browser is a window among several windows open. Each of these windows has a title bar with close, minimize, maximize buttons. There are a few menu options with several actions. There is also perhaps a toolbar and/or a statusbar.

Now, when we design these windows, we can use Object Oriented programming. Window, Menu, MenuItem, Toolbar, Statusbar, Button etc are all objects. A Window contains Menu, a Menu contains MenuItem etc.

```
class Window:
 List<Menu> menu

class Menu:
 List<MenuItem> menuItems
```

Some people like to think of Objects as "Nouns" in the system.

# Example 2 - An Operating System

When we talk about an Operating System, we talk about things like Process Management (a sub-system that can handle various processes in the OS), Memory Management (a sub-system that handles the memory of the system), Network Management (a sub-system responsible for managing the network hardware and interactions) etc.

ProcessManager, MemoryManager, NetworkManager are classes that can handle this. A ProcessManager manages Process's, where Process's are also objects. A Process contains a processID, a processOwner etc.

```
class ProcessManager
 List<Process> processes
...

class Process
 int processID
 String processOwner
...
```