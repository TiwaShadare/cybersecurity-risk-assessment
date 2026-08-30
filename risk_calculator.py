import csv


def calculate_risk(likelihood, impact):
    """Calculate risk score."""
    return likelihood * impact


def classify_risk(score):
    """Classify risk based on risk score."""

    if score >= 20:
        return "Critical"

    elif score >= 12:
        return "High"

    elif score >= 6:
        return "Medium"

    else:
        return "Low"


def analyze_risks():

    risks = []

    with open("risk_assessment.csv", "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            likelihood = int(row["Likelihood"])
            impact = int(row["Impact"])

            score = calculate_risk(
                likelihood,
                impact
            )

            level = classify_risk(score)

            risk = {
                "id": row["Risk_ID"],
                "asset": row["Asset"],
                "threat": row["Threat"],
                "score": score,
                "level": level
            }

            risks.append(risk)

    return risks


def display_report(risks):

    print("\nCYBERSECURITY RISK REPORT")
    print("-" * 60)

    for risk in risks:

        print(
            f"{risk['id']} | "
            f"{risk['asset']} | "
            f"{risk['threat']} | "
            f"Score: {risk['score']} | "
            f"{risk['level']}"
        )


    print("\nHIGH-PRIORITY RISKS")
    print("-" * 60)

    for risk in risks:

        if risk["level"] in [
            "Critical",
            "High"
        ]:

            print(
                f"{risk['asset']}: "
                f"{risk['threat']} "
                f"({risk['level']})"
            )


risks = analyze_risks()

display_report(risks)
