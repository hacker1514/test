from tkinter import *
from datetime import datetime, timedelta
import webbrowser
from tkinter import messagebox

w = Tk()
w.title("ADSA Test Portal")
w.attributes('-fullscreen', True)
w.protocol("WM_DELETE_WINDOW", lambda: None)
def f(event):
    if event.keysym.lower() == 'k':
        w.destroy()
    else:
        return "break"
w.bind_all("<KeyPress>", f)
w.bind_all("<KeyRelease>", f)
w.bind_all("<Button>", lambda e: "break")
w.bind_all("<Motion>", lambda e: "break")

th = 16
tm = 30
ts = 0
c = datetime.now()
ch = c.hour
cm = c.minute
cs = c.second
if (ch > th) or (ch == th and cm > tm) or (ch == th and cm == tm and cs > ts):
    messagebox.showinfo("Time Delay", "Test Locked!\nAlready Test Started.\nIf you have further doubt, contact Niranjan!")
    w.destroy()

w.config(bg="#1C1C1C")

title = Label(w, text="ADSA TEST", font=("Arial", 48, "bold"), fg="#ff4d4d", bg="#1c1c1c")
title.pack(pady=16)

timer_label = Label(w, text="", font=("Arial", 20, "bold"), fg="#00ff00", bg="#1c1c1c")
timer_label.pack(pady=6)

instruction_text = (
    "Welcome to the ADSA Test Portal !\n\n"
    "Instructions :\n"
    "--> Read all instructions carefully.\n"
    "--> Do not attempt anything outside the Test.\n"
    "--> System will auto-start at exact "+str(th)+"H: "+str(tm)+"M: "+str(ts)+"S .\n"
    "--> Test duration: 30 minutes.\n"
    "--> Submit button appears after 15 minutes.\n"
    "--> Each question carry 1 mark.\n"
    "--> Any Problem Please Contact Niranjan.\n"
    "--> Certificate Provides those who score more than 15.\n"
    "--> Total Test Contain 30 questions.\n\n"
    "-----------------All The Best !----------------"
)
def on_focus_out(event):
    correct_count = sum(1 for q, data in answer_vars.items() if data["var"].get() == data["correct"])
    for widget in w.winfo_children():
        widget.destroy()
    result_label = Label(w, text=f"Your Score: {correct_count} / {len(questions)}", font=("Arial", 40, "bold"), fg="white", bg="#1c1c1c")
    result_label.pack(pady=40)
    exit_btn = Button(w, text="Exit", font=("Arial", 18, "bold"), bg="red", fg="white", command=w.destroy)
    exit_btn.pack(pady=20)
w.bind("<FocusOut>", on_focus_out)

inst_label = Label(w, text=instruction_text, font=("Arial", 16), fg="white", bg="#1c1c1c", justify=LEFT)
inst_label.pack(padx=40, pady=8, anchor="w")

questions = [
("1. The time complexity of finding the height of an AVL tree is:", 
 ["a) O(1)", "b) O(log n)", "c) O(n)", "d) O(n log n)"], 
 "b) O(log n)"),

("2. The maximum height of an AVL tree with n nodes is approximately:", 
 ["a) 1.44 log₂(n+2) - 0.328", "b) log₂n", "c) n/2", "d) √n"], 
 "a) 1.44 log₂(n+2) - 0.328"),

("3. In AVL tree rotation, which of the following is not a valid imbalance type?", 
 ["a) LL", "b) RR", "c) LR", "d) RL-LR"], 
 "d) RL-LR"),

("4. B-Tree of order m can have maximum children:", 
 ["a) m", "b) m+1", "c) 2m", "d) m-1"], 
 "a) m"),

("5. In B-Tree, all leaves appear:", 
 ["a) At same level", "b) At different levels", "c) Only at root", "d) Only at leftmost path"], 
 "a) At same level"),

("6. The worst-case time complexity of searching in a B-tree of order m and height h is:", 
 ["a) O(h)", "b) O(mh)", "c) O(log n)", "d) O(h log m)"], 
 "b) O(mh)"),

("7. The adjacency matrix representation of a graph with n vertices requires:", 
 ["a) O(n)", "b) O(n²)", "c) O(E)", "d) O(V+E)"], 
 "b) O(n²)"),

("8. In DFS traversal of a graph, which data structure is used?", 
 ["a) Queue", "b) Stack", "c) Priority Queue", "d) Heap"], 
 "b) Stack"),

("9. The recurrence relation for Merge Sort is:", 
 ["a) T(n)=T(n-1)+O(1)", "b) T(n)=2T(n/2)+O(n)", "c) T(n)=T(n/2)+O(1)", "d) T(n)=T(n/4)+O(n)"], 
 "b) T(n)=2T(n/2)+O(n)"),

("10. The time complexity of Strassen’s Matrix Multiplication is:", 
 ["a) O(n³)", "b) O(n².81)", "c) O(n²)", "d) O(n log n)"], 
 "b) O(n².81)"),

("11. Quick Sort has worst-case complexity when pivot is:", 
 ["a) Median element", "b) Random element", "c) Smallest or largest element", "d) None"], 
 "c) Smallest or largest element"),

("12. The greedy method guarantees an optimal solution only if:", 
 ["a) Optimal substructure and greedy choice property exist", "b) Overlapping subproblems exist", "c) Recursion is used", "d) None of the above"], 
 "a) Optimal substructure and greedy choice property exist"),

("13. The complexity of Kruskal’s algorithm using union-find is:", 
 ["a) O(E log V)", "b) O(V²)", "c) O(E+V)", "d) O(V log V)"], 
 "a) O(E log V)"),

("14. Dijkstra’s algorithm fails for graphs containing:", 
 ["a) Negative edges", "b) Positive weights", "c) Undirected edges", "d) Zero-weight cycles"], 
 "a) Negative edges"),

("15. The Bellman-Ford algorithm runs in:", 
 ["a) O(V²)", "b) O(VE)", "c) O(E log V)", "d) O(V log V)"], 
 "b) O(VE)"),

("16. The all-pairs shortest path problem is efficiently solved by:", 
 ["a) Dijkstra’s algorithm", "b) Bellman-Ford algorithm", "c) Floyd-Warshall algorithm", "d) Kruskal’s algorithm"], 
 "c) Floyd-Warshall algorithm"),

("17. The recurrence relation for dynamic programming 0/1 knapsack problem is:", 
 ["a) V[i,j]=max(V[i-1,j], V[i-1,j-wi]+vi)", "b) V[i,j]=V[i-1,j]+vi", "c) V[i,j]=V[i-1,j/2]+wi", "d) None"], 
 "a) V[i,j]=max(V[i-1,j], V[i-1,j-wi]+vi)"),

("18. Travelling Salesperson Problem (TSP) using dynamic programming has complexity:", 
 ["a) O(n²)", "b) O(2ⁿ·n²)", "c) O(n!)", "d) O(n³)"], 
 "b) O(2ⁿ·n²)"),

("19. In 8-Queens problem, total possible solutions are:", 
 ["a) 8!", "b) 92", "c) 64", "d) 256"], 
 "b) 92"),

("20. Backtracking ensures:", 
 ["a) Complete search of feasible solutions", "b) Random selection of nodes", "c) Probabilistic result", "d) Heuristic pruning"], 
 "a) Complete search of feasible solutions"),

("21. Sum of Subsets problem is an example of:", 
 ["a) Greedy algorithm", "b) Backtracking", "c) Divide and conquer", "d) Dynamic programming"], 
 "b) Backtracking"),

("22. Branch and Bound is more efficient than backtracking because:", 
 ["a) Uses bounding function to prune", "b) Explores all paths", "c) Ignores cost functions", "d) Works without recursion"], 
 "a) Uses bounding function to prune"),

("23. In branch and bound for 0/1 knapsack, upper bound is computed by:", 
 ["a) Fractional knapsack", "b) Exact knapsack", "c) Dynamic programming", "d) Random estimation"], 
 "a) Fractional knapsack"),

("24. The decision version of Travelling Salesperson Problem is:", 
 ["a) NP", "b) NP-Complete", "c) NP-Hard", "d) P"], 
 "b) NP-Complete"),

("25. Cook’s theorem shows that:", 
 ["a) SAT is NP-Complete", "b) TSP is NP-Hard", "c) Graph coloring is NP", "d) Clique problem is polynomial"], 
 "a) SAT is NP-Complete"),

("26. A problem X is NP-Hard means:", 
 ["a) Every NP problem reduces to X", "b) X reduces to every NP problem", "c) X is easier than NP problems", "d) X is undecidable"], 
 "a) Every NP problem reduces to X"),

("27. Clique Decision Problem (CDP) asks:", 
 ["a) Whether graph is complete", "b) Whether there exists a clique of size k", "c) Minimum spanning tree cost", "d) Shortest path length"], 
 "b) Whether there exists a clique of size k"),

("28. Chromatic Number Decision Problem (CNDP) determines:", 
 ["a) Minimum colors to color vertices", "b) Maximum degree of graph", "c) Bipartiteness", "d) Edge coloring"], 
 "a) Minimum colors to color vertices"),

("29. Job Shop Scheduling problem is classified as:", 
 ["a) NP", "b) NP-Hard", "c) P", "d) PSPACE"], 
 "b) NP-Hard"),

("30. Which of the following statements is true for NP-Complete problems?", 
 ["a) Every NP-Complete problem can be polynomially reduced to every other NP-Complete problem", "b) NP-Complete ⊂ P", "c) NP-Complete = NP-Hard", "d) NP-Complete ⊂ NP-Hard and ⊂ P"], 
 "a) Every NP-Complete problem can be polynomially reduced to every other NP-Complete problem")
]
answer_vars = {q: {"var": StringVar(), "correct": correct} for q, opts, correct in questions}
quiz_started = False
quiz_start_time = None
current_index = 0
quiz_frame = None
question_label = None
option_widgets = []
submit_btn = None
next_btn = None
prev_btn = None
page_label = None
score_shown = False

def show_question(index):
    global option_widgets
    q, opts, correct = questions[index]
    question_label.config(text=q)
    for rb in option_widgets:
        rb.destroy()
    option_widgets.clear()
    sv = answer_vars[q]["var"]
    for opt in opts:
        rb = Radiobutton(q_area, text=opt, variable=sv, value=opt, font=("Arial", 14), bg="#1c1c1c", fg="white", selectcolor="#1c1c1c", activebackground="#1c1c1c", anchor="w", justify=LEFT)
        rb.pack(fill=X, anchor="w", padx=20, pady=2)
        option_widgets.append(rb)
    page_label.config(text=f"Question {index+1} / {len(questions)}")

def next_question():
    global current_index
    if current_index < len(questions) - 1:
        current_index += 1
        show_question(current_index)

def prev_question():
    global current_index
    if current_index > 0:
        current_index -= 1
        show_question(current_index)

def create_quiz_ui():
    global quiz_frame, q_area, question_label, option_widgets, submit_btn, next_btn, prev_btn, page_label
    quiz_frame = Frame(w, bg="#1c1c1c")
    quiz_frame.pack(fill=BOTH, expand=True, padx=20, pady=12)
    q_top = Frame(quiz_frame, bg="#1c1c1c")
    q_top.pack(fill=X, pady=6)
    page_label = Label(q_top, text="", font=("Arial", 14), fg="yellow", bg="#1c1c1c")
    page_label.pack(side=LEFT)
    q_area = Frame(quiz_frame, bg="#1c1c1c")
    q_area.pack(fill=BOTH, expand=True, pady=8)
    question_label = Label(q_area, text="", font=("Arial", 18, "bold"), fg="white", bg="#1c1c1c", wraplength=1200, justify=LEFT)
    question_label.pack(anchor="w", pady=6)
    option_widgets.clear()
    btn_frame = Frame(quiz_frame, bg="#1c1c1c")
    btn_frame.pack(fill=X, pady=12)
    prev_btn = Button(btn_frame, text="Previous", font=("Arial", 14, "bold"), command=prev_question, bg="#3333ff", fg="white")
    prev_btn.pack(side=LEFT, padx=12, pady=6)
    next_btn = Button(btn_frame, text="Next", font=("Arial", 14, "bold"), command=next_question, bg="#3333ff", fg="white")
    next_btn.pack(side=LEFT, padx=12, pady=6)
    submit_btn = Button(btn_frame, text="Submit", font=("Arial", 14, "bold"), bg="#00ff00", fg="black", command=submit_quiz)
    submit_btn.pack(side=RIGHT, padx=12, pady=6)
    submit_btn.pack_forget()
    show_question(current_index)

def submit_quiz():
    global score_shown
    if score_shown:
        return
    correct_count = sum(1 for q, data in answer_vars.items() if data["var"].get() == data["correct"])
    for widget in w.winfo_children():
        widget.destroy()
    result_label = Label(w, text=f"Your Score: {correct_count} / {len(questions)}", font=("Arial", 40, "bold"), fg="white", bg="#1c1c1c")
    result_label.pack(pady=40)
    if correct_count >= 15:
        webbrowser.open("https://hacker1514.github.io/test/c.html")
    exit_btn = Button(w, text="Exit", font=("Arial", 18, "bold"), bg="red", fg="white", command=w.destroy)
    exit_btn.pack(pady=20)
    score_shown = True

def update_loop():
    global quiz_started, quiz_start_time
    now = datetime.now()
    target = now.replace(hour=th, minute=tm, second=ts, microsecond=0)
    if now < target:
        diff = target - now
        h, r = divmod(int(diff.total_seconds()), 3600)
        m, s = divmod(r, 60)
        timer_label.config(text=f"Test starts in {h:02d}H : {m:02d}M : {s:02d}S")
    elif now >= target and not quiz_started:
        quiz_started = True
        quiz_start_time = datetime.now()
        inst_label.pack_forget()
        create_quiz_ui()
    elif now > target + timedelta(seconds=1) and not quiz_started:
        messagebox.showinfo("Time Delay", "Test Locked!\nAlready Test Started.\nIf you have further doubt, contact Niranjan!")
        w.destroy()
        return
    if quiz_started:
        elapsed = datetime.now() - quiz_start_time
        remaining_seconds = max(0, 30 * 60 - int(elapsed.total_seconds()))
        remaining_min, remaining_sec = divmod(remaining_seconds, 60)
        timer_label.config(text=f"Remaining Time: {remaining_min:02d}M : {remaining_sec:02d}S")
        if elapsed.total_seconds() >= 15 * 60:
            submit_btn.pack(side=RIGHT, padx=12, pady=6)
        else:
            submit_btn.pack_forget()
        if remaining_seconds <= 0:
            submit_quiz()
    w.after(1000, update_loop)

update_loop()
w.mainloop()
