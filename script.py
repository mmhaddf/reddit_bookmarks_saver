import praw
import datetime

reddit = praw.Reddit(  #write your information
    client_id="",
    client_secret="",
    user_agent="script:bookmark_exporter:v1.0 (by /u/)",
    username="",
    password=""
)

bookmarks = list(reddit.user.me().saved(limit = None))
lines = []

def get_date(submission): #the date of the bookmark creation
	time = submission.created
	return datetime.datetime.fromtimestamp(time)

for idx, bookmark in enumerate(bookmarks, 1):
    if isinstance(bookmark, praw.models.Submission):
        title = bookmark.title
        url = bookmark.url
        date = get_date(bookmark)
    elif isinstance(bookmark, praw.models.Comment):
        title = f'Comment in {bookmark.submission.title}'
        url = f"https://www.reddit.com{bookmark.permalink}"
        date = get_date(bookmark)
    else:
        continue


    line = f'{idx}. [{title}]({url})[{date}]'
    lines.append(line)

with open('my_reddit_bookmarks.md', 'w',  encoding='utf8') as f: 
    f.write('# Reddit bookmarks \n\n')
    f.write('\n'.join(lines))


print('Your bookmarks have been successfully uploaded to my_reddit_bookmarks.md')

