from main import emailProcess, printMsg


def main():
    emails = ['abc@gmail.com', 'xuan@gmail.com', 'hello@gmail.com', 'blabla@gmail.com']
    for email in emails:
        email_user, email_domain = emailProcess(email)
        printMsg(email_user, email_domain)


if __name__ == '__main__':
    main()
