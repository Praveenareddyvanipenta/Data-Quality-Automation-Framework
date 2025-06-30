from great_expectations.data_context import get_context
import sys, json

context = get_context()
result = context.run_checkpoint(checkpoint_name="my_expectations")

stats = result["run_results"][list(result["run_results"])[0]]["validation_result"]["statistics"]
print(json.dumps(stats, indent=2))

if not result["success"]:
    sys.exit(1)
