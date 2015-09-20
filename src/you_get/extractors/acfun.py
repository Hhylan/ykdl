#!/usr/bin/env python

from ..common import *
from ..embedextractor import EmbedExtractor

import json

class Acfun(EmbedExtractor):

    def prepare(self, **kwargs):
        assert self.url
        assert re.match(r'http://[^\.]+.acfun.[^\.]+/\D/\D\D(\d+)', self.url)

        html = get_content(self.url)

        self.title = match1(html, '<h1 id="txt-title-view">([^<>]+)<')
        videos = matchall(html,["data-vid=\"(\d+)\""])

        for video in videos:
            info = json.loads(get_html('http://www.acfun.tv/video/getVideo.aspx?id=' + video))
            sourceType = info['sourceType']
            sourceId = info['sourceId']
            if sourceType == 'letv':
                #workaround for letv, because it is letvcloud
                sourceType = 'letvcloud'
                sourceId = (sourceId, '2d8c027396')

            self.video_info.append((sourceType, sourceId))

site = Acfun()
download = site.download
download_playlist = playlist_not_supported('acfun')
