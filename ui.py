from tkinter import *
from quiz_brain import *


THEME_COLOR = "#375362"
# canvas_font = ("Arial, 20, italic")   #must be in tuple form, which this is, BUT it's not in proper Font tuple format, so it must be:
canvas_font = ("Arial", 20, "italic")   # name of the font, size, special text style


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # we will create our UI User Interface  inside this Class  # dont need this: padding=20, color=THEME_COLOR, font=canvas_font, height=250, width=300)
        self.quiz = quiz_brain

        self.window = Tk()   #instead of creating our window as a simple variable, we will create a window from the property of this Class (QuizInterface), so we use self. but from a Tkinter Module, and a window will be a new object from the tk Class.
        self.window.title("Quizli")  # to change some aspects of the window, and we can continue like this inside the init function

        # <place anything here you want for the window, and as long as the .mainloop() is applied and there are no running while loops in the same project, all will be fine.>

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)    #text is fg, so we make it white
        self.score_label.grid(row=0, column=1)

        # setting up the canvas, which we can add different layers to it, and make it whatever size we want it to:
        self.canvas = Canvas(width=300, height=250, bg="white")  # white makes it stand out like a card, with the darker bg
        # the canvas width from above is set to 300, so let's set it to 280 in the with below, to make it wrapped text:
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=canvas_font)  #don't forget: when we add an image or something to a canvas, we have to provide an x and y pos for placement.
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        true_image = PhotoImage(file="images/true.png")   #no text involved, on either buttons - # Note: we did not use self. on any of the true or false images, because we won't be using those images for anything else other than that particular thing.
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_pressed)   # check_answer   # self.true_button
        self.true_button.grid(row=2, column=0)  # IF you wanted to have only 1 button and have it perfectly centered, then all you have to do is use: columnspan=2) and it will take over both spots equally in the middle, and you don't have to guess the pixel location.

        false_image = PhotoImage(file="images/false.png")  # no text involved, on either buttons - # Note: we did not use self. on any of the true or false images, because we won't be using those images for anything else other than that particular thing.
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(row=2, column=1)


        # Because we used self. in every single line within the __init__ creation/instantiation. The self. turns that item into a property, which can be accessed anywhere in the class.
        # Note: we did not use self. on any of the true or false images, because we won't be using those images for anything else other than that particular thing.

        self.get_next_question()

        self.window.mainloop()  # this applies here (can be at the end of this definition block, but still indented (only once, not 0 times). never ending while loop, so we don't want .mainloop() AND another while loop running at the same time, yes, EVEN IF IT'S IN ANOTHER LINKED MODULE OF THE SAME PROJECT!


    def get_next_question(self):  # this is going to tap into the quiz_brain.py and call this next_question() function.  #to get ahold of the same quiz_brain in our main.py file, we could pass into quiz_ui = QuizInterface() as input INSIDE the paren () - and because in the main.py file, thatwe assigned quiz to = QuizBrain(question_bank), that we can place "quiz" in the paren () to do so, like: quiz_ui = QuizInterface(quiz)
                                # and to CATCH it, we add quiz_brain as the 2nd parameter (after self, ) in the __init__ line, and THEN we can create a property called the quiz and set it equal to the quiz_brain that we receive when we initialize this new quiz interface, like: self.quiz = quiz_brain
                                # then we tap into the self.quiz, and then call the method quiz.next_question (and even though we expect it to auto-populate, it doesn't actually know what data type of the particular object (quiz_brain)).
                                # To fix that issue, you can actually add the datatype in when you create it as a parameter - an you must import in the ui.py file (should be this file) "from quiz_brain import QuizBrain", it must be DataType 'QuizBrain' (which is a Class).
                                # Yes, you can create a QuizBrain Object, QuizBrain Class, which means you can have a QuizBrain DATATYPE!
                                # in the __init__ creation, you would write:
                                #   def __init__(self, quiz_brain: QuizBrain):  # we will create our UI User Interface  inside this Class  # dont need this: padding=20, color=THEME_COLOR, font=canvas_font, height=250, width=300)
                                # self.quiz = quiz_brain
        self.canvas.config(bg="white")   # moving this line OUTSIDE the If statement will make the background white no matter what happens
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()  # we know this is going to give us the output, so this is the q_text
            self.canvas.itemconfig(self.question_text, text=q_text)    # then update the canvas screen
            #then call this method, which we do in our __init__, so that we we first initialize our user interface, we don't end up seeing "some question text" but we get the 1st question from our list of questions whiuch we extracted using our API.
            # But remember that everything must go before our mainloop()
            # so place this above the mainloop():     self.get_next_question()
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")    # we also want to disable our True and False buttons, to prevent them from being pressed or activated
            self.false_button.config(state="disabled")  # we also want to disable our True and False buttons, to prevent them from being pressed or activated

    def true_button_pressed(self):
        #is_right = self.quiz.check_answer("True")  # ("True"), not (True)  # because quiz = QuizBrain(question_bank) *in main, doing this: self.quiz.check_answer("True"), will pass True into def check_answer(self, user_answer): *in quiz_brain, and will check the user_answer against the correct answer.
        self.give_feedback_to_user(self.quiz.check_answer("True"))       #then pass in the output ( self.quiz.check_answer("True") ) to this method call ( self.give_feedback_to_user() ) but put it inside the () part, and then delete the above line ( is_right = self.quiz.check_answer("True")  )
        # print("The True button was pressed")

    def false_button_pressed(self):
        is_right = self.quiz.check_answer("False")   # ("False"), not (False)   #this line and the one below this, do exactly the same as: self.give_feedback_to_user(self.quiz.check_answer("False"))
        self.give_feedback_to_user(is_right)
        # print("The False button was pressed")

    def give_feedback_to_user(self, is_right):
        if is_right:    # NOT if self.quiz.check_answer == "True":
            self.canvas.config(bg="green")  # NO NEED TO DO THIS before bg="green": Canvas(width=300, height=250,
        # self.window.after(1000, self.get_next_question)  # because we need to use a time.sleep() functionality, but cannot, due to the mainloop() running, we use self.window.after()
        # self.canvas.config(bg="white")    # no need for: = Canvas(width=300, height=250,

        else:   # NOT if self.quiz.check_answer  == "False":     # and not: elif not is_right
            self.canvas.config(bg="red")    # no need for Canvas(width=300, height=250,
        self.window.after(1000, self.get_next_question)   # after 1000ms, we want to actually go to the next question, so call that function! (but REMOVE PAREN (), like you would on a button func call (withoout paren)  # because we need to use a time.sleep() functionality, but cannot, due to the mainloop() running, we use self.window.after()
        # self.canvas.config(bg="white")   # no need for:  Canvas(width=300, height=250,   # because of timing delay: move this line to the beginning of the next_question





        # self.font = font
        # # self.padding = padding(20)  #pady= padx= ?
        # timer_label = Label(text="This is old text", fg=GREEN, bg=YELLOW, font=(font)  # color=GREEN
        # self.label = Label(self.window, text="Amazon aquired Twitch in August 2014 for $970 million dollars.", fg="white", bg=theme_color)
        # self.height = height
        # self.width = width
        # self.THEME_COLOR = color(THEME_COLOR)
        # # self.font = font(canvas_font)
        # # others we Could use: grid()     “padx” and “pady

