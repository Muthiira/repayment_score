from repayment_score.score import getMeanScore
from repayment_score.score_inputs import score_inputs

mean_score, individual_results = getMeanScore(score_inputs)

print(f"Mean Score: {mean_score}")
print("Results:")
for i, result in enumerate(individual_results, start=1):
    print(f"Result {i}: {result}")
