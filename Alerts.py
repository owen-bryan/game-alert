from win10toast import ToastNotifier

def sendAlert (game):
    toast = ToastNotifier()
    toast.show_toast("Game Released", "{0} released today".format (game.title))