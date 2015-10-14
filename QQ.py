import urllib as ur

'''this is the address of the tencent QQ add = "https://w.qq.com";'''
conn= ur.urlopen("https://w.qq.com")

data = conn.read()

print  data
