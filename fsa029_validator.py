from lxml import etree
from pathlib import Path

def validate_submission(schema_path, submission_path):
    # Determine the directory of the script
    script_dir = Path(__file__).resolve().parent

    # Construct relative paths
    schema_path = script_dir / schema_path
    submission_path = script_dir / submission_path

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

if __name__ == "__main__":
    schema_path = "CommonTypes-Schema.xsd"  # Updated to relative path
    submission_path = "FSA029-Sample-Full.xml"  # Updated to relative path

    validate_submission(schema_path, submission_path)
