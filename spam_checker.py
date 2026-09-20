# COP 2373 - Spam Email Checker
# This program checks an email message for common spam words and phrases.


def get_email():
    """Get an email message from the user."""

    print("Spam Email Checker")
    print("------------------")

    email = input("Enter an email message: ")

    return email


def check_spam(email):
    """Check the email for common spam words and phrases."""

    spam_words = [
        "free",
        "congratulations",
        "winner",
        "won",
        "prize",
        "cash",
        "money",
        "earn money",
        "make money",
        "guaranteed",
        "risk-free",
        "limited time",
        "act now",
        "click here",
        "buy now",
        "special offer",
        "exclusive offer",
        "free gift",
        "claim now",
        "you have been selected",
        "urgent",
        "important",
        "lottery",
        "casino",
        "million dollars",
        "no obligation",
        "miracle",
        "100% free",
        "work from home",
        "congratulations you won"
    ]

    # Convert the email to lowercase for case-insensitive checking.
    email_lower = email.lower()

    score = 0
    found_words = []

    # Check each spam word or phrase in the email.
    for word in spam_words:
        count = email_lower.count(word)

        if count > 0:
            score += count

            for _ in range(count):
                found_words.append(word)

    return score, found_words


def rate_spam(score):
    """Determine the likelihood that the email is spam."""

    if score <= 2:
        return "Unlikely to be spam"
    elif score <= 5:
        return "Possibly spam"
    elif score <= 9:
        return "Likely spam"
    else:
        return "Highly likely to be spam"


def display_results(score, likelihood, found_words):
    """Display the spam score, likelihood, and words found."""

    print()
    print("Spam Check Results")
    print("------------------")
    print("Spam score:", score)
    print("Likelihood:", likelihood)

    print()
    print("Words/phrases that caused the spam score:")

    if len(found_words) == 0:
        print("None")
    else:
        for word in found_words:
            print("-", word)


def main():
    """Run the spam email checker program."""

    # Get the email message from the user.
    email = get_email()

    # Check the message for spam words and calculate the score.
    score, found_words = check_spam(email)

    # Determine the likelihood that the message is spam.
    likelihood = rate_spam(score)

    # Display the results.
    display_results(score, likelihood, found_words)


# Start the program.
main()
