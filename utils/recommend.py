def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        recommendations.append(
            f"Improve or learn {skill}"
        )

    return recommendations