from tkinter import *
from datetime import datetime, timedelta
import webbrowser
from tkinter import messagebox

w = Tk()
w.title("PYTHON Test Portal")
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

th = 8
tm = 33
ts = 0
c = datetime.now()
ch = c.hour
cm = c.minute
cs = c.second
if (ch > th) or (ch == th and cm > tm) or (ch == th and cm == tm and cs > ts):
    messagebox.showinfo("Time Delay", "Test Locked!\nAlready Test Started.\nIf you have further doubt, contact Niranjan!")
    w.destroy()

w.config(bg="#1C1C1C")

title = Label(w, text="PYTHON TEST", font=("Arial", 48, "bold"), fg="#ff4d4d", bg="#1c1c1c")
title.pack(pady=16)

timer_label = Label(w, text="", font=("Arial", 20, "bold"), fg="#00ff00", bg="#1c1c1c")
timer_label.pack(pady=6)

instruction_text = (
    "Welcome to the PYTHON Test Portal !\n\n"
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
("1. What will be the output of the expression `sorted([1, -2, 3, -4], key=lambda x: x*x)`?",
 ["a) [1, -2, 3, -4]", "b) [-2, -4, 1, 3]", "c) [1, -2, 3, -4]", "d) [1, -2, 3, -4]"],
 "b) [-2, -4, 1, 3]"),
("2. Which of these statements about Python’s GIL is TRUE?",
 ["a) It allows true multithreading on multiple CPUs", "b) It prevents multiple threads from executing Python bytecode simultaneously", "c) It improves CPU-bound performance", "d) It’s not present in CPython"],
 "b) It prevents multiple threads from executing Python bytecode simultaneously"),
("3. What is the result of `list(map(None, [1,2,3]))` in Python 3?",
 ["a) [1,2,3]", "b) [(1,), (2,), (3,)]", "c) TypeError", "d) [None,1,2,3]"],
 "c) TypeError"),
("4. Which method can be overridden to customize object printing?",
 ["a) __print__", "b) __repr__", "c) __display__", "d) __show__"],
 "b) __repr__"),
("5. What does `from __future__ import annotations` do?",
 ["a) Enables postponed evaluation of annotations", "b) Imports all annotations automatically", "c) Disables type checking", "d) Converts annotations to comments"],
 "a) Enables postponed evaluation of annotations"),
("6. What is the difference between `is` and `==` in Python?",
 ["a) `is` checks equality, `==` checks identity", "b) Both are identical", "c) `is` checks identity, `==` checks equality", "d) None of the above"],
 "c) `is` checks identity, `==` checks equality"),
("7. What will be printed by `a=[[]]*3; a[0].append(10); print(a)`?",
 ["a) [[10],[],[]]", "b) [[10],[10],[10]]", "c) [[],[],[10]]", "d) SyntaxError"],
 "b) [[10],[10],[10]]"),
("8. Which of the following creates an immutable sequence?",
 ["a) list()", "b) tuple()", "c) set()", "d) dict()"],
 "b) tuple()"),
("9. What is the output of `bool(0.0 or 0)`?",
 ["a) True", "b) False", "c) None", "d) 0"],
 "b) False"),
("10. In Python, closures are created when:",
 ["a) A function is defined inside another function and references variables from outer scope", "b) Global variables are modified", "c) A class inherits another", "d) A decorator is defined"],
 "a) A function is defined inside another function and references variables from outer scope"),
("11. Which will result in a valid decimal comparison?",
 ["a) Decimal('1.1') == 1.1", "b) Decimal('1.1') == Decimal(1.1)", "c) Decimal('1.1') == Decimal('1.1')", "d) All of the above"],
 "c) Decimal('1.1') == Decimal('1.1')"),
("12. Which of these statements about Python generators is FALSE?",
 ["a) They are iterators", "b) They store entire sequence in memory", "c) They can be iterated once", "d) They use `yield` keyword"],
 "b) They store entire sequence in memory"),
("13. Which operator has higher precedence?",
 ["a) not", "b) and", "c) or", "d) in"],
 "a) not"),
("14. What is output of `a=(1,2,3); b=(1,2,3); a is b`?",
 ["a) True", "b) False", "c) None", "d) Error"],
 "b) False"),
("15. Which method in context managers is always executed?",
 ["a) __enter__", "b) __exit__", "c) __del__", "d) close"],
 "b) __exit__"),
("16. How does `@staticmethod` differ from `@classmethod`?",
 ["a) classmethod gets class as first arg, staticmethod gets none", "b) staticmethod gets class, classmethod gets instance", "c) both same", "d) staticmethod can access class vars"],
 "a) classmethod gets class as first arg, staticmethod gets none"),
("17. What is the output of `all([])`?",
 ["a) False", "b) True", "c) Error", "d) None"],
 "b) True"),
("18. What will `re.match('a*b','aaab')` return?",
 ["a) None", "b) Match object", "c) True", "d) False"],
 "b) Match object"),
("19. What happens if a dictionary key is mutable?",
 ["a) Raises TypeError", "b) Works fine", "c) Converts to string", "d) Stores hash of key"],
 "a) Raises TypeError"),
("20. What does `locals()` return?",
 ["a) Dictionary of local symbol table", "b) List of locals", "c) Global vars", "d) None"],
 "a) Dictionary of local symbol table"),
("21. Which module implements abstract base classes?",
 ["a) abc", "b) base", "c) abstract", "d) collections"],
 "a) abc"),
("22. What is the result of `set([1,2,2,3])`?",
 ["a) {1,2,3}", "b) [1,2,2,3]", "c) (1,2,3)", "d) {1,1,2,3}"],
 "a) {1,2,3}"),
("23. What will `list(zip(*[[1,2,3],[4,5,6]]))` produce?",
 ["a) [(1,4),(2,5),(3,6)]", "b) [(1,2,3),(4,5,6)]", "c) [(1,2),(4,5),(3,6)]", "d) Error"],
 "a) [(1,4),(2,5),(3,6)]"),
("24. In Python, decorators are applied:",
 ["a) At runtime", "b) At compile-time", "c) During interpretation", "d) Before bytecode generation"],
 "a) At runtime"),
("25. What is the output of `sum([i for i in range(3)], start=10)`?",
 ["a) 13", "b) 16", "c) 10", "d) 6"],
 "b) 16"),
("26. How can you force garbage collection manually?",
 ["a) gc.collect()", "b) del()", "c) sys.gc()", "d) gc()"],
 "a) gc.collect()"),
("27. What does `hash()` function return?",
 ["a) Memory address", "b) Unique string", "c) Integer hash value", "d) Encoded bytes"],
 "c) Integer hash value"),
("28. The expression `{True: 'A', 1: 'B', 1.0: 'C'}` results in:",
 ["a) {'A': True, 'B': 1, 'C': 1.0}", "b) {True:'A',1:'B',1.0:'C'}", "c) {True:'C'}", "d) {1:'C'}"],
 "d) {1:'C'}"),
("29. In Python 3, which is valid way to merge two dicts?",
 ["a) dict1 + dict2", "b) dict1.update(dict2)", "c) dict1 | dict2", "d) merge(dict1,dict2)"],
 "c) dict1 | dict2"),
("30. What will be the output of `''.join(sorted('banana'))`?",
 ["a) banana", "b) aaabnn", "c) aaannb", "d) aabann"],
 "b) aaabnn")
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
nav_buttons = {}

def show_question(index):
    global option_widgets
    q, opts, correct = questions[index]
    question_label.config(text=q)
    for rb in option_widgets:
        rb.destroy()
    option_widgets.clear()
    sv = answer_vars[q]["var"]
    for opt in opts:
        rb = Radiobutton(q_area, text=opt, variable=sv, value=opt, font=("Arial", 14), bg="#1c1c1c", fg="white", selectcolor="#1c1c1c", activebackground="#1c1c1c", anchor="w", justify=LEFT, command=update_nav_colors)
        rb.pack(fill=X, anchor="w", padx=20, pady=2)
        option_widgets.append(rb)
    page_label.config(text=f"Question {index+1} / {len(questions)}")
    update_nav_colors()

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

def jump_to_question(i):
    global current_index
    current_index = i
    show_question(current_index)

def update_nav_colors():
    for i, (q, data) in enumerate(answer_vars.items()):
        if data["var"].get():
            nav_buttons[i].config(bg="#00cc66")
        else:
            nav_buttons[i].config(bg="#ff4d4d")
    nav_buttons[current_index].config(bg="yellow")

def create_quiz_ui():
    global quiz_frame, q_area, question_label, option_widgets, submit_btn, next_btn, prev_btn, page_label, nav_buttons
    main_frame = Frame(w, bg="#1c1c1c")
    main_frame.pack(fill=BOTH, expand=True)
    quiz_frame = Frame(main_frame, bg="#1c1c1c")
    quiz_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=12)
    nav_frame = Frame(main_frame, bg="#262626", width=200)
    nav_frame.pack(side=RIGHT, fill=Y, padx=10, pady=10)
    nav_label = Label(nav_frame, text="Questions", font=("Arial", 16, "bold"), fg="white", bg="#262626")
    nav_label.pack(pady=6)
    nav_buttons.clear()
    grid_frame = Frame(nav_frame, bg="#262626")
    grid_frame.pack(pady=8)
    for i in range(len(questions)):
        btn = Button(grid_frame, text=str(i+1), width=4, height=1, font=("Arial", 12, "bold"), command=lambda i=i: jump_to_question(i), bg="#ff4d4d", fg="white", relief=FLAT)
        btn.grid(row=i//5, column=i%5, padx=3, pady=3)
        nav_buttons[i] = btn
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
