ALGORITHM TO CLASSIFY THE DIFFICULTY OF QUESTION.

AIM:
	To classify the difficulty of the question using the given parameters.
1) Question type -- MCQ, Fillup, Programming, Match the following
2) Manually assigned difficulty -- Easy, Medium, Hard
3) Total number of students who have attended this question
a) Time taken by each student to answer this question
b) Number of times the answer was changed if it is MCQ type question
c) Number of times the program was compiled if it is programming question
d) Number of hints used
e) Programming language used if it is programming question (c, c++ , java etc)
4) Feedback given for this question by other students
5) Total number of students who have answered it right
6) Total number of students who have answered it wrong
7) Total number of students who have answered it partially correct
8) Maximum marks allocated for this question

PROGRAMMING LANGUAGE AND PLATFORM USED:
	Programming Language: Python
	Platform: Google Colab, Anaconda prompt

DESCRIPTION AND PROOF OF CONCEPT:
	The dataset consist of Question type -- MCQ, Fillup, Programming, Match the following,  Manually assigned difficulty -- Easy, Medium, Hard, Total number of students who have attended this question, Time taken by each student to answer this question, Number of times the answer was changed 
  if it is MCQ type question, Number of times the program was compiled if it is programming question, Number of hints used, Programming language used if it is programming question (c, c++ , java etc), Feedback given for this question by other students, Total number of students who have 
  answered it right, Total number of students who have answered it wrong, Total number of students who have answered it partially correct, Maximum marks allocated for this question.	First the dataset is created by taking into account the above mentioned parameters. Then I started to create
  a classification algorithm using the concept of XGB classifier and the decision tree. First, import the CSV file that we saved earlier into a pandas DataFrame. Now that we have loaded the data, we can see the shape of the data, find out how many different classes are there in the data, 
  and get the basic idea about the distribution of the data by looking at the value of the mean, standard deviation, percentile distribution for the numeral values. Let’s split the data into input and output. We will take the 12 features as input X and the difficulty class as output Y.
	Now, we split the dataset further into training and test dataset, where 0.3 percent of the total dataset is split as a test set. X_train is the training input, y_train is the training output, X_test is the test input and y_test is the test output.	Let's build a multi-class gradient 
  boost classifier using xgboost python library and train the classifier using the training dataset. We have a trained multi-class classifier, which we will now use to predict the classes for the test set. We will be using ROC AUC as the evaluation matrix for this model.
	We can also visually compare the expected output and the predicted output for the test dataset.	I too have also used the decision tree classifier to classify the difficulty of the questions. Let's build a decision tree classifier using sklearn python library and train the classifier 
  using the training dataset. Then I have given a sample input to test the model.
 
ALGORITHM:
This algortihm will help the user to find the difficuty of the question faced by students in tests.

1)Import the necessary libraries.

2)Import the dataset.

3)Print the dataset to check wheteher the dataset is properly loaded.

4)Check the shape of the dataset.

5)Get the basic idea about the distribution of the data by printing the values of the mean, standard deviation, percentile distribution for the numeral values.

6)Split the data into input and output.

7)The difficulty level is our output and the remaining factors are taken as input.

8)Then split the dataset further into training and test dataset, where 0.3 percent of the total dataset is split as a test set.

9)X_train is the training input, y_train is the training output, X_test is the test input and y_test is the test output.

10)Build a multi-class gradient boost classifier using xgboost python library and train the classifier using the training dataset.

11)Now we have a trained multi-class classifier, which we will now use to predict the classes for the test set.

I have also build a Decision Tree Classifier model

Use the same steps 1 to 9.

10)Build a decision tree classifier using sklearn python library and train the classifier using the training dataset.

11)Now we have a trained decision tree classifier, which we will now use to predict the classes for the test set.
