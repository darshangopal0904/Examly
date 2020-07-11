#ALGORITHM TO PREDICT THE CODING SKILL SCORE OF STUDENTS ON VARIOUS PROGRAMMING LANGUAGES

#AIM:
	To predict the coding skill score of students on various programming languages using the given parameters.
1) The number tests / questions attempted by the student
2) Scores in each test
3) Number of questions in each test
4) Coding / programming language used in each question
5) Number of learning videos viewed by the student
6) Category of learning videos viewed by the student – matching the programming
     language
7) Number of practice tests attempted by the student
8) Scores in each test
9) Question wise data
   a) Type of question -- MCQ, Fillup, Programming etc
   b) Difficulty level of the question
   c) Time taken to answer this question
   d) If programming question number of times the code was compiled
   e) If MCQ question number of times answer was changed
   f) Average time taken by other students to solve this question
   g) Total number of students who have attempted this question
   h) Number of students who have attempted this question correctly
   i) Number of students who have attempted this question wrongly

#PROGRAMMING LANGUAGE AND PLATFORM USED:
	Programming Language: Python
	Platform: Google Colab, Anaconda prompt

#DESCRIPTION AND PROOF OF CONCEPT:
	The dataset consist of the number tests / questions attempted by the student. Scores in each test, Number of questions in each test, Coding / programming language used in each question, Number of learning videos viewed by the student, Category of learning videos viewed by the student – matching the programming language, Number of practice tests attempted by the student, Scores in each test, Type of question -- MCQ, Fillup, Programming etc, Difficulty level of the question, Time taken to answer this question, If programming question number of times the code was compiled, If MCQ question number of times answer was changed, Average time taken by other students to solve this question, Total number of students who have attempted this question, Number of students who have attempted this question correctly, Number of students who have attempted this question wrongly, First the dataset is created by taking into account the above mentioned parameters. Then I started to create a regression algorithm. First, import the CSV file that we saved earlier into a pandas DataFrame. Now that we have loaded the data, we can see the shape of the data, find out how many different classes are there in the data, and get the basic idea about the distribution of the data by looking at the value of the mean, standard deviation, percentile distribution for the numeral values.	Let’s split the data into input and output. We will take the 17 features as input X and the difficulty class as output Y.	Now, we split the dataset further into training and test dataset, where 0.3 percent of the total dataset is split as a test set. X_train is the training input, y_train is the training output, X_test is the test input and y_test is the test output.	Let's build a regression model using the training dataset. Now the values are predicted using the test data set and is compares with the original value that is to be predicted. We can visually see the difference by plotting the actual verses predicted data.	We then calculate the error values.
 
	
#ALGORITHM:
This algortihm will help the user to find the student skill score in various programming languages.

1)Import the necessary libraries.

2)Import the dataset.

3)Print the dataset to check wheteher the dataset is properly loaded.

4)Check the shape of the dataset.

5)Get the basic idea about the distribution of the data by printing the values of the mean, standard deviation, percentile distribution for the numeral values.

6)Split the data into input and output.

7)The skill score level is our output and the remaining factors are taken as input.

8)Then split the dataset further into training and test dataset, where 0.3 percent of the total dataset is split as a test set. 

9)X_train is the training input, y_train is the training output, X_test is the test input and y_test is the test output.

10)Build a simple regression model using sklearn python library and train the model using the training dataset.

11)Now we have a trained simple regression model, which we will now use to predict the student skill score.

12)Print the predicted and actual score to see the resemblance of our prediction.

13)Plot a bar graph to represent the similarity between the actual and predicted value.

14)Calculate the error percentage and print it.
