# Chapter 5: GUIs

[Prev: Chapter 4 - Web Scraping](./chapter04.md) \| [Next: Chapter 6 - APIs](./chapter06.md)

## Summary:

It's time to get GUI \(pronounced 'goo-ee'\), and I'm not talking about cookie dough.
This chapter is all about getting started with simple Graphical User Interfaces
\(GUIs\) in Python, using the built-in, cross-platform _tkinter_ package.

If you've programmed for more than a few hours in your life, you've probably
asked yourself, "What's up with this lame terminal window? When can I start
making 'normal' applications--with windows and buttons!?" Well, now is the
time to start, and--like most things in Python--it's not daunting at all!

In this chapter, you'll get to study some basic concepts with GUI programming,
learn how to use a handful of the basic widgets supplied by tkinter, and
even learn how to make a basic, but functional text editor!

---

## Content:

Up until this point you've been using the CLI, or Command-Line Interface, but now I'm going to show you how to upgrade to GUI, or Graphical User Interface. GUI is what you're probably used to for everyday tasks on your PC; you open up your browser, text editor, file explorer--all of these use a GUI.

The basic concept of a GUI is a application window, or _frame_, which contains more frames and\/or widgets. Widgets are everything in GUI programming. They are buttons, text fields, scrollbars, images, checkboxes, etc. There are many GUI packages available for Python, but to keep it simply we'll use Python's built-in tkinter.

You won't be making any exotic applications with complicated, custom widgets with tkinter, but it certainly gives enough functionality for most projects. To start though, we just want _something_, even if it's just a blank window. So let's do that:

```python
# Example 5-1 (gui0.pyw)
# A simple 'Hello World' GUI
import tkinter as tk

root = tk.Tk()
root.title('Simple GUI')

my_label = tk.Label(root, text='Hello World!')
my_label.pack()

root.mainloop()
```

First we import tkinter; please note that if you are using Python 2 you should `import Tkinter as tk` (capitalize the T). The `as tk` part just pakes it more convenient to type each time we use a tkinter class (such as *Label*); and it's usually not a good idea to `import * from tkinter`.

The first real step is to create the root application frame, which is the *Tk* class.

`root = tk.Tk()`

Then, for aesthetics, we can set the title to be shown in the title bar of the application:

`root.title('Simple GUI')`

I know I implied we would create a blank window, but one widget won't hurt will it? The next line creates a *Label* which is just a placeholder for text. You typically find labels next to input fields or as static messages to the user.

`my_label = tk.Label(root, text='Hello World!')`

Just creating this instance won't cut it for tkinter though. In order to display the widget you must use one of tkinter's *geometry managers* (GM). There are two good GMs that tkinter offers: *pack* and *grid*. Pack will place widgets relative to each other and can be a bit more challenging for beginners to learn, which is why the rest of the examples will use grid. If you just call *pack()* on each widget you create, they will display in a single column, stacked in the order you packed them. Grid, on the other hand, works like a table; you can specify which column and row to place the widget, as well as how many columns and rows the widget should span.

`my_label.pack()`

The last step in creating our glorious GUI is to start the application loop. This is an infinite loop for the application to be used.

`root.mainloop()`


---

## Wrap Up:

[Prev: Chapter 4 - Web Scraping](./chapter04.md) \| [Next: Chapter 6 - APIs](./chapter06.md)
