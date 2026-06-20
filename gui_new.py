import tkinter as tk
from tkinter import ttk, messagebox
from user_profile import UserProfile
from university_expenses import UniversityExpenses
from budget import BudgetGenerator
from analyzer import BudgetAnalyzer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# main window
root = tk.Tk()
root.title("University Financial Dashboard")
root.geometry("1000x650")
root.configure(bg="#f4f6fb")

#globals/data storage
user_data = {}
scenario_data = {}
latest_budget = {}
latest_score = 0
latest_rating = ""

#layout
sidebar = tk.Frame(root, bg="#1f2937", width=200)
sidebar.pack(side="left", fill="y")

main_area = tk.Frame(root, bg="#f4f6fb")
main_area.pack(side="right", expand=True, fill="both")

#pages instead of different frames
