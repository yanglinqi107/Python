#1.找到未加密的参数
#2.想办法把参数进行加密，params,encSecKey
#3.请求到网易，拿到评论信息
from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests


proxies = {
    "https":"117.157.197.18:3128"   #"https":"https://117.157.197.18:3128"
}
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式是post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1387581250",
    "threadId": "R_SO_4_1387581250"
}
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
e = "010001"
i = "7k2f27HBDb3IhCYI"
g = "0CoJUm6Qyw8W8jud"

def get_encSecKey():
    return "6f04d55d3b596b1a076c0c742858e22c8c0ea7274b373978ce2ca9bbdd1790fd13060e3ed5e35c569859f381c952f70d722e0ac47a6a4365ee4731c424c9354631827bfaadef85015bea6b89158327d5b9733bc4ce43eb44eb9c65732f393d54b838a8c8cfdaea08a27b51183d3b9c9ac41efa0e510e8c0d6be99d94582dbf04"

def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key = key.encode('utf-8'), IV = iv.encode('utf-8'), mode = AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs), 'utf-8')

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

resp = requests.post(url = url, proxies = proxies, data = {
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})
resp.close()
print(resp.text)

"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {       
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
"""
# d:数据data
# e:010001    
# f:00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
# g:0CoJUm6Qyw8W8jud
