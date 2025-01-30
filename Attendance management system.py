import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Data Storage
users = {'admin': 'admin123'}
employees = {}
attendance_records = {}

# GUI Application
class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("400x400")
        
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Admin Login", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        tk.Button(self.root, text="Login", command=self.authenticate).pack(pady=10)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username] == password:
            messagebox.showinfo("Login", "Login successful!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def show_main_menu(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Attendance Management", font=("Arial", 14)).pack(pady=10)
        
        tk.Button(self.root, text="Add Employee", command=self.add_employee).pack(pady=5)
        tk.Button(self.root, text="Mark Attendance", command=self.mark_attendance).pack(pady=5)
        tk.Button(self.root, text="View Attendance", command=self.view_attendance).pack(pady=5)
        tk.Button(self.root, text="Generate Report", command=self.generate_report).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.show_login_screen).pack(pady=10)

    def add_employee(self):
        self.clear_screen()
        tk.Label(self.root, text="Add Employee", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Employee ID").pack()
        self.emp_id_entry = tk.Entry(self.root)
        self.emp_id_entry.pack()
        
        tk.Label(self.root, text="Employee Name").pack()
        self.emp_name_entry = tk.Entry(self.root)
        self.emp_name_entry.pack()
        
        tk.Button(self.root, text="Save", command=self.save_employee).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack()

    def save_employee(self):
        emp_id = self.emp_id_entry.get()
        emp_name = self.emp_name_entry.get()
        
        if emp_id and emp_name:
            employees[emp_id] = emp_name
            attendance_records[emp_id] = {}
            messagebox.showinfo("Success", "Employee added successfully!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Please enter all fields!")

    def mark_attendance(self):
        self.clear_screen()
        tk.Label(self.root, text="Mark Attendance", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Employee ID").pack()
        self.emp_id_attendance_entry = tk.Entry(self.root)
        self.emp_id_attendance_entry.pack()
        
        tk.Label(self.root, text="Status (P/A)").pack()
        self.attendance_status_entry = tk.Entry(self.root)
        self.attendance_status_entry.pack()
        
        tk.Button(self.root, text="Submit", command=self.save_attendance).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack()

    def save_attendance(self):
        emp_id = self.emp_id_attendance_entry.get()
        status = self.attendance_status_entry.get().upper()
        date = datetime.today().strftime('%Y-%m-%d')

        if emp_id in employees:
            attendance_records[emp_id][date] = status
            messagebox.showinfo("Success", "Attendance marked successfully!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Employee not found!")

    def view_attendance(self):
        self.clear_screen()
        tk.Label(self.root, text="View Attendance", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Employee ID").pack()
        self.emp_id_view_entry = tk.Entry(self.root)
        self.emp_id_view_entry.pack()
        
        tk.Button(self.root, text="Show", command=self.display_attendance).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack()

    def display_attendance(self):
        emp_id = self.emp_id_view_entry.get()
        
        if emp_id in employees:
            records = attendance_records.get(emp_id, {})
            attendance_list = "\n".join([f"{date}: {status}" for date, status in records.items()])
            messagebox.showinfo("Attendance Records", attendance_list if attendance_list else "No records found.")
        else:
            messagebox.showerror("Error", "Employee not found!")

    def generate_report(self):
        self.clear_screen()
        tk.Label(self.root, text="Generate Report", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Employee ID").pack()
        self.emp_id_report_entry = tk.Entry(self.root)
        self.emp_id_report_entry.pack()
        
        tk.Button(self.root, text="Generate", command=self.display_report).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack()

    def display_report(self):
        emp_id = self.emp_id_report_entry.get()
        
        if emp_id in employees:
            records = attendance_records.get(emp_id, {})
            report = f"Attendance Report for {employees[emp_id]}:\n" + "\n".join([f"{date}: {status}" for date, status in records.items()])
            messagebox.showinfo("Attendance Report", report if records else "No records found.")
        else:
            messagebox.showerror("Error", "Employee not found!")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
