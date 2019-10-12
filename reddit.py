import praw
import creds as r


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

    def start_loop(self):
        while True:
            command = input(">")
            self.process_command(command)

    def process_command(self, cmd):
        cmd_parts = cmd.split(' ')
        if cmd_parts[0] == 'img':
            self.get_images(cmd)


if __name__ == '__main__':
    redd = REDDIT()
