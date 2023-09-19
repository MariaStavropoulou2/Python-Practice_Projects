def email_slicer(email):
    username = email[:email.index("@")]
    domain_name = email[email.index("@")+1:]
    format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
    print(format_)

email = input("Enter Your Email: ").strip()
email_slicer(email)