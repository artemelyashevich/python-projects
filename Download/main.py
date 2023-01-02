import requests


def d_img(url, name):
    try:
        res = requests.get(url=url)
        with open(name, 'wb') as file:
            file.write(res.content)
        return "Success"

    except Exception as e:
        print(f"\t{e}")


def d_video(url, name):
    try:
        res = requests.get(url=url)
        with open(name, 'wb') as file:
            file.write(res.content)
        return "Success"

    except Exception as e:
        print(f"\t{e}")


def main():
    url_img = ''
    url_video = ''
    d_img(url_img, 'img.jpeg')
    d_video(url_video, 'video.mp4')


if __name__ == "__main__":
    main()
