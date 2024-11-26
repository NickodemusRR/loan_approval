# Test prediction of a data in the deployed app
import requests

url = "http://localhost:9696/predict"

customer_id = "abc-789"
customer = {
    "person_age": 21,
    "person_gender": "female",
    "person_education": "High School",
    "person_income": 12951.0,
    "person_emp_exp": 0,
    "person_home_ownership": "OWN",
    "loan_amnt": 2500.0,
    "loan_intent": "VENTURE",
    "loan_int_rate": 7.14,
    "loan_percent_income": 0.19,
    "cb_person_cred_hist_length": 2.0,
    "credit_score": 532,
    "previous_loan_defaults_on_file": "No",
}


response = requests.post(url, json=customer).json()
print(response)

if response["Loan_Approval"]:
    print("Approve the loan application of customer %s" % customer_id)
else:
    print("Reject the loan application of customer %s" % customer_id)
