# -*- coding:utf-8 -*-
__author__ = 'zqf'

cookies = {

}


cookies_str = 'is-delta-value-used=1; bill_search_slide_search=0; current-delta-value=; cna=ebmREhfjm3MCAXPXKQtHMPfG; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=5838951351336776563; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; _tb_token_=efeb6db34914b; uc1=cookie14=UoTdf1JN9JUzww%3D%3D&lng=zh_CN&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=V32FPkk%2FhSt4&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; uc3=sg2=UIMd39YMh8FovAaghIqo8l3%2Bs07gWz%2BX9MHQF9BhWmA%3D&nk2=rpdqh0qBWs0%3D&id2=UNQ3F6fN1mgNPg%3D%3D&vt3=F8dBzLba501Ypt%2BaHuI%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTUxNDM3NTE1Ng%3D%3D; uss=WvBlHq10DWOfKzHTcqYUcK0MOPPnwUeo3Gf2R%2B5cE4adNoduY4fW5U0%3D; lgc=%5Cu4E07%5Cu6613%5Cu901A%5Cu8FBE; tracknick=%5Cu4E07%5Cu6613%5Cu901A%5Cu8FBE; cookie2=377bb5fa51d32311ca4915cacbcc6536; sg=%E8%BE%BE32; mt=np=&ci=14_1; cookie1=UU6p81Ce1JbCIYPr2k%2BzCw9rleQQWfV9yNqWPoVUX%2Bs%3D; unb=3408892653; skt=21a4463206a9bf2d; t=3cbaf3eff99f04fd8a922134660c9e84; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=%5Cu4E07%5Cu6613%5Cu901A%5Cu8FBE; cookie17=UNQ3F6fN1mgNPg%3D%3D; l=Anh4klPGM43osa9e5gCuYJFOyCwIKtxr; JSESSIONID=73CB009E242E4CADFD1CF77293EFB13A; isg=AtPTBmZGjbmHJ0EkoAUQNJOEYlc9IHcvbh0vp4XxOPIqBPmmCl7hml0WSkOQ'

key_values = cookies_str.split('; ')
for key_value in key_values:
    key, value = key_value.split('=', maxsplit=1)
    cookies[key] = value
