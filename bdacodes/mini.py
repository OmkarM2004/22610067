# Predicting Admission Chances using 3 Separate Models
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# ---- Sample dataset ----
data = {
    'GRE_Score': [320, 310, 305, 325, 330, 300, 290, 340, 315, 310],
    'GPA': [9.1, 8.5, 8.3, 9.5, 9.7, 8.0, 7.5, 9.9, 8.9, 8.7],
    'Research': [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    'Chance_of_Admit': [0.92, 0.75, 0.68, 0.95, 0.97, 0.72, 0.65, 0.99, 0.88, 0.79]
}
df = pd.DataFrame(data)

# ---- Split dataset ----
X = df[['GRE_Score', 'GPA', 'Research']]
y = df['Chance_of_Admit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# =====================================================
# 1️⃣ Linear Regression Model
# =====================================================
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
lin_pred = lin_model.predict(X_test)
lin_r2 = r2_score(y_test, lin_pred)
lin_mae = mean_absolute_error(y_test, lin_pred)

# =====================================================
# 2️⃣ Decision Tree Model
# =====================================================
tree_model = DecisionTreeRegressor(random_state=42)
tree_model.fit(X_train, y_train)
tree_pred = tree_model.predict(X_test)
tree_r2 = r2_score(y_test, tree_pred)
tree_mae = mean_absolute_error(y_test, tree_pred)

# =====================================================
# 3️⃣ Random Forest Model
# =====================================================
rf_model = RandomForestRegressor(n_estimators=50, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_r2 = r2_score(y_test, rf_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)

# =====================================================
# 📊 Combine Results into a Table
# =====================================================
results = pd.DataFrame({
    'Model': ['Linear Regression', 'Decision Tree', 'Random Forest'],
    'R2_Score': [round(lin_r2, 3), round(tree_r2, 3), round(rf_r2, 3)],
    'MAE': [round(lin_mae, 3), round(tree_mae, 3), round(rf_mae, 3)]
})

print("📊 Model Evaluation Results:")
print(results)
