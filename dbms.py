from tkinter import *
from datetime import datetime, timedelta
import webbrowser
from tkinter import messagebox

w = Tk()
w.title("DBMS Test Portal")
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

th = 17
tm = 0
ts = 0
c = datetime.now()
ch = c.hour
cm = c.minute
cs = c.second
if (ch > th) or (ch == th and cm > tm) or (ch == th and cm == tm and cs > ts):
    messagebox.showinfo("Time Delay", "Test Locked!\nAlready Test Started.\nIf you have further doubt, contact Niranjan!")
    w.destroy()

w.config(bg="#1C1C1C")

title = Label(w, text="DBMS TEST", font=("Arial", 48, "bold"), fg="#ff4d4d", bg="#1c1c1c")
title.pack(pady=16)

timer_label = Label(w, text="", font=("Arial", 20, "bold"), fg="#00ff00", bg="#1c1c1c")
timer_label.pack(pady=6)

instruction_text = (
    "Welcome to the DBMS Test Portal !\n\n"
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

questions =[
("1. Which of the following is not a limitation of traditional file systems?", 
 ["a) Data redundancy", "b) Data inconsistency", "c) Concurrent access control", "d) High normalization"], 
 "d) High normalization"),

("2. In DBMS architecture, which layer is responsible for query optimization?", 
 ["a) External layer", "b) Conceptual layer", "c) Internal layer", "d) Physical layer"], 
 "b) Conceptual layer"),

("3. A schema that defines the structure of the entire database is known as ________", 
 ["a) Internal schema", "b) Logical schema", "c) External schema", "d) Physical schema"], 
 "b) Logical schema"),

("4. Which of the following relationships cannot be represented directly in ER modeling?", 
 ["a) One-to-one", "b) One-to-many", "c) Many-to-many-to-many", "d) Recursive"], 
 "c) Many-to-many-to-many"),

("5. The total number of possible relationships among n entities is:", 
 ["a) n", "b) n²", "c) 2ⁿ - 1", "d) n!"], 
 "c) 2ⁿ - 1"),

("6. Which type of attribute can be divided into smaller sub-parts?", 
 ["a) Composite", "b) Multivalued", "c) Derived", "d) Key"], 
 "a) Composite"),

("7. A weak entity is identified by:", 
 ["a) Primary key", "b) Partial key with owner key", "c) Foreign key", "d) Derived attribute"], 
 "b) Partial key with owner key"),

("8. Structural constraints in ER modeling include:", 
 ["a) Participation and cardinality", "b) Entity and attribute", "c) Primary and foreign key", "d) Generalization and specialization"], 
 "a) Participation and cardinality"),

("9. Mapping a multivalued attribute in ER model results in:", 
 ["a) One relation", "b) Two relations", "c) Three relations", "d) Single attribute expansion"], 
 "b) Two relations"),

("10. The relational model is based on:", 
 ["a) Graph theory", "b) Predicate logic and set theory", "c) Calculus", "d) Network model"], 
 "b) Predicate logic and set theory"),

("11. Which SQL clause removes duplicates in query output?", 
 ["a) UNIQUE", "b) DISTINCT", "c) ONLY", "d) LIMIT"], 
 "b) DISTINCT"),

("12. Which aggregate function in SQL ignores NULL values?", 
 ["a) SUM()", "b) AVG()", "c) COUNT()", "d) All of the above"], 
 "d) All of the above"),

("13. What is true about a correlated subquery?", 
 ["a) Executes once per outer row", "b) Executes once overall", "c) Uses temporary table", "d) Executes after outer query"], 
 "a) Executes once per outer row"),

("14. In SQL, which command is used to revoke privileges?", 
 ["a) REMOVE", "b) REVOKE", "c) DROP", "d) DELETE"], 
 "b) REVOKE"),

("15. Triggers in SQL are executed:", 
 ["a) Automatically when a condition occurs", "b) Manually by user", "c) Only at startup", "d) Only after commit"], 
 "a) Automatically when a condition occurs"),

("16. Which of the following is a dynamic SQL feature?", 
 ["a) Queries compiled at runtime", "b) Views", "c) Stored procedure", "d) Trigger"], 
 "a) Queries compiled at runtime"),

("17. In relational algebra, σ(A>5)(R) means:", 
 ["a) Selection of tuples where A>5", "b) Projection of A>5", "c) Rename relation", "d) Join operation"], 
 "a) Selection of tuples where A>5"),

("18. A relation is in BCNF if:", 
 ["a) It is in 3NF and every determinant is a candidate key", "b) It is in 2NF only", "c) All attributes are atomic", "d) It has no transitive dependency"], 
 "a) It is in 3NF and every determinant is a candidate key"),

("19. A multivalued dependency A →→ B means:", 
 ["a) B uniquely determines A", "b) A determines multiple independent sets of B", "c) B is functionally dependent on A", "d) A is fully functionally dependent on B"], 
 "b) A determines multiple independent sets of B"),

("20. 4NF deals with:", 
 ["a) Functional dependencies", "b) Multivalued dependencies", "c) Join dependencies", "d) Transitive dependencies"], 
 "b) Multivalued dependencies"),

("21. 5NF deals with:", 
 ["a) Elimination of multivalued dependency", "b) Join dependency elimination", "c) Functional dependency simplification", "d) Partial dependency removal"], 
 "b) Join dependency elimination"),

("22. Which data structure is used by B+-tree for indexing?", 
 ["a) Linked list", "b) Balanced binary tree", "c) Multiway search tree", "d) Hash table"], 
 "c) Multiway search tree"),

("23. Which of the following statements about B+ tree is false?", 
 ["a) Leaf nodes are linked", "b) Keys are duplicated in internal nodes", "c) Searching requires visiting all levels", "d) It supports range queries efficiently"], 
 "c) Searching requires visiting all levels"),

("24. Hashing is inefficient when:", 
 ["a) Dataset is small", "b) Range queries are frequent", "c) Keys are unique", "d) Hash table is sparse"], 
 "b) Range queries are frequent"),

("25. In two-phase locking, a transaction cannot acquire locks after releasing one because:", 
 ["a) It ensures serializability", "b) It reduces concurrency", "c) It avoids deadlock", "d) It improves throughput"], 
 "a) It ensures serializability"),

("26. Deferred update recovery method keeps log entries:", 
 ["a) Before actual write to database", "b) After writing to database", "c) Only during commit", "d) During rollback"], 
 "a) Before actual write to database"),

("27. Buffer management in DBMS aims to:", 
 ["a) Reduce disk I/O", "b) Increase normalization", "c) Control transactions", "d) Optimize SQL"], 
 "a) Reduce disk I/O"),

("28. In DAC (Discretionary Access Control):", 
 ["a) Access is controlled by system", "b) Access is granted by data owner", "c) Access is based on user role", "d) Access depends on clearance level"], 
 "b) Access is granted by data owner"),

("29. The CAP theorem states that a distributed database cannot simultaneously guarantee:", 
 ["a) Consistency, Availability, Partition tolerance", "b) Accuracy, Portability, Security", "c) Atomicity, Consistency, Durability", "d) Concurrency, Atomicity, Partitioning"], 
 "a) Consistency, Availability, Partition tolerance"),

("30. Which NoSQL database model stores data as documents?", 
 ["a) Column-family", "b) Key-value", "c) Graph", "d) Document-oriented"], 
 "d) Document-oriented")
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
