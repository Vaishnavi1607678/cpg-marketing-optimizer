from app.data_loader import load_data


def optimize():
    df = load_data()

    recommendations = []

    for _, row in df.iterrows():

        roi = row["Sales"] / row["Spend"]

        if roi >= 2.5:
            recommendation = row["Spend"] * 1.10
            action = "Increase Budget"

        elif roi >= 2.0:
            recommendation = row["Spend"]
            action = "Keep Same"

        else:
            recommendation = row["Spend"] * 0.90
            action = "Reduce Budget"

        recommendations.append(
            {
                "channel": row["Channel"],
                "product": row["Product"],
                "current_spend": round(row["Spend"], 2),
                "sales": round(row["Sales"], 2),
                "roi": round(roi, 2),
                "recommended_spend": round(recommendation, 2),
                "action": action,
            }
        )

    return recommendations