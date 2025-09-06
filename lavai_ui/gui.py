import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
import lavai
import os
import json


class LavaiGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Lavai GUI - Manage AI Provider Credentials")
        self.root.geometry("500x400")
        self.root.minsize(400, 300)
        
        self.client_list = []
        self.client_listbox = None
        
        self.setup_ui()
        self.update_client_listbox()

    def update_client_listbox(self):
        """Update the client listbox with current clients."""
        if self.client_listbox:
            self.client_listbox.delete(0, tk.END)
            for client in lavai.list_clients():
                self.client_listbox.insert(tk.END, client)

    def save_client(self, client_name, api_key):
        """Save client credentials using lavai library."""
        try:
            lavai.store(client_name, api_key)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error saving client: {str(e)}")
            return False

    def remove_client(self, client_name):
        """Remove client credentials using lavai library."""
        try:
            lavai.remove(client_name)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error removing client: {str(e)}")
            return False
        
    def setup_ui(self):
        """Set up the main user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Lavai GUI - Manage AI Provider Credentials", 
                               font=("Arial", 12, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 10), sticky=tk.W)
        
        # Client listbox with scrollbar
        listbox_frame = ttk.Frame(main_frame)
        listbox_frame.grid(row=1, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        listbox_frame.columnconfigure(0, weight=1)
        listbox_frame.rowconfigure(0, weight=1)
        
        self.client_listbox = tk.Listbox(listbox_frame, height=15)
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.client_listbox.yview)
        self.client_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.client_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=(0, 10))
        
        # Buttons
        add_button = ttk.Button(button_frame, text="Add", command=self.handle_add)
        remove_button = ttk.Button(button_frame, text="Remove", command=self.handle_remove)
        refresh_button = ttk.Button(button_frame, text="Refresh", command=self.update_client_listbox)
        exit_button = ttk.Button(button_frame, text="Exit", command=self.root.destroy)
        
        add_button.pack(side=tk.LEFT, padx=(0, 5))
        remove_button.pack(side=tk.LEFT, padx=(0, 5))
        refresh_button.pack(side=tk.LEFT, padx=(0, 5))
        exit_button.pack(side=tk.LEFT)

    def handle_add(self):
        """Handle the add client functionality."""
        # Create add dialog
        add_dialog = tk.Toplevel(self.root)
        add_dialog.title("Add New Client")
        add_dialog.geometry("400x150")
        add_dialog.transient(self.root)
        add_dialog.grab_set()
        
        # Center the dialog
        add_dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        # Variables
        client_name_var = tk.StringVar()
        api_key_var = tk.StringVar()
        
        # Layout
        main_frame = ttk.Frame(add_dialog, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Client name
        ttk.Label(main_frame, text="Client Name:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        client_name_entry = ttk.Entry(main_frame, textvariable=client_name_var, width=30)
        client_name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=(0, 5))
        
        # API key
        ttk.Label(main_frame, text="API Key:").grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
        api_key_entry = ttk.Entry(main_frame, textvariable=api_key_var, width=30, show="*")
        api_key_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=(0, 5))
        
        def save_client():
            client_name = client_name_var.get().strip()
            api_key = api_key_var.get().strip()
            
            if not client_name or not api_key:
                messagebox.showwarning("Warning", "Please fill in both Client Name and API Key.")
                return
            
            if self.save_client(client_name, api_key):
                messagebox.showinfo("Success", "Client added successfully!")
                add_dialog.destroy()
                self.update_client_listbox()
            else:
                messagebox.showerror("Error", "Failed to add client.")
        
        save_button = ttk.Button(button_frame, text="Save", command=save_client)
        cancel_button = ttk.Button(button_frame, text="Cancel", command=add_dialog.destroy)
        
        save_button.pack(side=tk.LEFT, padx=(0, 5))
        cancel_button.pack(side=tk.LEFT)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        add_dialog.columnconfigure(0, weight=1)

    def handle_remove(self):
        """Handle the remove client functionality."""
        selection = self.client_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a client to remove.")
            return
        
        client_name = self.client_listbox.get(selection[0])
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to remove '{client_name}'?")
        
        if confirm:
            if self.remove_client(client_name):
                messagebox.showinfo("Success", "Client removed successfully!")
                self.update_client_listbox()
            else:
                messagebox.showerror("Error", "Failed to remove client.")


    def run(self):
        """Run the main GUI application."""
        # Center the main window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
        
        self.root.mainloop()


def main():
    """Main entry point for the GUI application."""
    app = LavaiGUI()
    app.run()


if __name__ == "__main__":
    main()
