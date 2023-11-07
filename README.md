# FSA029 XML Validator

The **FSA029 XML Validator** is a Python script that validates an FSA029 submission against the FSA029 schema. This script allows you to check whether your FSA029 XML submission conforms to the specified schema.

## Requirements

Before using this script, you need to have the following prerequisites:

1. **Python**: Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **lxml Library**: The script relies on the lxml library for XML parsing and validation. You can install it using pip:

   ```bash
   pip install lxml
   ```

## Usage

To validate an FSA029 submission using this script, you need to specify the paths to the schema file and the submission file. You can run the script as follows:

```bash
python fsa029_validator.py /path/to/FSA029-Schema.xsd /path/to/file/you/want/to/validate.xml
```

Replace `/path/to/FSA029-Schema.xsd` with the actual path to your FSA029 schema file and `/path/to/file/you/want/to/validate.xml` with the path to your FSA029 XML submission. Make sure the order of the arguments is correct, with the schema file path first, followed by the submission file path.

If the submission is valid, the script will display "Validation successful. The submission is valid." If there are any validation errors, the script will provide an error message.

## Further Info'

(a) **What causes it to fail schema validation?**
   'FSA029-Sample-Full.xml' may fail schema validation due to various reasons. Some common causes include incorrect data types, missing required elements, or elements in the wrong order. The regulator likely included this example to demonstrate the types of errors that can occur in submissions.

(b) **How would you fix the file to pass schema validation?**
   To fix 'FSA029-Sample-Full.xml,' you would need to review the schema requirements and ensure that the XML submission adheres to those requirements. This may involve correcting data types, providing missing elements, or reordering elements as specified in the schema.

(c) **Why do you think the regulator has included an invalid file in their examples?**
   Regulators often include invalid files in their examples to help institutions and individuals understand the schema's requirements better. By providing both valid and invalid examples, they can demonstrate the common mistakes that filers might make. This serves as a learning resource and helps filers avoid similar errors in their submissions.

---
