#网易云音乐批量下载
#Python 3.4.4

import requests
import urllib

#榜单歌曲批量下载
#r = requests.get('http://music.163.com/api/playlist/detail?id=2884035')
#网易原创歌曲榜
#r = requests.get('http://music.163.com/api/playlist/detail?id=19723756')
#云音乐飘升榜
#r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')
#云音乐热歌榜
r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')
#云音乐新歌榜

#r = requests.get('http://music.qq.com/api/playlist/detail?id=1913719')
#QQ音乐的尝试 失败




#歌单歌曲批量下载
#r = requests.get('http://music.163.com/api/playlist/detail?id=123415635')
#云音乐歌单——【华语】中国风的韵律，中国人的印记

arr = r.json()['result']['tracks']  #共有100首歌

for i in range(10):   #输入要下载音乐的数量，1到199
    name = str(i+1) + '' +arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url']
    urllib.request.urlretrieve(link,'网易云音乐\\' + name)  #提前要创建文件夹
    print(name + '下载完成')
    
