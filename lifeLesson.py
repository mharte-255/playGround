def belief(question: str) -> bool:

    secret = "You"
    author = " - Henry Ford"

    reply = None
    while reply not in ("", "y", "n"):
        reply = input(f"{question} (Y/N): ").lower()

    return secret + "'re right!" + "\n" + "\"Whether " + secret.lower() + " think " + secret.lower() + " can, or " + secret.lower() + " think " + secret.lower() + " can't - " + secret.lower() + "'re right.\"" + "\n" + author

reply = belief("Can you do this?")
print(reply)






