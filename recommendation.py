
# AI Recommendation Logic
# Project 3 - DecodeLabs

# Items and their categories
items = {
    "Avengers": ["action", "sci-fi"],
    "Interstellar": ["sci-fi", "adventure"],
    "John Wick": ["action", "thriller"],
    "The Dark Knight": ["action", "crime"],
    "Titanic": ["romance", "drama"],
    "The Notebook": ["romance", "drama"]
}


def get_user_preferences():
    """Get preferences from the user."""
    while True:
        user_input = input(
            "\nEnter your interests separated by commas: "
        ).strip()

        if user_input:
            preferences = [
                preference.strip().lower()
                for preference in user_input.split(",")
                if preference.strip()
            ]

            if preferences:
                return preferences

        print("Please enter at least one interest.")


def calculate_score(preferences, categories):
    """Calculate the number of matching preferences."""
    score = 0

    for preference in preferences:
        if preference in categories:
            score += 1

    return score


def get_recommendations(preferences):
    """Find and sort recommended items."""
    recommendations = []

    for item, categories in items.items():
        score = calculate_score(preferences, categories)

        if score > 0:
            recommendations.append((item, score))

    # Highest score first
    recommendations.sort(key=lambda recommendation: recommendation[1],
                         reverse=True)

    return recommendations


def display_recommendations(recommendations):
    """Display the recommendations."""
    print("\n-----------------------------------")
    print("       RECOMMENDED ITEMS")
    print("-----------------------------------")

    if not recommendations:
        print("No matching recommendations found.")
        print("Try interests such as:")
        print("action, sci-fi, adventure, romance, drama")
        return

    for item, score in recommendations:
        print(f"{item} - Match Score: {score}")


def main():
    print("===================================")
    print("     AI RECOMMENDATION SYSTEM")
    print("===================================")
    print("This system recommends items based")
    print("on your interests.")

    preferences = get_user_preferences()

    print("\nYour interests:")
    for preference in preferences:
        print(f"- {preference}")

    recommendations = get_recommendations(preferences)

    display_recommendations(recommendations)

    print("\nThank you for using the AI Recommendation System!")


if __name__ == "__main__":
    main()

