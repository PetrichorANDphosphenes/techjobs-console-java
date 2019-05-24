class Post:

    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0


    def like(self):
        self.likes +=1



    def __str__(self):
        return self.title + self.author + self.body + str(self.likes)





        
class VideoPost(Post):
    def __init__(self, title, author, url):
        post.__init__(title, author, "")  # without this line, the videoPost would run without all values initialized from post
        self.url = url
        plays = 0

    def play(self):
        plays += 1

    def __self__(self):
        return Post.__init__ + self.title + "played" + self.plays + "number of times"


def main():
    plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
    vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")

    vid_post.play()
    vid_post.play()

    print(vid_post)
    print(plain_post)




if __name__ == "__main__":
    main()