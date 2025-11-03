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

th = 13
tm = 10
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
    "--> Submit button appears after 20 minutes.\n"
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
("1. In Python, identifiers are case-sensitive because:",
 ["a) Python is a weakly typed language", "b) Python internally converts all names to lowercase", "c) Python maintains separate namespaces for different cases", "d) Python ignores letter casing"],
 "c) Python maintains separate namespaces for different cases"),
("2. Which of the following is not a valid Python identifier?",
 ["a) _data", "b) data_123", "c) 123data", "d) data123"],
 "c) 123data"),
("3. The output of type(3/2) in Python 3 is:",
 ["a) int", "b) float", "c) double", "d) complex"],
 "b) float"),
("4. In Python, the expression 2 ** 3 ** 2 evaluates to:",
 ["a) 64", "b) 512", "c) 256", "d) 8"],
 "b) 512"),
("5. Which of the following statements about Python variables is true?",
 ["a) Variables must be declared before use", "b) Type must be specified explicitly", "c) Variables are created when assigned a value", "d) Variable names cannot start with underscore"],
 "c) Variables are created when assigned a value"),
("6. What will be the result of: bool('False')?",
 ["a) False", "b) True", "c) 0", "d) Error"],
 "b) True"),
("7. Which of the following statements will raise an error?",
 ["a) a,b=10,20", "b) a=b=c=10", "c) a,b=10", "d) a=10;b=20"],
 "c) a,b=10"),
("8. What is the output of: print(10//3)?",
 ["a) 3.33", "b) 3", "c) 4", "d) 3.0"],
 "b) 3"),
("9. In Python, which statement skips the remaining code in the current iteration?",
 ["a) break", "b) continue", "c) pass", "d) skip"],
 "b) continue"),
("10. In the try-except block, if no exception occurs:",
 ["a) except block executes", "b) finally block executes only", "c) both try and except execute", "d) only try block executes"],
 "d) only try block executes"),
("11. Which list operation creates a shallow copy?",
 ["a) new_list = old_list.copy()", "b) new_list = old_list[:]", "c) new_list = list(old_list)", "d) All of the above"],
 "d) All of the above"),
("12. The output of len([[]]) is:",
 ["a) 0", "b) 1", "c) 2", "d) Error"],
 "b) 1"),
("13. Which list method removes and returns the last element?",
 ["a) remove()", "b) pop()", "c) discard()", "d) del"],
 "b) pop()"),
("14. In Python, dictionaries are implemented as:",
 ["a) Lists", "b) Hash tables", "c) Arrays", "d) Sets"],
 "b) Hash tables"),
("15. What happens if you access a missing key in a dictionary using []?",
 ["a) Returns None", "b) Returns False", "c) Raises KeyError", "d) Returns empty dictionary"],
 "c) Raises KeyError"),
("16. Which function returns a list of dictionary keys?",
 ["a) keys()", "b) dictkeys()", "c) keylist()", "d) listkeys()"],
 "a) keys()"),
("17. Which of the following tuples is immutable?",
 ["a) (1,2,[3,4])", "b) (1,2,3)", "c) (1,{2:3})", "d) ([])"],
 "b) (1,2,3)"),
("18. The output of tuple([1,2,3]) is:",
 ["a) [1,2,3]", "b) (1,2,3)", "c) {1,2,3}", "d) Error"],
 "b) (1,2,3)"),
("19. What is the result of len(set('mississippi'))?",
 ["a) 11", "b) 7", "c) 4", "d) 8"],
 "c) 4"),
("20. Which of the following is true about frozenset?",
 ["a) Mutable and hashable", "b) Immutable and hashable", "c) Mutable and unhashable", "d) Immutable and unhashable"],
 "b) Immutable and hashable"),
("21. Which function in Python is used to get multiple return values?",
 ["a) return tuple", "b) yield", "c) multiple()", "d) None"],
 "a) return tuple"),
("22. What is the default return type of a Python function without a return statement?",
 ["a) 0", "b) False", "c) None", "d) Empty string"],
 "c) None"),
("23. The *args parameter is used to:",
 ["a) Pass multiple key-value arguments", "b) Pass a variable number of positional arguments", "c) Define constants", "d) Pass dictionary arguments"],
 "b) Pass a variable number of positional arguments"),
("24. What will print(len('Hello')) output?",
 ["a) 4", "b) 5", "c) 6", "d) Error"],
 "b) 5"),
("25. Which string method removes leading and trailing spaces?",
 ["a) strip()", "b) trim()", "c) remove()", "d) clear()"],
 "a) strip()"),
("26. The expression ','.join(['a','b','c']) outputs:",
 ["a) ['a','b','c']", "b) 'a,b,c'", "c) 'abc'", "d) ('a','b','c')"],
 "b) 'a,b,c'"),
("27. What happens if you open a file in 'w' mode that already exists?",
 ["a) Appends data", "b) Deletes file", "c) Overwrites file", "d) Raises error"],
 "c) Overwrites file"),
("28. Which method reads one line from a file?",
 ["a) read()", "b) readline()", "c) readlines()", "d) input()"],
 "b) readline()"),
("29. The pickle module is used for:",
 ["a) Text file handling", "b) Binary serialization", "c) JSON conversion", "d) CSV parsing"],
 "b) Binary serialization"),
("30. The CSV module in Python uses which default delimiter?",
 ["a) Tab", "b) Space", "c) Comma", "d) Colon"],
 "c) Comma")
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
    if correct_count > 15:
        webbrowser.open("https://hacker1514.github.io/test/python.html")
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
        timer_label.config(text=f"Quiz starts in {h:02d}H : {m:02d}M : {s:02d}S")
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
        if elapsed.total_seconds() >= 20 * 60:
            submit_btn.pack(side=RIGHT, padx=12, pady=6)
        else:
            submit_btn.pack_forget()
        if remaining_seconds <= 0:
            submit_quiz()
    w.after(1000, update_loop)

update_loop()
w.mainloop()
