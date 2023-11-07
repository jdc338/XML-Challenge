import argparse
from lxml import etree

def validate_submission(schema_path, submission_path):
    # Create an XML schema parser with the schema
    schema = etree.XMLSchema(etree.parse(schema_path))

    # Create an XML parser for the submission
    parser = etree.XMLParser(schema=schema)

    try:
        # Parse the submission
        etree.parse(submission_path, parser)
        print("Validation successful. The submission is valid.")
    except Exception as e:
        print(f"Validation failed. The submission is not valid.\nError: {e}")

def main():
    parser = argparse.ArgumentParser(description="Validate an XML submission against a schema.")
    parser.add_argument("schema_path", help="Path to the schema file")
    parser.add_argument("submission_path", help="Path to the XML submission file")

    args = parser.parse_args()
    validate_submission(args.schema_path, args.submission_path)

if __name__ == "__main__":
    main()
