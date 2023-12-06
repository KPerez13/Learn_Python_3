#You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#Step1, create a list called subjects and fill it with the classes you are taking:
#"physics"
#"calculus"
#"poetry"
#"history"

subjects=["physics", "calculus", "poetry", "history"]

#Step2, Create a list called grades and fill it with your scores: 98, 97, 85, 88

grades=[98,97,85,88]

#Step3, Manually (without any methods) create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.
#Name 	Test Score
#"physics" 	98
#"calculus" 	97
#"poetry" 	85
#"history" 	88
#Assign the value into a variable called gradebook.

gradebook=[["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#Step4
#Print gradebook. Does it look how you expected it would?
print(gradebook)

#output should look like this:
#[['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]

#Step5
#Your grade for your computer science class just came in! You got a perfect score, 100!
#Use the .append() method to add a list with the values of "computer science" and an associated grade value of 100 to our two-dimensional list of gradebook.

gradebook.append(["computer science",100])
print(gradebook)

# Step6
# Your grade for "visual arts" just came in! You got a 93!
# Use append to add ["visual arts", 93] to gradebook.

gradebook.append(["visual arts", 93])
#test to see if this works, looks like it does :) print(gradebook)

#Step 7
#Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.
#Access the index of the grade for your visual arts class and modify it to be 5 points greater.

