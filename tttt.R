# clear your environment from any existing data
rm(list = ls())

# clear existing plots
dev.off()

# First, we will start by loading our dataset
Heart <- read.csv(file.choose())
data <- Heart
# Logistic Regression part

# split data
set.seed(10)
train <- createDataPartition(data$AHD, p = 0.7, list = FALSE)
trainning <- data[train, ]
test  <-  data[-train, ]
# fit and summary
LRModel <- train(AHD ~., data = trainning, method = "glm", family = "binomial")
summary(Model)
# predict
fitted.results <- predict(LRModel,newdata = test,type='prob')
fitted.results <- ifelse(fitted.results > 0.5,1,0)
misClasificError <- mean(fitted.results != test$AHD)
print(paste('Accuracy',1-misClasificError))


# help(Heart)

# # make a copy of the data to work on 
# data <- Heart
# # pre-process data
# head(data)
# dim(data)
# summary(data)

# # download and install packages
# install.packages("rpart")
# install.packages("caret")
# install.packages("plotly")
# install.packages("rattle")
# install.packages("randomForest")
# install.packages("randomForestSRC")
# install.packages("dplyr")
# install.packages("ggplot2")
# install.packages("ROCR")
# library(ROCR)
# library(ggplot2)
# library(dplyr)
# library(randomForest)
# library(randomForestSRC)
# library(rattle)
# library(rpart)
# library(caret)
# library(plotly)

# # clusters the data based on disease or not
# p <- plot_ly(data, x = data$Age, y = data$AHD, 
# color = data$AHD, colors = "Set1", mode = "markers")
# p

# # set.seed function to make sure our results are reproducable
# set.seed(10)

# # we will divide our dataset into a training set and a test set 
# train.flag <- createDataPartition(y = Heart$AHD, p=0.7, list=FALSE)
# training <- Heart[train.flag,]
# Validation <- Heart[-train.flag,]

# # before we go on and build our models, we want to make sure to implement the cross validation 
# # to avoid overfitting
# control <- trainControl(method = "cv", number=10)
# metrix <- "Accuracy"

# # we specifiy our dependent variable
# # add metric and trControl attributes to build the model with 10-fold cross validation

# tree_model <- train(Age ~ ., method="rpart", data=training, metric=metrix, trControl=control)

# #summarize the model
# summary(tree_model)
# tree_model

# fancyRpartPlot(tree_model$finalModel)

# # validate the model
# # predict with the same data we trained our model with
# train.cart <- predict(tree_model, newdata = training)

# # show the original values vs the predicted ones
# table(train.cart, training$AHD)

# # predict using the test set
# pred.cart <- predict(tree_model, newdata = Validation)

# # show the original values vs the predicted ones
# table(pred.cart, Validation$AHD)

# # plot the missclassified observations 
# correct <- pred.cart == Validation$AHD

# p <- plot_ly(Validation, x = data$Age, y = data$AHD, 
# color = correct, colors = "Set1", mode = "markers")
# p

# #calculate the confusion matrix
# confusionMatrix(pred.cart, Validation$AHD)

# # build the model using the training dataset
# set.seed(10)
# random_forest_model <- train(Age ~ ., method="rf", data=training, metric=metrix, trControl=control)

# # summarize the random forest model
# summary(random_forest_model)
# random_forest_model

# # use varImp function to decide which variables are most imprtant and which ones can be ignored
# var_importance <- varImp(random_forest_model)
# plot(var_importance)

# # predict using training data
# train.rf <- predict(random_forest_model, newdata = training)

# # show the results 
# table(train.rf, training$AHD)

# # now we will predict using the test set
# pred.rf <- predict(random_forest_model, newdata = Validation)

# # here we will show the original values vs the predicted ones
# table(pred.rf, Validation$AHD) 

# # calculate the confusion matrix
# confusionMatrix(pred.rf, Validation$AHD)

# # compare the two models 
# results <- resamples(list(cart = tree_model, rf = random_forest_model))
# summary(results)
# dotplot(results)


# # Logistic Regression 
# # don't have to create a subset of Heart dataset for AHD has only two possible values

# # build the model using glm function
# logit_model <- glm(num ~ ., data = Heart, family = binomial(link="logit"))

# # summarize the model
# summary(logit_model)

# # remove the variables with higher p-values
# logit_model_reduced <- glm(num ~ .,data = Heart, family = binomial(link = "logit"))

# # using the step function on the full model
# step(logit_model)

# # now summarize again
# summary(logit_model_reduced)

# # now let's plot the fitted probability as a function of the linear predictor
# lr_data <- data.frame(predictor=logit_model_reduced$linear.predictors, prob=logit_model_reduced$fitted.values, num = Heart$AHD)
# ggplot(lr_data, aes(x=predictor, y=prob, color=Species)) + geom_point()

# # partition our new dataset
# train.flag_sub <- createDataPartition(y = Heart$AHD, p=0.7, list=FALSE)

# # set the training data
# training_sub <- Heart[train.flag_sub,]

# # set the left data to validation
# Validation_sub <- Heart[-train.flag_sub,]

# # predict
# pred.logit <- predict(logit_model_reduced, newdata = Validation_sub, type = "response")

# #the results we get from the prediction is a probability of a specific category to occur, accordingly
# #we add prob as a 6th variable to the validation dataset so that we can compare between the predicted
# #value and the original one
# Validation_sub$prob <- pred.logit

# # transform the probabilities into a standard format
# my_pred <- prediction(Validation_sub$prob, Validation_sub$AHD)

# # plot model ROC curve
# my_roc<- performance(my_pred, "tpr", "fpr")
# plot(my_roc)

# # calculate the accuracy
# my_auc <- performance(my_pred, measure = "auc")
# my_auc@y.values