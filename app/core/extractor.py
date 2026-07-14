def extract_information(extracted_text):

    extracted_data = {
        "name": "Not Found",
        "title": "Not Found",
        "organization": "Not Found",
        "date": "Not Found",
        "certificate_number": "Not Found",
        "grade": "Not Found",
        "duration": "Not Found"
    }

    for line in extracted_text.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("Candidate Name:"):
            extracted_data["name"] = line.replace("Candidate Name:", "").strip()

        elif line.startswith("Certificate Title:"):
            extracted_data["title"] = line.replace("Certificate Title:", "").strip()

        elif line.startswith("Organization Name:"):
            extracted_data["organization"] = line.replace("Organization Name:", "").strip()

        elif line.startswith("Issue Date:"):
            extracted_data["date"] = line.replace("Issue Date:", "").strip()

        elif line.startswith("Certificate Number:"):
            extracted_data["certificate_number"] = line.replace("Certificate Number:", "").strip()

        elif line.startswith("Grade/Score:"):
            extracted_data["grade"] = line.replace("Grade/Score:", "").strip()

        elif line.startswith("Duration:"):
            extracted_data["duration"] = line.replace("Duration:", "").strip()

    return extracted_data