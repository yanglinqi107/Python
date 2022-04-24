# import string
# lowers = string.ascii_lowercase #lowers是全部的小写英文字母
# uppers = string.ascii_uppercase #uppers是全部的大写英文字母
# digits = string.digits #digits是全部的数字字符
# table = ''.maketrans('opqrstuvwxyz' ,'rstuvwxyzabc') # 建立'o' -> 'r', 'p' ->  's' ..的映射关系，存储在table里
# place = 'zoo'.translate(table)      #使用table里的映射关系对'zoo'加密，得到密文'crr'
# print(place)  # crr

import string


def caesar_cipher(text, offset=3):
    """接收明文字符串为参数，返回用凯撒密码加密后的字符串。"""
    lowbefore = string.ascii_lowercase
    lowafter = lowbefore[offset:] + lowbefore[:offset]
    upbefore = string.ascii_uppercase
    upafter = upbefore[offset:] + upbefore[:offset]
    digitsbefore = string.digits
    digitsafter = digitsbefore[offset:] + digitsbefore[:offset]
    trans_table = str.maketrans(lowbefore + upbefore + digitsbefore,
                                lowafter + upafter + digitsafter,
                                ',!')  # 创建转换表
    message = text.translate(trans_table)  # 根据转换表转换
    return message


if __name__ == '__main__':
    plaintext = input()  # 输入一个字符串
    ciphertext = caesar_cipher(plaintext)  # 调用函数
    print(ciphertext)  # 输出密文
