def emailProcess(email):
    email_user = email[0:email.index("@")]
    email_domain = email[email.index("@") + 1:]

    return [email_user, email_domain]
    # print(f"User name is {email_user}")


def main():
    email = input("Please enter email address: ").strip()
    email_user, email_domain = emailProcess(email)
    printMsg(email_user, email_domain)
    # print(f"Hello {email}")


def printMsg(email_user, email_domain):
    print(f"Username is {email_user}; Email domain: {email_domain}")


if __name__ == '__main__':
    main()
