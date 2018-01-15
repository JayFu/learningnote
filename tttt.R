# clear your environment from any existing data
rm(list = ls())

# clear existing plots
dev.off()

# First, we will start by loading our dataset
Heart <- read.csv(file.choose())
data <- Heart

# split data
set.seed(10)
train <- createDataPartition(data$AHD, p = 0.7, list = FALSE)
trainning <- data[train, ]
test  <-  data[-train, ]

# Logistic Regression part
# Data Exploration part
LRModel <- train(AHD ~., data = trainning, method = "glm", family = "binomial")
summary(Model)

# predict
fitted.results <- predict(LRModel,newdata = test,type='prob')
fitted.results <- ifelse(fitted.results > 0.5,1,0)
misClasificError <- mean(fitted.results != test$AHD)
print(paste('Accuracy',1-misClasificError))

# decision tree part
install.packages("rpart")
library(rpart)

# control cut variable
Treecontro <- rpart.control(minsplit=20,minbucket=20,maxdepth=10,xval=5,cp=0.005)

# bulid model
rpart.mod=rpart(AHD ~.,data=trainning,method="class",
                 parms = list(prior = c(0.65,0.35), split = "gini"),
                 control=Treecontro)
summary(rpart.mod)

# view about imporatance
rpart.mod$variable.importance
# cp is the complexity factor corresponding to each segment
rpart.mod$cp

# plot the cp of the model
plotcp(rpart.mod)

# min xerror cp function to cut the tree
rpart.mod.pru<-prune(rpart.mod, cp= rpart.mod$cptable[which.min(rpart.mod$cptable[,"xerror"]),"CP"]) 
rpart.mod.pru$cp

library(rpart.plot)
# plot the tree after cut
rpart.plot(rpart.mod,branch=1, extra=106, under=TRUE, faclen=0,
           cex=0.8, main="decision tree")

# predict and summary
rpart.pred<-predict(rpart.mod.pru,test)
pre<-ifelse(rpart.pred[,2]>0.5,1,0)
summary(rpart.pred)

#random forest 

library(randomForest)
# confirm mtry values
for (i in 1:(14-1)){
    test_model <- randomForest(AHD~.,data=data,mtry=i)
    err <- mean(test_model$err)    
    print(err)
# mtry = 1

# confirm number of tree
tran_model <- randomForest(AHD~.,data=data,mtry=1,ntree=2000)
plot(tran_model)
# ntree = 1000

# build model
tran_model <- randomForest(AHD~.,data=data,mtry=1,ntree=1000)
tran_model

# see variables importance
tran_imp <- importance(x=tran_model)
varImpPlot(tran_model)
tran_imp
# most important variable is Ca

# predict and calculate
table(actual=test$AHD,predicted=predict(tran_model,newdata = test,type = "class"))
# print(Rate<- (48+36)/(48+36+5))