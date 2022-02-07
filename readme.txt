Uh, Mana here.
I'll explain how to install RNS Remix 4.02.
If you find any bugs, please post them to the BBS.

■ Fixes

Fixed a bug in 4.00 and 4.01, there was a bug in convert.cgi that prevented it from taking over logs properly. There was also the possibility for bbs.cgi to overwrite previous data files, so that was also fixed. I feel like I've finally made something decent...

■ Features since 4.00

By creating a list file, the server load should be significantly reduced compared to the previous version.
For various reasons, it's no longer possible to change the board's appearance.
Also, I made some minor usability changes to the system, but I'm not going to detail everything because that would be a pain in the ass.
I didn't think this update would take a year...


■ Installation guidelines

* indicates changes/additions from 3.513 or earlier

public_html (home directory)
         　　|
         　　|-- cgi-bin (optional)
         　　　　　|       
         　　　　　|-- bbs.cgi (755)　　　     　Main script *
         　　　　　|-- bbsreg.cgi (755)　　　 Posting script *
         　　　　　|-- bbssrc.cgi (755)　　　 Thread view script
         　　　　　|-- bbsedit.cgi (755)　　　 　Post deletion script
         　　　　　|-- jcode.pl (755)     　　　 　Japanese library
         　　　　　|-- getlog_m.cgi (755)　　　 　Log search script *
         　　　　　|-- convert.cgi (755)　　　 　Only for users of the previous version *
         　　　　　|  
         　　　　　|-- list.log (666)　　　  File where the latest list data is written to
         　　　　　|-- bbs.log (666)　　　  File where the latest post data is written to
         　　　　　|  
         　　　　　|-- data (folder 777)　　　  Folder to store all the topics
         　　　　　|  
         　　　　　|-- bbsnum (folder 777)　　　  Folder for the counters that determine topic id numbers *
         　　　　　|  
         　　　　　|-- log (folder 777)　　　  Folder to store recorded logs
         　　　　　|  
         　　　　　|-- count1 (folder 777)　　 Folder to store hit counters


■ For those who are installing for the very first time

You don't have to put anything in any of the folders.
All the .log files can also be empty.


■ For those who used RNS Remix 3.513 or earlier

Leave all the folders as they are.
Create an empty list.log, install convert.cgi, then open it in your browser.
A list.log will be generated automatically.
It doesn't convert any of the files in the data directory, so you can downgrade if you want to.
Don't forget to set up an empty bbsnum folder...

--------------------------------------------------------------------------------

Translator's addendum (2021/10/14)

■ I'm having problems with this script or would like to report a bug/mistranslation, where should I go to post about it?

For now, https://ayashii.net/bbs.php and https://dis.heyuri.net/lounge/ are probably the best places to discuss this script and the translation project.


■ How do I post as admin? ($adminpost and crypt.cgi)

Without an encrypted admin password, you cannot post as administrator. To generate the encrypted admin password manually, you can open up the included crypt.cgi in a web browser. Once you've generated the required string and pasted the result into the $adminpost setting in bbs.cgi, you should be able to type your original unencrypted password into the name field when posting to activate the administrator capcode.

Attempting to use the admin name without using the password will add (fraudster) to the end of your name, and using the encrypted password as your name will result in (hacker) being displayed instead.


■ Can I modify the genres?

Yes, but there's caveats. The names of the genres (found in the @genname setting of bbs.cgi) can be modified freely at any time with little consequence, but modifying an existing genre's ID (@genid) will cause all kinds of problems and headaches. Avoid changing existing genre IDs unless the genre in question is unused or you want to delete it. Adding/removing IDs isn't a problem so long as the order of the IDs matches up with the order of the genre names. Remember to increase/decrease the $gens setting appropriately as well.


■ Where can I put a banner or announcement on the topic list page?

If you search for "# Banner goes here" in bbs.cgi, you'll find the banner/announcement section. A template for an announcement is provided, just uncomment it and replace the text with whatever you want.


■ Where did this script originate?

In October 2021, while digging through various Ayashii World-related archives, I discovered copies of various scripts used on Mana's Ayashii World boards circa 1999 here: https://web.archive.org/web/20030202120105/http://www.bea.hi-ho.ne.jp/strangeworld/

I then discovered there was a later version named RNS REMIX 3.513: https://web.archive.org/web/20020118112042/http://www.rns.f2s.com/

And then after playing with that for a while and getting annoyed with the bugs, I discovered RNS Remix 4.02 on this page: https://web.archive.org/web/20050212113919/http://www.acc.ne.jp/~remix/script.html

The .lzh archive may have been corrupted in the archival process as there were issues with the files upon extracting. I managed to solve most of them by opening the files with Shift JIS encoding, and removing the garbage data at the tops and bottoms of all the files. After that I adjust the Perl paths, and replaced the supplied jcode.pl with this "fixed for Perl 5.20+" version: https://piano2nd.smb.net/PukiWiki/index.php?%E5%8F%A4%E3%81%84CGI (this is a must-have if you want to run old Japanese scripts, the old versions will lead to errors.)

RNS Remix 4.02 was released on 2002/06/02, and it derives from the REMIX board that was first launched publicly on 1999/05/24. While the earliest version was based on a modified version of Rescue's MiniBBS v7.5, the later versions of the script are based on Kuzuha(くずは)'s KuzuhaScript(くずはすくりぷと) Final Beta #2 pl0.3, which I believe was released on 2000/1/06.

The developer of REMIX and RNS Remix is known as Mana, and they were once a prominent figure in the post-Shiba Ayashii World scene. They were the creator/administor of several prominent Ayashii World BBSes such as REBIRTH, REMIX, and REQUIEM. REBIRTH and REQUIEM in particular were both considered "Main" Ayashii World BBSes during their respective runs, and it's where the iconic #004040 color scheme comes from.

REMIX developed a distinct community and culture, and eventually they parted ways with Mana and joined up with Ayashii World@Christmas Shima (Strange World@Christmas Island). As of October 2021, they still exist at this location: http://www.strangeworld.ne.jp/cgi-bin/remix/bbs.cgi (they block all non-Japanese and non-British IPs from accessing the board, but you can view it from archive.org). They use an older version of the Remix script (3.513), possibly because there were some unpopular UI changes and feature removals between version 3.513 and 4.xx.


■ In that case, why version 4.02 and not 3.513?

In my initial testing, 3.513 appeared to have some annoying bugs with the topic list, while 4.02 did not. There was apparently an updated version of 3.513 released called 3.513b that may have fixed the bugs, but I've yet to find a copy of that version. It wasn't archived by archive.org at the same location I found 4.02, and I haven't been able to find it in other collections of Ayashii World scripts. It may simply be lost to time. (;´Д`)