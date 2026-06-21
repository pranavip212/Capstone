import tkinter as tk
from tkinter import ttk, messagebox
from user_profile import UserProfile
from university_expenses import UniversityExpenses
from budget import BudgetGenerator
from analyzer import BudgetAnalyzer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#main window
root = tk.Tk()
root.title("University Financial Planner")
root.geometry("950x650")
root.configure(background="#f4f6fb")

# globals
user_data = {}
scenario_data = {}

#layout/ sidebar and main window spilt
sidebar = tk.Frame(root, bg="#1f2937", width=180)
sidebar.pack(side="left", fill="y")

main_area = tk.Frame(root, bg="#f4f6fb")
main_area.pack(side="right", fill="both", expand=True)

def show_frame(frame):
    user_frame.pack_forget()
    university_frame.pack_forget()
    results_frame.pack_forget()

    frame.pack(fill="both", expand=True)

# sidebar buttons
#lambda function citations (from lesson document)
tk.Label(sidebar, text="MENU", bg="#1f2937", fg="white", font=("Arial", 14, "bold")).pack(pady=20)
tk.Button(sidebar, text="Input", command=lambda: show_frame(user_frame), bg="#1f2937", fg="white", relief="flat").pack(fill="x")
tk.Button(sidebar, text="University", command=lambda: show_frame(university_frame), bg="#1f2937", fg="white", relief="flat").pack(fill="x")
tk.Button(sidebar, text="Results", command=lambda: show_frame(results_frame), bg="#1f2937", fg="white", relief="flat").pack(fill="x")

#user frame
user_frame = tk.Frame(main_area, bg="#f4f6fb")
user_frame.grid_columnconfigure(0, weight=1)
user_frame.grid_columnconfigure(1, weight=2)

tk.Label(user_frame, text="Student Financial Information", font=("Arial", 18, "bold"), bg="#f4f6fb").grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(user_frame, text="Monthly Income ($)", bg="#f4f6fb").grid(row=1, column=0, sticky="w", padx=10, pady=5)
monthly_income_entry = tk.Entry(user_frame)
monthly_income_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)


#Savings
tk.Label(user_frame, text="Current Savings ($)", bg="#f4f6fb").grid(row=2, column=0, sticky="w", padx=10, pady=5)
current_savings_entry = tk.Entry(user_frame)
current_savings_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

#Scholarship Amount
tk.Label(user_frame, text="Scholarship Amount ($)", bg="#f4f6fb").grid(row=3, column=0, sticky="w", padx=10, pady=5)
scholarship_entry = tk.Entry(user_frame)
scholarship_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

#Family Support per Month
tk.Label(user_frame, text="Monthly Family Support ($)", bg="#f4f6fb").grid(row=4, column=0, sticky="w", padx=10, pady=5)
family_support_entry = tk.Entry(user_frame)
family_support_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

## Spending Style
tk.Label(user_frame, text="Spending Style (1–5)", bg="#f4f6fb").grid(row=5, column=0, sticky="w", padx=10, pady=5)

spending_style = ttk.Combobox(user_frame, values=[1, 2, 3, 4, 5], state="readonly")
spending_style.current(2)
spending_style.grid(row=5, column=1, sticky="ew", padx=10, pady=5)


# OSAP
tk.Label(user_frame, text="OSAP Level", bg="#f4f6fb")\
    .grid(row=6, column=0, sticky="w", padx=10, pady=5)

osap_level = ttk.Combobox(user_frame, values=["none", "average", "high"], state="readonly")
osap_level.current(1)
osap_level.grid(row=6, column=1, sticky="ew", padx=10, pady=5)

# nect button
def next_page():
    global user_data

    try:
        monthly_income = float(monthly_income_entry.get())
        current_savings = float(current_savings_entry.get())
        scholarship_amount = float(scholarship_entry.get())
        family_support = float(family_support_entry.get())

        if monthly_income < 0 or current_savings < 0 or scholarship_amount < 0 or family_support < 0:
            messagebox.showerror("Error", "No negative values allowed.")
            return

        if spending_style.get() not in ["1", "2", "3", "4", "5"]:
            messagebox.showerror("Error", "Invalid spending style.")
            return

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers. Ensure there are no spaces or characters")
        return

    user_data = {
        "monthly_income": monthly_income,
        "current_savings": current_savings,
        "scholarship_amount": scholarship_amount,
        "family_support": family_support,
        "spending_style": int(spending_style.get()),
        "osap_level": osap_level.get()
    }

    next_button.pack_forget()
    show_frame(university_frame)

next_button = tk.Button(root, text="Next", command=next_page)
next_button.pack(pady=10)

# University info page

university_frame = tk.Frame(main_area, bg="#f4f6fb")

title2 = tk.Label(university_frame, text="University Information", font=("Arial", 18, "bold"))
title2.grid(row=0, column=0, columnspan=2, pady=15)

tk.Label(university_frame, text="University Name").grid(row=1, column=0, sticky="w", pady=5)
university_entry = tk.Entry(university_frame)
university_entry.grid(row=1, column=1, pady=5)

tk.Label(university_frame, text="Program Name").grid(row=2, column=0, sticky="w", pady=5)

program_entry = tk.Entry(university_frame)
program_entry.grid(row=2, column=1, pady=5)

tk.Label(university_frame, text="Annual Tuition ($)").grid(row=3, column=0, sticky="w", pady=5)
tuition_entry = tk.Entry(university_frame)
tuition_entry.grid(row=3, column=1, pady=5)

tk.Label(university_frame, text="Living Situation").grid(row=4, column=0, sticky="w", pady=5)
living_combo = ttk.Combobox(university_frame, values=["home", "residence", "apartment"], state="readonly")
living_combo.current(0)
living_combo.grid(row=4, column=1, pady=5)

tk.Label(university_frame, text="Food Spending Level").grid(row=5, column=0, sticky="w", pady=5)
food_combo = ttk.Combobox(university_frame, values=["low", "medium", "high"], state="readonly")
food_combo.current(1)
food_combo.grid(row=5, column=1, pady=5)

tk.Label(university_frame, text="Transportation").grid(row=6, column=0, sticky="w", pady=5)

transport_combo = ttk.Combobox(university_frame, values=["drive", "transit", "walk"], state="readonly")
transport_combo.current(0)
transport_combo.grid(row=6, column=1, pady=5)

tk.Label(university_frame, text="Commute Distance (km)").grid(row=7, column=0, sticky="w", pady=5)
distance_entry = tk.Entry(university_frame)
distance_entry.grid(row=7, column=1, pady=5)

tk.Label(university_frame, text="Days On Campus Per Week").grid(row=8, column=0, sticky="w", pady=5)
days_entry = tk.Entry(university_frame)
days_entry.grid(row=8, column=1, pady=5)


#report

def generate_report():
    global scenario_data

    if not university_entry.get().strip():
        messagebox.showerror("Missing Information", "Please enter a university name.")
        return

    if not program_entry.get().strip():
        messagebox.showerror("Missing Information", "Please enter a program name.")
        return

    try:
        tuition = float(tuition_entry.get())
        commute_distance = float(distance_entry.get())
        days_on_campus = int(days_entry.get())

        if tuition < 0:
            messagebox.showerror("Invalid Input", "Tuition cannot be negative.")
            return

        if commute_distance < 0:
            messagebox.showerror("Invalid Input", "Commute distance cannot be negative.")
            return

        if days_on_campus < 0 or days_on_campus > 7:
            messagebox.showerror("Invalid Input", "Days on campus must be between 0 and 7.")
            return

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for tuition, commute distance, and/or days on campus.")
        return

    scenario_data = {
    "university_name": university_entry.get(),
    "program_name": program_entry.get(),
    "tuition": tuition,
    "living_situation": living_combo.get(),
    "food_level": food_combo.get(),
    "commute_type": transport_combo.get(),
    "commute_distance": commute_distance,
    "days_on_campus": days_on_campus
    }

    user = UserProfile(**user_data)

    try:
        scenario = UniversityExpenses(**scenario_data)
    except Exception as e:
        messagebox.showerror("Error", f"Scenario build failed: {e}")
        return


    budget = BudgetGenerator.generate_budget(user, scenario)
    score = BudgetAnalyzer.calculate_score(budget)
    rating = BudgetAnalyzer.financial_rating(score)
    recommendations = BudgetAnalyzer.generate_recommendations(budget)

    show_results(budget, score, rating, recommendations)


tk.Button(university_frame, text="Generate", command=generate_report).grid(row=9, column=1)

#Results page
results_frame = tk.Frame(main_area, bg="#f4f6fb")
results_title = tk.Label(results_frame, text="Results", font=("Arial", 16, "bold"))
results_title.pack(pady=10)

score_label = tk.Label(results_frame, font=("Arial", 14))
score_label.pack()

rating_label = tk.Label(results_frame, font=("Arial", 14))
rating_label.pack()

chart_frame = tk.Frame(results_frame)
chart_frame.pack()

summary_label = tk.Label(results_frame, justify="left")
summary_label.pack(pady=10)

recommendations_label = tk.Label(results_frame, justify="left")
recommendations_label.pack(pady=10)

def show_results(budget, score, rating, recommendations):

    university_frame.pack_forget()
    results_frame.pack(fill="both", expand=True)

    score_label.config(text=f"Score: {score}/100", fg=get_color(score))
    rating_label.config(text=f"Rating: {rating}")

    summary_label.config(text=
        f"Income: {budget['yearly_income']}\n"
        f"Expenses: {budget['yearly_expenses']}\n"
        f"Net: {budget['net_position']}"
    )

    rec_text = "Recommendations:\n"
    for r in recommendations:
        rec_text += f"- {r}\n"
    recommendations_label.config(text=rec_text)

    # chart reset
    for w in chart_frame.winfo_children():
        w.destroy()

    fig, ax = plt.subplots(figsize=(3,3))
    ax.pie([budget["yearly_income"], budget["yearly_expenses"]], labels=["Income", "Expenses"], autopct="%1.1f%%")

    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


#helper/extra feature
def get_color(score):
    if score >= 85:
        return "green"
    elif score >= 70:
        return "blue"
    elif score >= 50:
        return "orange"
    return "red"

# restart button
def reset_app():
    global user_data, scenario_data

    # reset stored data
    user_data = {}
    scenario_data = {}

    # clear all entry fields (user page)
    monthly_income_entry.delete(0, tk.END)
    current_savings_entry.delete(0, tk.END)
    scholarship_entry.delete(0, tk.END)
    family_support_entry.delete(0, tk.END)

    # reset dropdowns
    spending_style.current(2)
    osap_level.current(1)

    # university page fields
    university_entry.delete(0, tk.END)
    program_entry.delete(0, tk.END)
    tuition_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)
    days_entry.delete(0, tk.END)

    living_combo.current(0)
    food_combo.current(1)
    transport_combo.current(0)

    # clear results
    score_label.config(text="")
    rating_label.config(text="")
    summary_label.config(text="")
    recommendations_label.config(text="")

    for w in chart_frame.winfo_children():
        w.destroy()

    # reset view back to first page
    show_frame(user_frame)

tk.Button(sidebar, text="Restart", command=reset_app, bg="#1f2937", fg="white", relief="flat").pack(fill="x")
show_frame(user_frame)
root.mainloop()
