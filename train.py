# Deployment
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier

# Parameters
n = 50
model_output_file = "model1.bin"
dv_output_file = "dv.bin"

# 1. Data preparation
df = pd.read_csv("./loan_data.csv", sep=",")
df["person_age"] = df["person_age"].astype("int")
df = df[df["person_age"] <= 80]

# 2. Dataset splitting
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)


# 3. Selecting features and target variable
categorical = [feat for feat in df.columns if df[feat].dtypes == "object"]
numerical = [
    feat
    for feat in df.drop(columns="loan_status").columns
    if df[feat].dtypes != "object"
]

y_full_train = df_full_train["loan_status"].values
y_test = df_test["loan_status"].values


# 4. Model Training
train_dicts = df_full_train[categorical + numerical].to_dict(orient="records")
dv = DictVectorizer(sparse=False)
X_full_train = dv.fit_transform(train_dicts)

# model training
print("Training the model")
model = RandomForestClassifier(n_estimators=50)
model.fit(X_full_train, df_full_train["loan_status"].values)

# model prediction
test_dicts = df_test[categorical + numerical].to_dict(orient="records")

X_test = dv.transform(test_dicts)
y_pred = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, y_pred)
print(f"AUC of the final model: {auc.round(3)}")


# 6. Save the model
with open(model_output_file, "wb") as f_out:
    pickle.dump(model, f_out)

with open(dv_output_file, "wb") as f_out:
    pickle.dump(dv, f_out)

print(f"The model is saved to {model_output_file}")
print(f"The vectorizer is saved to {dv_output_file}")
