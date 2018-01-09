#As a first step, clear your environment from any existing data
rm(list = ls())

#clear existing plots (if any)
dev.off()

#First, we will start by loading our dataset. As a start we will use a default dataset provided by R
Heart <- read.csv("D:/RLan/Heart.csv")
#The dataset is called Heart:
help(Heart)

#always make a copy of the data to work on to have a backup ready for your original data!
data <- Heart

#start by exploring your data using the summary function
summary(data)

#Cluster your data for discovering the natural groups (iris species)
install.packages("ggplot2")
library(ggplot2)

qplot(ID, Age, Sex, RestBP, Chol, Fbs, RestECG, MaxHR, ExAng, Oldpeak, Slope, Ca, data = Heart)

#For this part we will use decision trees and random forests. Start by installing these packages
#these packages are used to build a CART: Classification and Regression Tree
install.packages("rpart")
library(rpart)

install.packages("caret")
library(caret)

#before we build our models, we will divide our dataset into a training set and a test set to avoid 
#overfitting. The training set is used to build the model and the test set is used to validate it

#we start by using this function from the CARET package to partition our dataset
#we set p: the percentage of data that goes to training into 0.7, thus, 70% of data is used for
#training to capture the main characterstics and the other 30% is used for validation
train.flag <- createDataPartition(y = Heart$ID, p=0.7, list=FALSE)

#set the training data
training <- Heart[train.flag,]

#set the left data to validation
Validation <- Heart[-train.flag,]

#before we go on and build our models, we want to make sure to implement the cross validation 
#to avoid overfitting
control <- trainControl(method = "cv", number=10)
metrix <- "Accuracy"

#now we build the model using the training data
#in the first part, we specifiy our dependent variable (Species) ~ . the dot represents all the other
#explanatory variables in the dataset which can be rewritten as Species ~ Sepal.Length + Sepal.Width + ..
#the method rpart is Recursive Partitioning and Regression Trees which builds the decision tree
#we also make sure to add metric and trControl attributes to build the model with 10-fold cross validation
#before training each model, we will use the set.seed function to make sure our results are reproducable!

set.seed(10)
tree_model <- train(ID ~ ., method="rpart", data=training, metric=metrix, trControl=control)

#summarize the model
summary(tree_model)
tree_model

#to plot the tree model we will use the following package
install.packages("rattle")
library(rattle)

fancyRpartPlot(tree_model$finalModel)

#now that we built the model, we need to validate it
#to do so, we use the predict function
#as a first step, we will try to predict with the same data we trained our model with
train.cart <- predict(tree_model, newdata = training)

#here we will show the original values vs the predicted ones
table(train.cart, training$ID)

#now we will predict using the test set
pred.cart <- predict(tree_model, newdata = Validation)

#here we will show the original values vs the predicted ones
table(pred.cart, Validation$ID)

#now let's try to plot the missclassified observations 
correct <- pred.cart == Validation$ID

qplot(ID, Age, Sex, RestBP, Chol, Fbs, RestECG, MaxHR, ExAng, Oldpeak, Slope, Ca, data = Heart)

#calculate the confusion matrix
confusionMatrix(pred.cart, Validation$ID)

#now we will implement a Random Forest model using the following packages
install.packages("randomForest")
library(randomForest)

install.packages("randomForestSRC")
library(randomForestSRC)

#now we build the model using the training dataset as before
#don't forget to set the seed

set.seed(10)
random_forest_model <- train(ID ~ ., method="rf", data=training, metric=metrix, trControl=control)

#summarize the random forest model
summary(random_forest_model)
random_forest_model

#in our first model, we were able to show the decision tree. However, in the case of a random forest
#we look more for variables importance to be able to decide which variables are most imprtant and
#which ones can be ignored. For that we will use varImp function

var_importance <- varImp(random_forest_model)
plot(var_importance)

#predict using training data
train.rf <- predict(random_forest_model, newdata = training)

#show the results 
table(train.rf, training$ID)

#now we will predict using the test set
pred.rf <- predict(random_forest_model, newdata = Validation)

#here we will show the original values vs the predicted ones
table(pred.rf, Validation$ID) 

#calculate the confusion matrix
confusionMatrix(pred.rf, Validation$ID)

#now let's compare the two models using the resamples function which enables us to combine the
#results from each model and plot them!

results <- resamples(list(cart = tree_model, rf = random_forest_model))
summary(results)
dotplot(results)

#For this part of the tutorial, we will use Logistic Regression 
#as a start, we want to create a subset of the iris dataset. The reason is because we want to
#demonstrate the logistic regression which is applicable on a binary dependent variable, however,
#the dependent variable (Species) contains three possible values, so we will take a small subset
#that contains verginica and versicolor species
attach(Heart)

#install and call this package to use the filter function to subset your data
install.packages("dplyr")
library(dplyr)



#now we build the model using glm function. GLM stands for generalized linear models. 
#we set the family to binomial with a logit link to specifiy the model we want which is logstic regression
logit_model <- glm(ID ~ ., data = Heart, family = binomial(link="logit"))

#summarize the model
summary(logit_model)

#looking at the summary, we can have an idea about the p-values of the explanatory variables,
#thus, the significane of such variables in our model. let's try to remove the variables with higher 
#p-values and see what happens. p-values that are higher than 0.1 are mostly considered insignificant
logit_model_reduced <- glm(ID ~ .,data = Heart, family = binomial(link = "logit"))

#we can do that also by simply using the step function on the full model
step(logit_model)

#now summarize again
summary(logit_model_reduced)

#now let's plot the fitted probability as a function of the linear predictor
lr_data <- data.frame(predictor=logit_model_reduced$linear.predictors, prob=logit_model_reduced$fitted.values, ID=Heart$ID)
ggplot(lr_data, aes(x=predictor, y=prob, color=Species)) + geom_point()

#partition our new dataset
train.flag_sub <- createDataPartition(y = Heart$ID, p=0.7, list=FALSE)

#set the training data
training_sub <- Heart[train.flag_sub,]

#set the left data to validation
Validation_sub <- Heart[-train.flag_sub,]

#now let's predict
install.packages("ROCR")
library(ROCR)

pred.logit <- predict(logit_model_reduced, newdata = Validation_sub, type = "response")

#the results we get from the prediction is a probability of a specific category to occur, accordingly
#we add prob as a 6th variable to the validation dataset so that we can compare between the predicted
#value and the original one
Validation_sub$prob <- pred.logit

#we can see that the original values are wither 0 or 1 while the probability is a value between 0 and 1
#accordingly, we use the prediction function to transform the probabilities into a standard format
my_pred <- prediction(Validation_sub$prob, Validation_sub$ID)

#now, to evaluate out predictions, we are going to use the performance funtion and calculate two 
#values: tpr is true positive rate which indicates the ratio of predictions that were correctly
#classified and fpr which is false positive rate which indicates the ratio of predictions that were
#misclassified. These value will produce our ROC curve which is used to evaluate our model
my_roc<- performance(my_pred, "tpr", "fpr")
plot(my_roc)

#now we use the same function to calculate the accuracy
my_auc <- performance(my_pred, measure = "auc")
my_auc@y.values