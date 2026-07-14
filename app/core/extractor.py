def extract_information(extracted_text):

    info = {
        "name": "Not Found",
        "title": "Not Found",
        "organization": "Not Found",
        "date": "Not Found",
        "certificate_number": "Not Found",
        "grade": "Not Found",
        "duration": "Not Found"
    }

    lines = extracted_text.split("\n")

    for line in lines:

        line = line.strip()

        if line.startswith("Candidate Name:"):
            info["name"] = line.replace("Candidate Name:", "").strip()

        elif line.startswith("Certificate Title:"):
            info["title"] = line.replace("Certificate Title:", "").strip()

        elif line.startswith("Organization Name:"):
            info["organization"] = line.replace("Organization Name:", "").strip()

        elif line.startswith("Issue Date:"):
            info["date"] = line.replace("Issue Date:", "").strip()

        elif line.startswith("Certificate Number:"):
            info["certificate_number"] = line.replace("Certificate Number:", "").strip()

        elif line.startswith("Grade/Score:"):
            info["grade"] = line.replace("Grade/Score:", "").strip()

        elif line.startswith("Duration:"):
            info["duration"] = line.replace("Duration:", "").strip()

    return info