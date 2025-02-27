from tkinter import *  # Importing all classes from tkinter module
import random
names = []  # This will store user names or answers
global questions_answers

asked = []
score=0
class QuizStarter:
    def __init__(self, parent):
        background_color = "OldLace"  # Defining a background color for the GUI
        
        # Frame for the quiz interface, setting padding and background color
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        self.quiz_frame.grid()  # Placing the frame on the grid
        
        # Heading label with the quiz title, using a specific font and background color
        self.heading_label = Label(self.quiz_frame, text="NZ Road Rules", font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0, padx=20, pady=10)  # Placing the label with padding
        
        self.var1 = IntVar()  # Initialize IntVar for any future use (like storing integer values)
        
        # Label prompting the user to enter a username
        self.user_label = Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)  # Placing the label with padding
        
        # Entry box for user to input their username
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)  # Placing the entry box with padding
        
        # Button to continue, triggers the `name_collection` method when clicked
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)  # Placing the button with padding
    
    # Method to collect the entered name and store it in the `names` list
    def name_collection(self):
        name = self.entry_box.get()  # Retrieve the name entered in the entry box
        names.append(name)  # Add the name to the names list
        self.quiz_frame.destroy()  # Destroy the frame to move on to the next part (could be a quiz screen)

# Main program execution starts here
if __name__ == "__main__":  # Ensures the following code only runs if the script is executed directly
    root = Tk()  # Create the main window
    root.title("NZ Road Rules Quiz")  # Set the title of the window
    quiz_instance = QuizStarter(root)  # Create an instance of QuizStarter and pass the root window
    root.mainloop()  # Start the Tkinter event loop to display the window and wait for user interaction