
'''
#txt, sys, prg

txt:
  latinex (拉丁字母擴充)
  squiggle:
    rnd (內空圓形)
    sqr (方形)
    crsv (草寫)
    crsvb (草寫粗體)
    wrt (書寫)
    gthc (歌德)
    gthcb (歌德粗體)
    bld (粗體)
    itlc (斜體)
    itlcb (斜體粗體)
    fsp (全形)
sys:
  prmpbox(提示框)
  ddos
prg:
  

'''
import re
import tkinter as tk
from tkinter import messagebox

text = "./txt_squiggle.fsp/efwvrebtgds"
text = "./txt_latinex.cewclkns^e#E$e12hik?"
text = "./sys_prmpbox.10/警告/你是智障"
returnt = ""

template = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
pattern1 = r'\./(.*?)_(.*?)\.(.*)'
pattern2 = r'(.*?)/(.*?)$'

matches = re.search(pattern1, text)

#資料庫：
template1 = "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"
template3 = "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"
template4 = "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
template5 = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"
template6 = "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
template7 = "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"
template8 = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
template9 = "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳"
template10 = "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"
template11 = "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"
template12 = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
char_mapping = {
    "A`": "À", "A%": "Á", "A^": "Â", "A:": "Ä", "AE;": "Æ", "A~": "Ã", "AO;": "Å", "A-": "Ā", "A,": "Ą", "Ç": "C,", "Ć": "C%", "Č": "C$", "Ď": "D$",
    "É": "E%", "Ê": "E^", "Ë": "E:", "È": "E`", "Ě": "E$", "Ė": "E.", "Ē": "E-", "Ę": "E,", "Ģ": "G,", "Ğ": "G$",
    "Í": "I%", "Ì": "I`", "Ī": "I-", "Į": "I,", "Î": "I^", "I": "I;", "Ï": "I:", "ĳ": "IJ;", "Ķ": "K,", "Ļ": "L,", "Ł": "L-", "Ĺ": "L%", "Ľ": "L'",
    "Ñ": "N~", "Ņ": "N,", "Ń": "N%", "Ó": "O%", "Ô": "O^", "Ö": "O:", "Ò": "O`",  "Œ": "OE;", "Ø": "O/",  "Ō": "O-", "Õ": "O~", "Ő": "O#", "Ŗ": "R,", "Ŕ": "R%", "Ř": "R$", "ẞ": "SS;", "Ś": "S%", "Š": "S$", "Ş": "S,",
    "Ţ": "T,", "Ť": "T$", "Ú": "U%", "Ü": "U:", "Û": "U^", "Ù": "U`", "Ű": "U#", "Ų": "U,", "Ū": "U-", "Ů": "UO;", "Ŭ": "U$",
    "Ý": "Y%", "Ÿ": "Y:", "Ž": "Z$", "Ż": "Z.", "Ź": "Z%", "A̍": "A'", "Ǎ": "A$", "A̋": "A#", "E̋": "E#", "E̍": "E'", "I̍": "I'", "Ǐ": "I$", "I̋": "I#",  "O̍": "O'", "Ǒ": "O$", "Ū": "U-", "Ǔ": "U$", "Ḿ": "M%", "M̂": "M^", "M̀": "M`", "M̄": "M-", "M̍": "M'", "N̂": "N^", 
    "Ń": "N%", "Ǹ": "N`", "N̄": "N-", "N̍": "N'", "ⁿ": "n+", "O͘": "O.;", "Ô͘": "O^;", "Ó͘": "O%;", "Ò͘": "O`;", "Ō͘": "O-;", "Ŝ": "S^", "Ĝ": "G^", "Ĵ": "J^", "Ĉ": "C^", "Ŵ": "W^", "º": "o+", "ŉ": "n';", "Ŋ": "NG;", "Ċ": "C.", 
    "Đ": "D-;","đ": "d-;","Ð": "D-","ð": "d-", "Þ": "TH;", "þ": "th;", "Ĥ": "H^", "ĥ": "h^", "ħ": "h-", "Ħ": "H-",  "a`": "à", "a%": "á", "a^": "â", "a:": "ä", "ae;": "æ", "a~": "ã", "ao;": "å", "a-": "ā", "a,": "ą",
    "ç": "c,", "ć": "c%", "č": "c$", "ď": "d$", "é": "e%", "ê": "e^", "ë": "e:", "è": "e`", "ě": "e$", "ė": "e.", "ē": "e-", "ę": "e,",
    "ģ": "g,", "ğ": "g$", "í": "i%", "ì": "i`", "ī": "i-", "į": "i,", "î": "i^", "i": "i;", "ï": "i:", "ĳ": "ij;", "ķ": "k,", "ļ": "l,", "ł": "l-", "ĺ": "l%", "ľ": "l'",
    "ñ": "n~", "ņ": "n,", "ń": "n%", "ó": "o%", "ô": "o^", "ö": "o:", "ò": "o`",  "œ": "oe;", "ø": "o/",  "ō": "o-", "õ": "o~", "ő": "o#", "ŗ": "r,", "ŕ": "r%", "ř": "r$", "ß": "ss;", "ś": "s%", "š": "s$", "ş": "s,", "ţ": "t,", "ť": "t$",
    "ú": "u%", "ü": "u:", "û": "u^", "ù": "u`", "ű": "u#", "ų": "u,", "ū": "u-", "ů": "uo;", "ŭ": "u$", "ý": "y%", "ÿ": "y:", "ž": "z$", "ż": "z.", "ź": "z%", "a̍": "a'", "ǎ": "a$", "a̋": "a#", "e̋": "e#", "e̍": "e'", "i̍": "i'", "ǐ": "i$", "i̋": "i#", 
    "o̍": "o'", "ǒ": "o$", "ū": "u-", "ǔ": "u$", "ḿ": "m%", "m̂": "m^", "m̀": "m`", "m̄": "m-", "m̍": "m'", "n̂": "n^", "ń": "n%", "ǹ": "n`", "n̄": "n-", "n̍": "n'", "ⁿ": "n+", "o͘": "o.;", "ô͘": "o^;", "ó͘": "o%;", "ò͘": "o`;", "ō͘": "o-;", 
    "ŝ": "s^", "ĝ": "g^", "ĵ": "j^", "ĉ": "c^", "ŵ": "w^", "ŋ": "ng;", "ċ": "c.", "\u207f": "n+", "\u00ba": "o+", "\u02b7": "w+", "\u02b2": "j+", "\u02b0": "h+"
    }


#函數庫：
def prmpbox(i, message, top):
    def show_messages(i, message, top):
        for _ in range(i):
            messagebox.showinfo(top, message)
    root = tk.Tk()
    root.title("")
    root.geometry("0x0")
    show_messages(i, message, top)
    root.destroy()
    root.mainloop()



if matches:
    maint = matches.group(1)
    vicet = matches.group(2)
    bep = matches.group(3)
    if maint == "txt":
        if vicet == "latinex":
            for old_char, new_char in char_mapping.items():
                text = text.replace(new_char, old_char)
            returnt = text.replace("]]", "")
        elif vicet == "squiggle":
            matches = re.search(pattern2, bep)
            if matches:
                fvt = matches.group(1)
                fbep = matches.group(2)
                if fvt == "rnd":
                    translation_table = str.maketrans(template, template1)
                    returnt = fbep.translate(translation_table)
                elif fvt == "sqr":
                    translation_table = str.maketrans(template, template3)
                    returnt = fbep.translate(translation_table)
                elif fvt == "crsv":
                    translation_table = str.maketrans(template, template4)
                    returnt = fbep.translate(translation_table)
                elif fvt == "crsvb":
                    translation_table = str.maketrans(template, template5)
                    returnt = fbep.translate(translation_table)
                elif fvt == "wrt":
                    translation_table = str.maketrans(template, template6)
                    returnt = fbep.translate(translation_table)
                elif fvt == "gthc":
                    translation_table = str.maketrans(template, template7)
                    returnt = fbep.translate(translation_table)
                elif fvt == "gthcb":
                    translation_table = str.maketrans(template, template8)
                    returnt = fbep.translate(translation_table)
                elif fvt == "bld":
                    translation_table = str.maketrans(template, template9)
                    returnt = fbep.translate(translation_table)
                elif fvt == "itlc":
                    translation_table = str.maketrans(template, template10)
                    returnt = fbep.translate(translation_table)
                elif fvt == "itlcb":
                    translation_table = str.maketrans(template, template11)
                    returnt = fbep.translate(translation_table)
                elif fvt == "fsp":
                    translation_table = str.maketrans(template, template12)
                    returnt = fbep.translate(translation_table)
                else:
                    returnt = text
            else:
                print("No match found in bep:", bep)
    elif maint == "sys":
        if vicet == "prmpbox":
            matches = re.search(pattern2, bep)
            if matches:
                times = int(matches.group(1))
                fbep = matches.group(2)
                matches = re.search(pattern2, fbep)
                if matches:
                    top = matches.group(1)
                    inside = matches.group(2)
                    prmpbox(times, inside, top)
'''
    elif maint == "prg":

    else:
        returnt = text
'''
print(returnt)