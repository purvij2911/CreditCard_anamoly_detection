# # RandomForest on balanced data with ADASYN

# In[178]:


# Create the parameter grid 
param_grid = {
    'max_depth': range(5, 15, 5),
    'min_samples_leaf': range(50, 150, 50),
    'min_samples_split': range(50, 150, 50),
}


# Instantiate the grid search model
model = RandomForestClassifier()

grid_search = GridSearchCV(estimator = model, 
                           param_grid = param_grid, 
                           scoring= 'roc_auc',
                           cv = 5, 
                           n_jobs=-1,
                           verbose = 1)

# Fit the grid search to the data
grid_search.fit(X_train_adasyn,y_train_adasyn)


# In[179]:


# Printing the optimal roc score and hyperparameters
print("Best roc auc score : ", grid_search.best_score_)


# In[180]:


print(grid_search.best_estimator_)


# #### Model with optimal hyperparameters

# In[181]:


# Model with optimal hyperparameters
rf_adasyn_model =grid_search.best_estimator_
rf_adasyn_model.fit(X_train_adasyn, y_train_adasyn)


# #### Evaluating the model on train data

# In[182]:


# Evaluating model on the test data
y_train_pred = rf_adasyn_model.predict(X_train_adasyn)
display_scores(y_train_adasyn, y_train_pred)


# In[183]:


# Predicted probability
y_train_pred_proba = rf_adasyn_model.predict_proba(X_train_adasyn)[:,1]
# Plot the ROC curve
draw_roc(y_train_adasyn, y_train_pred_proba)


# #### Evaluating the model on the test set

# In[184]:


# Evaluating model on the test data
y_pred = rf_adasyn_model.predict(X_test)
display_scores(y_test, y_pred)


# In[185]:


# Predicted probability
y_test_pred_proba = rf_adasyn_model.predict_proba(X_test)[:,1]
# Plot the ROC curve
draw_roc(y_test, y_test_pred_proba)


# #### Model Summary
# - Train set
#     - ROC score : 100%
#     - F1 score: 99.96%
#     
# - Test set
#     - ROC score : 98%
#     - F1 score: 20.63%