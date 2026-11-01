import tkinter as tk


def do_popup(event):
    try:
        # Display the context menu at the mouse pointer's position
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        # Release the mouse grab properly
        context_menu.grab_release()


def action_one():
    text_var.set("Option1")


def action_two():
    text_var.set("Option2")


# Initialize main window
root = tk.Tk()
root.title("Context Menu Example")
root.geometry("400x300")

# 1. Create a Tkinter StringVar
text_var = tk.StringVar()
text_var.set("Right-click inside this window to open the menu.")
# Add a label widget to interact with
label = tk.Label(root, height=4, textvariable=text_var)
label.pack(pady=50, padx=20, fill="both", expand=True)

# 1. Create the Menu instance
context_menu = tk.Menu(root, tearoff=0)

# 2. Add commands and separators
context_menu.add_command(label="Option One", command=action_one)
context_menu.add_command(label="Option Two", command=action_two)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=root.quit)

# 3. Bind the right-click event cross-platform
# <Button-3> handles Windows and Linux right-clicks
root.bind("<Button-3>", do_popup)
# <Button-2> handles macOS right-clicks
root.bind("<Button-2>", do_popup)

root.mainloop()
