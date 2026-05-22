def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{0:02d}"
