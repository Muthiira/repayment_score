from score import getMeanScore
from score_inputs import score_inputs

mean_score, individual_results = getMeanScore(score_inputs)

print(f"Mean Score: {mean_score}")
print("Results:")
for i, result in enumerate(individual_results, start=1):
    print(f"Result {i}: {result}")
