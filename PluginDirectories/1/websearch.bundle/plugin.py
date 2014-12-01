import urllib, json
import i18n

def results(parsed, original_query):

    search_specs = [
         ["Google", "~googlequery", "https://www.google.de/search?q="],
         ["Google", "~googlequeryde", "https://www.google.de/search?q="],
         ["Duck Duck Go", "~duckduckgoquery", "https://duckduckgo.com/?q="],
         ["Google Images", "~googleimagequery", "https://www.google.de/search?tbm=isch&q="],
         ["Google Images", "~googleimagequeryde", "https://www.google.de/search?tbm=isch&q="],
         ["Baidu", "~baiduquery", "http://www.baidu.com/s?wd="],
         ["Bing", "~bingquery", "http://www.bing.com/search?q="],
         ["Yahoo", "~yahooquery", "https://sg.search.yahoo.com/search?p="],
         ["Twitter", "~twitterquery", "https://mobile.twitter.com/search?q="],
         ["Reddit", "~redditquery", "https://www.reddit.com/search?q="],
         ["Google Maps", "~googlemapsquery", "https://www.google.de/maps/place/"],
         ["Google Maps", "~googlemapsqueryde", "https://www.google.de/maps/place/"],
         ["Github", "~githubquery", "https://github.com/search?q="]
    ]
    for name, key, url in search_specs:
        if key in parsed:
            localizedurl = i18n.localstr(url)
            search_url = localizedurl + urllib.quote_plus(parsed[key])
            title = i18n.localstr("Search {0} for '{1}'").format(name, parsed[key]);
            return {
                "title": title,
                "run_args": [search_url],
                "html": """
                <script>
                setTimeout(function() {
                    window.location = %s
                }, 500);
                </script>
                """%(json.dumps(search_url)),
                "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
                "webview_links_open_in_browser": True
            }

def run(url):
    import os
    os.system('open "{0}"'.format(url))
