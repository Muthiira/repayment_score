from score import ScoreInput

# Define a list of ScoreInput objects
input1: ScoreInput = {
    "paymentStartDate": "2023-01-01T00:00:00Z",
    "paymentEndDate": "2023-12-31T00:00:00Z",
    "expectedPaymentDay": 5,
    "expectedPaymentAmount": 1000,
    "payments": [
        {"date": "2023-01-05T12:00:00Z", "amount": 1000},
        {"date": "2023-02-05T11:30:00Z", "amount": 1000},
    ],
    "reference": "Your Reference Here",
    "scoreBeforeStartDate": False,
}

input2: ScoreInput = {
    "paymentStartDate": "2023-01-01T00:00:00Z",
    "paymentEndDate": "2023-12-31T00:00:00Z",
    "expectedPaymentDay": 3,
    "expectedPaymentAmount": 5000,
    "payments": [
        {"date": "2023-01-05T12:00:00Z", "amount": 5000},
        {"date": "2023-05-05T11:30:00Z", "amount": 5000},
    ],
    "reference": "Your Reference Here",
    "scoreBeforeStartDate": True,
}

# Define a list to store the ScoreInput objects
score_inputs = [input1, input2]
