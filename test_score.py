from score import getScore
from score_types import ScoreInput, Payment, ScoreError, Score

sample_input: ScoreInput = {
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

result: Score = getScore(sample_input)

print("Result:", result)

