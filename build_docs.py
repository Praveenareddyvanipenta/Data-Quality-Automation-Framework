from great_expectations.data_context import get_context

context = get_context()
context.build_data_docs()

print("📂 Open your Data Docs at: great_expectations/uncommitted/data_docs/local_site/index.html")
