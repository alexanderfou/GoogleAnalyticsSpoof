# google analytics pageview spoofer
import requests
import urllib.parse
from time import sleep
import random
import uuid
import os


def gaspoof():
    try:
        #dir_path = os.path.dirname(os.path.realpath(__file__))
        #dir_path = dir_path.replace("tempcoderunner.py", "")
        #dir_path = dir_path + "/geoids.txt"
        # requests.get("https://google-analytics.com/analytics.js")
        #file = open(dir_path, "r", encoding="utf-8")
        #lines = file.readlines()
        count = 0
        referrers = ["https://www.google.com",
                     "https://www.twitter.com", "https://www.facebook.com", "https://www.instagram.com"]  # just example referrers

        # resolutions are to mix up screen resolution sizes, the following picks a random resolution from the 24 choices
        class resolution:
            def __init__(self, width, height):
                self.width = width
                self.height = height

        r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24 = resolution(1900, 1060), resolution(940, 700), resolution(
            1260, 780), resolution(1004, 556), resolution(2540, 1580), resolution(700, 1260), resolution(730, 1314), resolution(820, 1770), resolution(1020, 580), resolution(1900, 1420), resolution(480, 800), resolution(640, 1136), resolution(720, 1280), resolution(750, 1334), resolution(1080, 1920), resolution(1440, 2560), resolution(1125, 2436), resolution(480, 800), resolution(480, 754), resolution(1024, 600), resolution(768, 1280), resolution(1200, 1290), resolution(2560, 1600), resolution(800, 1280)

        resolutions = [r1, r2, r3, r4, r5, r6, r7,
                       r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24]

        # sample user agemts
        useragents = [
            "Opera%2F9.80%20%28Windows%20NT%206.0%29%20Presto%2F2.12.388%20Version%2F12.14", "Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36", "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3", "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:17.0) Gecko/17.0 Firefox/17.0", "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19", "Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30", "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36", "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0", "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36", "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977", "Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP", "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4", "Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0", "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727)", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063", "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 YaBrowser/18.3.1.1232 Yowser/2.5 Safari/537.36"]
        tracking_id = "UA-XXXXXXX-Y"  # find your own tid or the tid of the page you are hitting. Open the console and check for requests for google-analytics.com/collect. This will have the tid
        # name of page
        dl = "subdirectory"  # example.com/example123 would show up as "example123"
        ul = "en-us"  # user language (en-us is an example)
        dt = "example document title"  # document title
        # you can add more fake languages here, can be a string
        languages = ["english"]
        while True:
            dl = urllib.parse.quote_plus(dl)
            dt = random.choice(languages)
            # geoid = random.choice(lines) (un-comment this line to pick random geo-ids)
            geoid = "US"
            # screen resolutions
            choice = random.choice(resolutions)
            width, height = choice.width, choice.height
            screen_resolution = (f"{width}x{height}")
            srt = 500  # server response time
            v = 1  # protocol version
            _v = "j83"  # couldn't find anything on this
            aip = 1  # anonymize ip
            a = random.randint(100000000, 999999999)  # not sure what this is
            t = "pageview"  # type of hit
            de = "UTF-8"  # encoding type
            dr = urllib.parse.quote_plus(
                random.choice(referrers))  # document referrer
            sd = "24-bits"  # screen colors
            ul = random.choice(languages)  # user language
            ua = urllib.parse.quote_plus(
                random.choice(useragents))  # user agent
            vpwidth, vpheight = width-100, height-100
            vp = f"{vpwidth}x{vpheight}"  # viewable area of browser/device
            je = 0  # is javascript enabled
            _u = "AACAAUAB~"  # not sure
            cid = random.randint(0, 750000)  # client id
            gtm = "2ou6h1"  # not sure but stays the same
            # z = 1998421146  # not sure
            url = f"https://www.google-analytics.com/collect?v={v}&srt={srt}&ua={ua}&cid={cid}&de={de}&dt={dt}&ul={ul}&aip={aip}&_v={_v}&a={a}&dr={dr}&t={t}&dl={dl}&sd={sd}&sr={screen_resolution}&vp={vp}&je={je}&_u={_u}&jid=&gjid=&tid={tracking_id}&gtm={gtm}&geoid={geoid}"

            requests.get(url)
            count += 1
            print(f"Sent {count} times")
    except:
        print("There was an error!")
        sleep(5)
        gaspoof()


gaspoof()
