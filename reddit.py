import praw
import creds as r
import requests
import os

class REDDIT():
    """
    """
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=r.client_id,
            client_secret=r.client_secret,
            username=r.username,
            password=r.password,
            user_agent=r.user_agent
        )
        self.visited_posts = []

    def __load_visited__(self):
        v = []
        with open('visited.txt') as f:
            v = f.readlines()
        for line in v:
            self.visited_posts.append(line.strip())

    def __add_visited__(self, post_url):
        self.visited_posts.append(post_url)
        v = open('visited.txt', 'a')
        v.write(post_url + '\n')
        v.close()

    def start_loop(self):
        while True:
            command = input(">")
            self.process_command(command)

    def process_command(self, cmd):
        cmd_parts = cmd.split(' ')
        if cmd_parts[0] == 'img':
            self.get_images(cmd)

    def get_images(self, sub, number=1):
        retArray = []
        for submission in self.reddit.subreddit(sub).hot(limit=number):
            retArray.append(submission.url)
        return retArray

    def download_images(self, sub, number=1):
        urls = self.get_images(sub, number)
        extension = '0'
        image_files = []
        for url in urls:
            if url not in self.visited_posts:
                # Filter image file types
                if '.png' in url:
                    extension = '.png'
                elif '.jpg' in url or '.jpeg' in url:
                    extension = '.jpeg'
                elif 'imgur' in url:
                    url += 'jpeg'
                    extension = '.jpeg'
                else:
                    print("No image found on this url")

                if extension != '0':
                    image = requests.get(url, allow_redirects=False)
                    file_name = url[url.rfind('/') + 1:] + extension

                    if image.status_code == 200:
                        with open(file_name, mode='wb') as meme_file:
                            meme_file.write(image.content)
                            self.__add_visited__(url)
                        print(f"Images found and saved as {file_name} [{len(image_files)}]")
                        image_files.append(file_name)

                extension = '0'

        self.image_keep(image_files)

    def image_keep(self, image_files):
        x = 0
        for image in image_files:
            number = input('Keep file [' + str(x) + '](y/n)?')
            if number == 'n':
                os.remove(image)
            x += 1


if __name__ == '__main__':
    redd = REDDIT()
    redd.download_images('programmerhumor', 10)
