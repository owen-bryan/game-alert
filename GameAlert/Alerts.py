from win10toast import ToastNotifier

def sendAlertOne (game):
    toast = ToastNotifier()
    toast.show_toast("Game Released", "{0} released today".format (game))

def sendAlerts (games, platform):
    toast = ToastNotifier ()

    output = "Games released today for {0} :\n".format(platform)
    for game in games :
        output += "{0}\n".format (game['title'])
    

    toast.show_toast ("Game Alert", output, icon_path=None, duration=10)
