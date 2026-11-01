import tkinter as tk
from functools import partial


def action_one(text_var):
    text_var.set("Option1")


def action_two(text_var):
    text_var.set("Option2")


def addRightClickMenu(master, text_var):
    context_menu = tk.Menu(master, tearoff=0)
    context_menu.add_command(label="Option One", command=partial(action_one, text_var))
    context_menu.add_command(label="Option Two", command=partial(action_two, text_var))

    def do_popup(event):
        try:
            # Display the context menu at the mouse pointer's position
            context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            # Release the mouse grab properly
            context_menu.grab_release()

    # 3. Bind the right-click event cross-platform
    # <Button-3> handles Windows and Linux right-clicks
    master.bind("<Button-3>", do_popup)
    # <Button-2> handles macOS right-clicks
    master.bind("<Button-2>", do_popup)


def addTextLabel(master):
    # 1. Create a Tkinter StringVar
    text_var = tk.StringVar()
    text_var.set("Right-click inside this window to open the menu.")
    # Add a label widget to interact with
    label = tk.Label(master, height=4, textvariable=text_var)
    label.pack(pady=50, padx=20, fill="both", expand=True)

    return text_var


def main():
    # Initialize main window
    root = tk.Tk()
    root.title("Context Menu Example")
    root.geometry("400x300")
    root.bind

    text_var = addTextLabel(root)
    addRightClickMenu(root, text_var)

    root.mainloop()


if __name__ == "__main__":
    main()
