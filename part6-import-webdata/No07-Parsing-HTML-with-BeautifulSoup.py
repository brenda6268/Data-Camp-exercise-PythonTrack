#Parsing HTML with BeautifulSoup
'''
In this interactive exercise, you'll learn how to use the BeautifulSoup package to parse, prettify and extract information from HTML. You'll scrape the data from the webpage of Guido van Rossum, Python's very own Benevolent Dictator for Life. In the following exercises, you'll prettify the HTML and then extract the text and the hyperlinks.

The URL of interest is url = 'https://www.python.org/~guido/'.

#Instructions
100 XP
Import the function BeautifulSoup from the package bs4.
Assign the URL of interest to the variable url.
Package the request to the URL, send the request and catch the response with a single function requests.get(), assigning the response to the variable r.
Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable html_doc.
Create a BeautifulSoup object soup from the resulting HTML using the function BeautifulSoup().
Use the method prettify() on soup and assign the result to pretty_soup.
Hit submit to print to prettified HTML to your shell!
'''
# Code
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url= 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r=requests.get(url)

# Extracts the response as html: html_doc
html_doc=r.text

# Create a BeautifulSoup object from the HTML: soup
soup=BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup=soup.prettify()  # error:  prettify(soup)

# Print the response
print(pretty_soup)

'''result

<html>
 <head>
  <title>
   Guido's Personal Home Page
  </title>
 </head>
 <body bgcolor="#FFFFFF" text="#000000">
  <h1>
   <a href="pics.html">
    <img border="0" src="images/IMG_2192.jpg"/>
   </a>
   Guido van Rossum - Personal Home Page
  </h1>
  <p>
   <a href="http://www.washingtonpost.com/wp-srv/business/longterm/microsoft/stories/1998/raymond120398.htm">
    <i>
     "Gawky and proud of it."
    </i>
   </a>
   <h3>
    <a href="http://metalab.unc.edu/Dave/Dr-Fun/df200004/df20000406.jpg">
     Who
I Am
    </a>
   </h3>
   <p>
    Read
my
    <a href="http://neopythonic.blogspot.com/2016/04/kings-day-speech.html">
     "King's
Day Speech"
    </a>
    for some inspiration.
    <p>
     I am the author of the
     <a href="http://www.python.org">
      Python
     </a>
     programming language.  See also my
     <a href="Resume.html">
      resume
     </a>
     and my
     <a href="Publications.html">
      publications list
     </a>
     , a
     <a href="bio.html">
      brief bio
     </a>
     , assorted
     <a href="http://legacy.python.org/doc/essays/">
      writings
     </a>
     ,
     <a href="http://legacy.python.org/doc/essays/ppt/">
      presentations
     </a>
     and
     <a href="interviews.html">
      interviews
     </a>
     (all about Python), some
     <a href="pics.html">
      pictures of me
     </a>
     ,
     <a href="http://neopythonic.blogspot.com">
      my new blog
     </a>
     , and
my
     <a href="http://www.artima.com/weblogs/index.jsp?blogger=12088">
      old
blog
     </a>
     on Artima.com.  I am
     <a href="https://twitter.com/gvanrossum">
      @gvanrossum
     </a>
     on Twitter.  I
also have
a
     <a href="https://plus.google.com/u/0/115212051037621986145/posts">
      G+
profile
     </a>
     .
     <p>
      In January 2013 I joined
      <a href="http://www.dropbox.com">
       Dropbox
      </a>
      .  I work on various Dropbox
products and have 50% for my Python work, no strings attached.
Previously, I have worked for Google, Elemental Security, Zope
Corporation, BeOpen.com, CNRI, CWI, and SARA.  (See
my
      <a href="Resume.html">
       resume
      </a>
      .)  I created Python while at CWI.
      <h3>
       How to Reach Me
      </h3>
      <p>
       You can send email for me to guido (at) python.org.
I read everything sent there, but if you ask
me a question about using Python, it's likely that I won't have time
to answer it, and will instead refer you to
help (at) python.org,
       <a href="http://groups.google.com/groups?q=comp.lang.python">
        comp.lang.python
       </a>
       or
       <a href="http://stackoverflow.com">
        StackOverflow
       </a>
       .  If you need to
talk to me on the phone or send me something by snail mail, send me an
email and I'll gladly email you instructions on how to reach me.
       <h3>
        My Name
       </h3>
       <p>
        My name often poses difficulties for Americans.
        <p>
         <b>
          Pronunciation:
         </b>
         in Dutch, the "G" in Guido is a hard G,
pronounced roughly like the "ch" in Scottish "loch".  (Listen to the
         <a href="guido.au">
          sound clip
         </a>
         .)  However, if you're
American, you may also pronounce it as the Italian "Guido".  I'm not
too worried about the associations with mob assassins that some people
have. :-)
         <p>
          <b>
           Spelling:
          </b>
          my last name is two words, and I'd like to keep it
that way, the spelling on some of my credit cards notwithstanding.
Dutch spelling rules dictate that when used in combination with my
first name, "van" is not capitalized: "Guido van Rossum".  But when my
last name is used alone to refer to me, it is capitalized, for
example: "As usual, Van Rossum was right."
          <p>
           <b>
            Alphabetization:
           </b>
           in America, I show up in the alphabet under
"V".  But in Europe, I show up under "R".  And some of my friends put
me under "G" in their address book...
           <h3>
            More Hyperlinks
           </h3>
           <ul>
            <li>
             Here's a collection of
             <a href="http://legacy.python.org/doc/essays/">
              essays
             </a>
             relating to Python
that I've written, including the foreword I wrote for Mark Lutz' book
"Programming Python".
             <p>
              <li>
               I own the official
               <a href="images/license.jpg">
                <img align="center" border="0" height="75" src="images/license_thumb.jpg" width="100">
                 Python license.
                </img>
               </a>
               <p>
               </p>
              </li>
             </p>
            </li>
           </ul>
           <h3>
            The Audio File Formats FAQ
           </h3>
           <p>
            I was the original creator and maintainer of the Audio File Formats
FAQ.  It is now maintained by Chris Bagwell
at
            <a href="http://www.cnpbagwell.com/audio-faq">
             http://www.cnpbagwell.com/audio-faq
            </a>
            .  And here is a link to
            <a href="http://sox.sourceforge.net/">
             SOX
            </a>
            , to which I contributed
some early code.
           </p>
          </p>
         </p>
        </p>
       </p>
      </p>
     </p>
    </p>
   </p>
  </p>
 </body>
</html>
<hr>
 <a href="images/internetdog.gif">
  "On the Internet, nobody knows you're
a dog."
 </a>
 <hr>
 </hr>
</hr>

'''
