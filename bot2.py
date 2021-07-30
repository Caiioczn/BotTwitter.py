import tweepy

stream = tweepy.Stream(
  "1vZvtCsM3NkLg1PDxlpsVl1XU", "nl5Admf9H6VvaZqPTKsXYlEhmaHqp0sPMya8MrFmsxCGGWjZh7",
  "1292552542736592897-uhkBRli8PITjbjN588HSfdWRiFg01i", "cJLFdERVoF7YtRvbllTNgaTtnH7QLjZmIXKKit8uW1YkE  "
)
thread = stream.filter(track=["Tweepy"], threaded=True)

class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)


printer = IDPrinter(
  "1vZvtCsM3NkLg1PDxlpsVl1XU", "nl5Admf9H6VvaZqPTKsXYlEhmaHqp0sPMya8MrFmsxCGGWjZh7",
  "1292552542736592897-uhkBRli8PITjbjN588HSfdWRiFg01i", "cJLFdERVoF7YtRvbllTNgaTtnH7QLjZmIXKKit8uW1YkE"
)
