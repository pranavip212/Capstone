import tkinter as tk
from tkinter import ttk, messagebox
from user_profile import UserProfile
from university_expenses import UniversityExpenses
from budget import BudgetGenerator
from analyzer import BudgetAnalyzer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Main window
root = tk.Tk()
root.title("University Financial Planner")
root.geometry("700x650")

title = tk.Label(root, text="Student Financial Information", font=("Arial", 18, "bold"))
title.pack(pady=15)

#Global vars
user_data = {}
scenario_data = {}

# Main frame
user_frame = tk.Frame(root)
user_frame.pack(padx=20, pady=10, fill="both", expand=True)


#Income
tk.Label(user_frame, text="Monthly Income ($)").grid(row=0, column=0, sticky="w", pady=5)

monthly_income_entry = tk.Entry(user_frame)
monthly_income_entry.grid(row=0, column=1, pady=5)

#Savings
tk.Label(user_frame, text="Current Savings ($)").grid(row=1, column=0, sticky="w", pady=5)

current_savings_entry = tk.Entry(user_frame)
current_savings_entry.grid(row=1, column=1, pady=5)

#Scholarship Amount
tk.Label(user_frame, text="Scholarship Amount ($)").grid(row=2, column=0, sticky="w", pady=5)

scholarship_entry = tk.Entry(user_frame)
scholarship_entry.grid(row=2, column=1, pady=5)

#Family Support per Month
tk.Label(user_frame, text="Monthly Family Support ($)").grid(row=3, column=0, sticky="w", pady=5)

family_support_entry = tk.Entry(user_frame)
family_support_entry.grid(row=3, column=1, pady=5)

# Spending Style
tk.Label(user_frame, text="Spending Style (Lowest (1) - Highest(5)").grid(row=4, column=0, sticky="w", pady=5)

spending_style = ttk.Combobox(user_frame, values=[1, 2, 3, 4, 5], state="readonly")
#spending_style = ttk.Combobox(user_frame, values=["1 - Very Frugal", "2- Frugal", "3 - Balanced", "4 - Social", "5 - Very Social"], state="readonly")

spending_style.current(2)
spending_style.grid(row=4, column=1, pady=5)

#OSAP Level
tk.Label(user_frame, text="OSAP Level").grid(row=5, column=0, sticky="w", pady=5)

osap_level = ttk.Combobox(user_frame, values=["none", "average", "high"], state="readonly")
osap_level.current(1)
osap_level.grid(row=5, column=1, pady=5)

#Next button / Storing inputted data in a dict
def next_page():
    global user_data

    try:
        monthly_income = float(monthly_income_entry.get())
        current_savings = float(current_savings_entry.get())
        scholarship_amount = float(scholarship_entry.get())
        family_support = float(family_support_entry.get())

        if monthly_income < 0 or current_savings < 0 or scholarship_amount < 0 or family_support < 0:
            messagebox.showerror("Invalid Input","These financial values cannot be negative.")
            return

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all financial fields.")
        return

    user_data = {
        "monthly_income": monthly_income,
        "current_savings": current_savings,
        "scholarship_amount": scholarship_amount,
        "family_support": family_support,
        "spending_style": int(spending_style.get()),
        "osap_level": osap_level.get()
    }

    print(user_data)

    user_frame.pack_forget()
    next_button.pack_forget()

    university_frame.pack(padx=20, pady=10, fill="both", expand=True)



next_button = tk.Button(root, text="Next", command=next_page, width=15)
next_button.pack(pady=20)


university_frame = tk.Frame(root)
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

def back_to_user():

    university_frame.pack_forget()
    user_frame.pack(padx=20, pady=10, fill="both", expand=True)
    next_button.pack(pady=20)
    tk.Button(university_frame, text="Back", command=back_to_user).grid(row=10, column=0, pady=20)

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
# create objs
    user = UserProfile(
        monthly_income=user_data["monthly_income"],
        current_savings=user_data["current_savings"],
        scholarship_amount=user_data["scholarship_amount"],
        family_support=user_data["family_support"],
        spending_style=user_data["spending_style"],
        osap_level=user_data["osap_level"]
    )

    scenario = UniversityExpenses(
        university_name=scenario_data["university_name"],
        program_name=scenario_data["program_name"],
        tuition=scenario_data["tuition"],
        living_situation=scenario_data["living_situation"],
        commute_type=scenario_data["commute_type"],
        commute_distance=scenario_data["commute_distance"],
        days_on_campus=scenario_data["days_on_campus"],
        food_level=scenario_data["food_level"]
    )
    # calculations
    try:
        budget = BudgetGenerator.generate_budget(user, scenario)
        score = BudgetAnalyzer.calculate_score(budget)
        recommendations = BudgetAnalyzer.generate_recommendations(budget)
        rating = BudgetAnalyzer.financial_rating(score)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        print("Error:", e)
        return

    #TESTING
    show_results(budget, score, rating, recommendations)

tk.Button(university_frame, text="Generate Report", command=generate_report).grid(row=10, column=1, pady=20)


#results page

results_frame = tk.Frame(root)

canvas_frame = tk.Frame(results_frame)
canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_frame)
scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)

scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)


results_title = tk.Label(scrollable_frame, text="Financial Analysis Report", font=("Times New Roman", 15, "bold"))
results_title.pack(pady=10)

chart_frame = tk.Frame(scrollable_frame)
chart_frame.pack(pady=10)

score_label = tk.Label(scrollable_frame, text="", font=("Arial", 14))
score_label.pack()

rating_label = tk.Label(scrollable_frame, text="", font=("Arial", 14, "bold"))
rating_label.pack(pady=5)

summary_label = tk.Label(scrollable_frame, text="", justify="left", anchor="w", font=("Arial", 11))
summary_label.pack(padx=20, pady=10)

recommendations_label = tk.Label(scrollable_frame, text="", justify="left", anchor="w", font=("Arial", 11))
recommendations_label.pack(padx=20, pady=10)

def restart():

    scrollable_frame.pack_forget()
    user_frame.pack(padx=20, pady=10, fill="both", expand=True)
    next_button.pack(pady=20)

restart_button = tk.Button(scrollable_frame, text="Start Over", command=restart)
restart_button.pack(pady=20)

def get_rating_color(rating):
    if rating == "Excellent":
        return "green"
    elif rating == "Good":
        return "blue"
    elif rating == "Fair":
        return "orange"
    else:
        return "red"

def get_score_color(score):
    if score >= 85:
        return "green"
    elif score >= 70:
        return "blue"
    elif score >= 50:
        return "orange"
    else:
        return "red"

def section(title):
    frame = tk.Frame(scrollable_frame, pady=10)
    frame.pack(fill="x")

    tk.Label(frame, text=title, font=("Arial", 13, "bold")).pack(anchor="w")
    return frame

def show_results(budget, score, rating, recommendations):

    university_frame.pack_forget()

    score_label.config(text=f"Financial Score: {score}/100", fg=get_score_color(score))
    rating_label.config(text=f"Rating: {rating}", fg=get_rating_color(rating))
    results_frame.pack(fill="both", expand=True)

    income_section = section("Income Breakdown")
    tk.Label(income_section, text=f"Employment: ${budget['employment_income']:.2f}").pack(anchor="w")
    tk.Label(income_section, text=f"Scholarships: ${budget['scholarship_amount']:.2f}").pack(anchor="w")
    tk.Label(income_section, text=f"Family Support: ${budget['family_support'] * 12:.2f}").pack(anchor="w")
    tk.Label(income_section, text=f"OSAP Grant: ${budget['osap_grant']:.2f}").pack(anchor="w")

    expense_section = section("Expenses Breakdown")
    tk.Label(expense_section, text=f"Tuition: ${budget['tuition']:.2f}").pack(anchor="w")
    tk.Label(expense_section, text=f"Housing: ${budget['housing']:.2f}").pack(anchor="w")
    tk.Label(expense_section, text=f"Food: ${budget['food']:.2f}").pack(anchor="w")
    tk.Label(expense_section, text=f"Transportation: ${budget['transportation']:.2f}").pack(anchor="w")
    tk.Label(expense_section, text=f"Total: ${budget['yearly_expenses']:.2f}").pack(anchor="w")

    aff_section = section("Affordability")
    tk.Label(aff_section, text=f"Net (No Loan): ${budget['net_position']:.2f}").pack(anchor="w")
    tk.Label(aff_section, text=f"Net (With Loan): ${budget['net_position_with_loan']:.2f}").pack(anchor="w")
    tk.Label(aff_section, text=f"OSAP Loan: ${budget['osap_loan']:.2f}").pack(anchor="w")

    rec_section = section("Recommendations")
    for r in recommendations:
        tk.Label(rec_section, text=f"• {r}", wraplength=600, justify="left").pack(anchor="w")

 #used AI to help with some issues i was having with matplotlib
    # Clear old chart (important if restarting)
    for widget in chart_frame.winfo_children():
        widget.destroy()

    income = max(0, budget["yearly_income"])
    expenses = max(0, budget["yearly_expenses"])

    fig, ax = plt.subplots(figsize=(3.5, 3.5))  # smaller

    ax.pie([income, expenses], labels=["Income", "Expenses"], autopct="%1.1f%%", startangle=90)
    ax.set_title("Income vs Expenses")
    canvas = FigureCanvasTkAgg(fig, master=scrollable_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)






root.mainloop()