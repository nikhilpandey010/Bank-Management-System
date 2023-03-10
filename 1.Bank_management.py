while True:
    print("====Enter====")
    print("    1.   User")
    print("    2.  Admin")
    print("    3.   Exit")
    ch=int(input(" : "))
    if ch==1:
        import User
        User.User()
    elif ch==2:
        import Admin
        Admin.admin()
    elif ch==3:
        exit(0)
    else:
        print("Invalid Entry!!!...")
