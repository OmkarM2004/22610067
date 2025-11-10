import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Step 1: Load Dataset (use full path)
file_path = r"C:\Users\omman\Desktop\my_genai_code\US_graduate_schools_admission_parameters_dataset.csv"
data = pd.read_csv(file_path)

# Rename column if needed (some versions have a space at the end)
if 'Chance of Admit ' in data.columns:
    data = data.rename(columns={'Chance of Admit ': 'Chance_of_Admit'})
elif 'Chance of Admit' in data.columns:
    data = data.rename(columns={'Chance of Admit': 'Chance_of_Admit'})

# Step 2: Feature and Target
X = data.drop('Chance_of_Admit', axis=1)
y = data['Chance_of_Admit']

# Step 3: Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Scale Data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 5: Train Models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

# Step 6: Evaluate Models
print("\n📊 Model Performance Comparison:\n")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{name}: R2 = {r2_score(y_test, y_pred):.3f}, MSE = {mean_squared_error(y_test, y_pred):.3f}")

print("\n✅ Done! Models trained and evaluated successfully.")
