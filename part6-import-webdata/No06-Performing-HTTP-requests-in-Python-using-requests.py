#Performing HTTP requests in Python using requests
'''
Now that you've got your head and hands around makin
g HTTP requests using the urllib package, you're going to figure out how to do the same using the higher-level requests library. You'll once again be pinging DataCamp servers for their "http://www.datacamp.com/teach/documentation" page.

Note that unlike in the previous exercises using urllib, you don't have to close the connection when using requests!

#Instructions
100 XP
Import the package requests.
Assign the URL of interest to the variable url.
Package the request to the URL, send the request and catch the response with a single function requests.get(), assigning the response to the variable r.
Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable text.
Hit submit to print the HTML of the webpage.
'''

# Code
# Import package
#from urllib.request import Requests   Error: not this lib
import requests
# Specify the url: url
url="http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r=requests.get(url)  #not Requests(url)  And don't need to be closed

# Extract the response: text
text=r.text

# Print the html
print(text)


'''result: the format is differeent from the previous one
<!doctype html>
<html lang="en" data-direction="ltr">
  <head>
    <link href="https://fonts.intercomcdn.com" rel="preconnect" crossorigin>
      <script src="https://www.googletagmanager.com/gtag/js?id=UA-39297847-9" async="async" nonce="roMnx80gAKY2kLbEPHCfV4mRv8CYMnfISDrR6mLOrD0="></script>
      <script nonce="roMnx80gAKY2kLbEPHCfV4mRv8CYMnfISDrR6mLOrD0=">
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-39297847-9');
</script>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>DataCamp Help Center</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="intercom:trackingEvent" content="{&quot;name&quot;:&quot;Viewed Help Center&quot;,&quot;metadata&quot;:{&quot;action&quot;:&quot;viewed&quot;,&quot;object&quot;:&quot;educate_home&quot;,&quot;place&quot;:&quot;help_center&quot;,&quot;owner&quot;:&quot;educate&quot;}}" />

    <link rel="stylesheet" media="all" href="https://intercom.help/_assets/application-d1f7d2f5ecbab279e0c25a70c759326b30d53b9cc5832e8fdc7973fe1bc09ce2.css" />
    <link rel="canonical" href="http://instructor-support.datacamp.com/"/>

        <link href="https://static.intercomassets.com/assets/educate/educate-favicon-64x64-at-2x-52016a3500a250d0b118c0a04ddd13b1a7364a27759483536dd1940bccdefc20.png" rel="shortcut icon" type="image/png" />
      <style>
        .header, .avatar__image-extra { background-color: #263e63; }
        .article a, .c__primary { color: #263e63; }
        .avatar__fallback { background-color: #263e63; }
        article a.intercom-h2b-button { background-color: #263e63; border: 0; }
      </style>

      <meta property="og:title" content="DataCamp Help Center" />
  <meta name="twitter:title" content="DataCamp Help Center" />


<meta property="og:type" content="website" />
<meta property="og:image" content="" />

<meta name="twitter:image" content="" />

  </head>
  <body class="">
    <header class="header">
  <div class="container header__container o__ltr" dir="ltr">
    <div class="content">
      <div class="mo o__centered o__reversed header__meta_wrapper">
        <div class="mo__body">
          <div class="header__logo">
            <a href="/">
                <img alt="DataCamp Help Center" src="https://downloads.intercomcdn.com/i/o/81221/856b63d438031754b681746b/4ea2737e4266936fb423911d9c587812.png" />
            </a>
          </div>
        </div>
        <div class="mo__aside">
          <div class="header__home__url">
              <a target="_blank" rel='noopener' href="http://www.datacamp.com/teach"><svg width="14" height="14" viewBox="0 0 14 14" xmlns="http://www.w3.org/2000/svg"><title>Group 65</title><g stroke="#FFF" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"><path d="M11.5 6.73v6.77H.5v-11h7.615M4.5 9.5l7-7M13.5 5.5v-5h-5"/></g></svg><span>Go to DataCamp</span></a>
          </div>
        </div>
      </div>
          <h1 class="header__headline">Advice and answers from the DataCamp Team</h1>
        <form action="/" autocomplete="off" class="header__form search">
          <input type="text" autocomplete="off" class="search__input js__search-input o__ltr" placeholder="Search for articles..." tabindex="1" name="q" value="">
          <div class="search_icons">
            <button type="submit" class="search__submit o__ltr"></button>
            <a class="search__clear-text__icon">
              <svg class="interface-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
                <path d="M8.018 6.643L5.375 4 4 5.375l2.643 2.643L4 10.643 5.375 12l2.643-2.625L10.625 12 12 10.643 9.357 8.018 12 5.375 10.643 4z" />
              </svg>
            </a>
        </form>
      </div>
    </div>
  </div>
</header>

    <div class="container">
      <div class="content educate_content"><section class="section">
    <div class="g__space">
      <a href="/getting-started" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="chat-star" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linejoin="round"><path d="M20 34.942c-2.083-.12-4.292-.42-6-.942L3 39l4-9c-3.858-3.086-6-7.246-6-12C1 8.61 10.328 1 21.835 1 33.343 1 43 8.61 43 18c0 1.044-.117 2.065-.342 3.057"></path><path d="M36.016 25L40 33h7l-6 5 3 9-8-5.494L28 47l3-9-6-5h7l4.016-8z"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Getting Started</h2>
            <p class="paper__preview">Everything you need to know to begin your DataCamp journey!</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2352718/square_128/Rebecca_Robins_-_Headshot-1535969735.jpg?1535969735" alt="Becca Robins avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2678519/square_128/pic2-1539176502.JPG?1539176502" alt="Jen Bricker avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2637958/square_128/YR_Headshot-1539175806.JPG?1539175806" alt="Yashas Roy avatar" class="avatar__image">

      <span class="avatar__image avatar__fallback">+2</span>
  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        11 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> Becca Robins,</span> <span class='c__darker'> Jen Bricker,</span> <span class='c__darker'> Yashas Roy</span> and 2 others
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
    <div class="g__space">
      <a href="/courses" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="devices-laptop" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round"><path d="M41 31H7V11h34v20z"></path><path d="M3 35V10a3 3 0 0 1 3-3h36a3 3 0 0 1 3 3v25m-16 0v2H19v-2H1v4a2 2 0 0 0 2 2h42a2 2 0 0 0 2-2v-4H29z" stroke-linejoin="round"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Courses</h2>
            <p class="paper__preview">Everything you need to know about creating DataCamp courses.</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2637958/square_128/YR_Headshot-1539175806.JPG?1539175806" alt="Yashas Roy avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2247397/square_128/IMG_2763_final_square_small-1532522734.jpg?1532522734" alt="Nick Carchedi avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2366194/square_128/richie-in-hairnet-1537451295.JPG?1537451295" alt="Richie Cotton avatar" class="avatar__image">

      <span class="avatar__image avatar__fallback">+7</span>
  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        78 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> Yashas Roy,</span> <span class='c__darker'> Nick Carchedi,</span> <span class='c__darker'> Richie Cotton</span> and 7 others
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
    <div class="g__space">
      <a href="/daily-practice" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="tools-dashboard" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round" stroke-linejoin="round"><path d="M27 31a3 3 0 0 1-6 0 3 3 0 0 1 6 0zm-.88-2.12l9.9-9.9M5 32h4m34 .002L39 32m2.553-8.27l-3.696 1.53M31.27 13.447l-1.53 3.695M24 12v4m-7.27-2.553l1.53 3.695m-7.694.422l2.826 2.83M6.447 23.73l3.695 1.53"></path><path d="M24 8C11.297 8 1 18.3 1 31v9h46v-9C47 18.3 36.703 8 24 8z"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Daily Practice</h2>
            <p class="paper__preview">Everything you need to know about creating DataCamp Daily Practice.</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2734728/square_128/Anneleen_Beckers-xtra-small-1541624054.jpg?1541624054" alt="Anneleen Beckers avatar" class="avatar__image">

  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        12 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> Anneleen Beckers</span>
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
    <div class="g__space">
      <a href="/projects" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="book-opened2"><path d="M24 11c0-3.866 10.297-7 23-7v33c-12.703 0-23 3.134-23 7 0-3.866-10.3-7-23-7V4c12.7 0 23 3.134 23 7zm0 0v32m-5-27.52c-3.22-1.232-7.773-2.128-13-2.48m13 8.48c-3.22-1.232-7.773-2.128-13-2.48m13 8.48c-3.22-1.232-7.773-2.128-13-2.48m13 8.48c-3.22-1.23-7.773-2.127-13-2.48m23-15.52c3.223-1.232 7.773-2.128 13-2.48m-13 8.48c3.223-1.232 7.773-2.128 13-2.48m-13 8.48c3.223-1.232 7.773-2.128 13-2.48m-13 8.48c3.223-1.23 7.773-2.127 13-2.48" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Projects</h2>
            <p class="paper__preview">Everything you need to know about creating DataCamp projects.</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2360843/square_128/20170928_DavidV_ByBBImagery-022-1380-1537479799.jpg?1537479799" alt="David Venturi avatar" class="avatar__image">

  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        19 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> David Venturi</span>
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
    <div class="g__space">
      <a href="/course-editor-basics" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="book-bookmark" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linecap="round"><path d="M35 31l-6-6-6 6V7h12v24z"></path><path d="M35 9h6v38H11a4 4 0 0 1-4-4V5" stroke-linejoin="round"></path><path d="M39 9V1H11a4 4 0 0 0 0 8h12" stroke-linejoin="round"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Course Editor Basics</h2>
            <p class="paper__preview">Everything you need to know to get going with our online course editor.</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2352718/square_128/Rebecca_Robins_-_Headshot-1535969735.jpg?1535969735" alt="Becca Robins avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2247397/square_128/IMG_2763_final_square_small-1532522734.jpg?1532522734" alt="Nick Carchedi avatar" class="avatar__image">

  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        5 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> Becca Robins</span> and <span class='c__darker'> Nick Carchedi</span>
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
    <div class="g__space">
      <a href="/tips-and-tricks" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="comms-mail" stroke-width="2" fill="none" fill-rule="evenodd" stroke-linejoin="round"><path d="M47 3L1 22l18 7L47 3z"></path><path d="M47 3l-8 37-20-11L47 3zM19 29v16l7-12"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Tips &amp; Tricks</h2>
            <p class="paper__preview">Become a DataCamp wizard!</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2352718/square_128/Rebecca_Robins_-_Headshot-1535969735.jpg?1535969735" alt="Becca Robins avatar" class="avatar__image">

  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        6 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> Becca Robins</span>
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
    <div class="g__space">
      <a href="/frequently-asked-questions-faq" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="chat-question" fill="none" fill-rule="evenodd"><path d="M47 21.268c0 10.363-10.297 18.765-23 18.765-2.835 0-5.55-.418-8.058-1.184L2.725 45 7.9 34.668c-4.258-3.406-6.9-8.15-6.9-13.4C1 10.904 11.297 2.502 24 2.502s23 8.402 23 18.766z" stroke-width="2" stroke-linejoin="round"></path><path d="M25 28.502a2 2 0 1 0 0 4 2 2 0 0 0 0-4" fill="#231F1F"></path><path d="M19 17.75c0-3.312 2.686-6.124 6-6.124 3.313 0 6 2.626 6 5.938 0 3.315-2.687 5.938-6 5.938V26" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Frequently Asked Questions (FAQ)</h2>
            <p class="paper__preview">Common questions that arise during content creation.</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2352718/square_128/Rebecca_Robins_-_Headshot-1535969735.jpg?1535969735" alt="Becca Robins avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2366194/square_128/richie-in-hairnet-1537451295.JPG?1537451295" alt="Richie Cotton avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2637958/square_128/YR_Headshot-1539175806.JPG?1539175806" alt="Yashas Roy avatar" class="avatar__image">

      <span class="avatar__image avatar__fallback">+3</span>
  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        48 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> Becca Robins,</span> <span class='c__darker'> Richie Cotton,</span> <span class='c__darker'> Yashas Roy</span> and 3 others
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
    <div class="g__space">
      <a href="/miscellaneous" class="paper ">
        <div class="collection o__ltr">
          <div class="collection__photo">
            <svg role='img' viewBox='0 0 48 48'><g id="tools-edit"><path d="M14.932 43.968L2 47l3.033-12.93 31.2-31.203a4 4 0 0 1 5.658 0l4.247 4.243a4 4 0 0 1 0 5.656L14.932 43.968zm29.84-29.735L34.82 4.28m7.125 12.782L31.992 7.11M15.436 43.465l-9.9-9.9" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
          </div>
          <div class="collection_meta" dir="ltr">
            <h2 class="t__h3 c__primary">Miscellaneous</h2>
            <p class="paper__preview">Have a question for DataCamp, but not about creating content? You&#39;ll probably find the answer here.</p>
            <div class="avatar">
  <div class="avatar__photo avatars__images o__ltr">
        <img src="https://static.intercomassets.com/avatars/2352718/square_128/Rebecca_Robins_-_Headshot-1535969735.jpg?1535969735" alt="Becca Robins avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2830289/square_128/IMG_0665_a-1545331304.jpg?1545331304" alt="Lisa Monteleone avatar" class="avatar__image">

        <img src="https://static.intercomassets.com/avatars/2859053/square_128/gabriel_about_pic-1546620603.jpg?1546620603" alt="Gabriel de Selding avatar" class="avatar__image">

  </div>
  <div class="avatar__info">
    <div>
      <span class="c__darker">
        9 articles in this collection
      </span>
      <br>
      Written by <span class='c__darker'> Becca Robins,</span> <span class='c__darker'> Lisa Monteleone,</span> and <span class='c__darker'> Gabriel de Selding</span>
    </div>
  </div>
</div>

          </div>
        </div>
      </a>
    </div>
</section>
</div>
    </div>
    <footer class="footer">
  <div class="container">
    <div class="content">
      <div class="u__cf"  dir="ltr">
        <div class="footer__logo">
          <a href="/">
              <img alt="DataCamp Help Center" src="https://downloads.intercomcdn.com/i/o/81221/856b63d438031754b681746b/4ea2737e4266936fb423911d9c587812.png" />
          </a>
        </div>
        <div class="footer__advert logo">
          <img src="https://intercom.help/_assets/intercom-a6a6ac0f033657af1aebe2e9e15b94a3cd5eabf6ae8b9916df6ea49099a894d8.png" alt="Intercom" />
          <a href="https://www.intercom.com/intercom-link?company=DataCamp&amp;solution=customer-support&amp;utm_campaign=intercom-link&amp;utm_content=We+run+on+Intercom&amp;utm_medium=help-center&amp;utm_referrer=http%3A%2F%2Finstructor-support.datacamp.com%2F&amp;utm_source=desktop-web">We run on Intercom</a>
        </div>
      </div>
    </div>
  </div>
</footer>

    
  <script nonce="roMnx80gAKY2kLbEPHCfV4mRv8CYMnfISDrR6mLOrD0=">
    window.intercomSettings = {"app_id":"ug0ps1rq"};
</script>
  <script nonce="roMnx80gAKY2kLbEPHCfV4mRv8CYMnfISDrR6mLOrD0=">
    (function(){var w=window;var ic=w.Intercom;if(typeof ic==="function"){ic('reattach_activator');ic('update',intercomSettings);}else{var d=document;var i=function(){i.c(arguments)};i.q=[];i.c=function(args){i.q.push(args)};w.Intercom=i;function l(){var s=d.createElement('script');s.type='text/javascript';s.async=true;s.src="https://widget.intercom.io/widget/ug0ps1rq";var x=d.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x);}if(w.attachEvent){w.attachEvent('onload',l);}else{w.addEventListener('load',l,false);}}})()
</script>

    

    <script src="https://intercom.help/_assets/application-4500b8159f32efa509d5464e27ebd8e4735c3a0e4b59bd4aab6c00e8e49c04d2.js" nonce="roMnx80gAKY2kLbEPHCfV4mRv8CYMnfISDrR6mLOrD0="></script>
  </body>
</html>

'''