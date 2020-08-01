"""Provides account data.

@author Adrian Parker
 """

from bs4 import BeautifulSoup
from src.call_account import *


def get_call_accounts(live=False):
    """Accessor for set of call accounts.

    Args:
      live: return live data or not. Defaults to False
    Returns:
      Array of CallAccount
    """

    accounts = []
    for account in _get_accounts(_get_call_account_html(live)):
        accounts.append(CallAccount(account))
    return accounts


def get_call_accounts_from_html(html):
    """Accessor for set of call accounts, derived from given html.

    Args:
      html: to exract call account data from.
    Returns:
      Array of CallAccount
    """

    accounts = []
    for account in _get_accounts(html):
        accounts.append(CallAccount(account))
    return accounts


def get_call_account_institution_names(live=False):
    """Accessor for set of institution names of the institutions providing call accounts.

    Args:
      live: derive names from live data, or not. Defaults to False
    Returns:
      Array of str
    """

    return _get_institution_names(_get_call_account_html(live))


def _get_accounts(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_rows = soup.find_all('tr')
    accounts = []
    for row in table_rows:
        if row.get('class') and 'primary_row' in row['class']:
            institution = _get_institution(row)
        tds = row.find_all('td')
        if len(tds) == 5:
            credit_rating = tds[1].string
            account_type = tds[2].string
            min_amount = float(tds[3].string.replace('$', '').replace(',', ''))
            nominal = _get_nominal(tds[4])
            accounts.append([institution, credit_rating,
                             account_type, min_amount, nominal])
    return accounts


def _get_institution_names(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_rows = soup.find_all('tr')
    institutions = []
    for row in table_rows:
        if row.get('class') and 'primary_row' in row['class']:
            institutions.append(_get_institution(row))
    return institutions


def _get_nominal(tag):
    # tag may include an up or down indicator img; if so will be child b tag
    b = tag.find('b')
    nominal = b.contents[0] if b else tag.string
    return float(nominal)


def _get_institution(tag):
    anchor = tag.find('a')
    anchor_img = anchor.find('img')
    institution = anchor_img['alt'] if anchor_img else anchor.string
    # remove any trailing spaces
    while institution[-1] == ' ':
        institution = institution[:-1]
    return institution


def _get_call_account_html(live=True):
    if live:
        # "https://www.interest.co.nz/saving/call-account"
        raise NotImplementedError()
    else:
        # sample taken at 17/07/2020
        return r"""
    <html>
    <head>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="shortcut icon" href="https://www.interest.co.nz/sites/all/themes/interest_19/favicon.gif" type="image/gif" />
    <meta name="generator" content="Drupal 7 (https://www.drupal.org)" />
    <link rel="canonical" href="https://www.interest.co.nz/saving/call-account" />
    <link rel="shortlink" href="https://www.interest.co.nz/saving/call-account" />
    <meta property="og:site_name" content="interest.co.nz" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://www.interest.co.nz/saving/call-account" />
    <meta property="og:title" content="Standard savings accounts" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:url" content="https://www.interest.co.nz/saving/call-account" />
    <meta name="twitter:title" content="Standard savings accounts" />
      <title>Standard savings accounts | interest.co.nz</title>
      <link type="text/css" rel="stylesheet" href="https://www.interest.co.nz/sites/default/files/css/css_xE-rWrJf-fncB6ztZfd2huxqgxu4WO-qwma6Xer30m4.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.interest.co.nz/sites/default/files/css/css_ugmd-SSDbm1OKE5izFKyWoDlN0VLzOd_7qwRN49enDo.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.interest.co.nz/sites/default/files/css/css_TgSGRqmLJOlGXFvFcKlXbuL6HyUBoh1mSO4zK9piWmA.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.interest.co.nz/sites/default/files/css/css_9QAsD1IHKbFu9Zpw4oIZC-93fLehhxoI38rcLhA1t70.css" media="all" />
    <link type="text/css" rel="stylesheet" href="https://www.interest.co.nz/sites/default/files/css/css_1MNfDLc11cP7WSWyxXMHK0Z9_gYZAY3zdNX5fA98j70.css" media="all" />
      <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    window.jQuery || document.write("<script src='/sites/all/modules/jquery_update/replace/jquery/1.10/jquery.min.js'>\x3C/script>")
    //--><!]]>
    </script>
    <script type="text/javascript" src="https://www.interest.co.nz/sites/default/files/js/js_uJR3Qfgc-bGacxkh36HU9Xm2Q98e_V5UWlFISwie5ro.js"></script>
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js"></script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    window.jQuery.ui || document.write("<script src='/sites/all/modules/jquery_update/replace/ui/ui/minified/jquery-ui.min.js'>\x3C/script>")
    //--><!]]>
    </script>
    <script type="text/javascript" src="https://www.interest.co.nz/sites/default/files/js/js_kVYUHPow03cU_mL4c7JNnI9gyFiLNdVAM2yU5r_fAPs.js"></script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    (function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","https://www.google-analytics.com/analytics.js","ga");ga("create", "UA-256522-2", {"cookieDomain":"auto"});ga("set", "anonymizeIp", true);ga("send", "pageview");
    //--><!]]>
    </script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--

        (function(d) {
          var el, fjs = d.getElementsByTagName("script")[0];
                el = d.createElement("script");
                el.id = "js-pp-banner";
                el.src = "//dashboard.presspatron.com/dev/banner?b=otsLiLFCX82yC86Cnz4DiJa6";
                fjs.parentNode.insertBefore(el, fjs);
        }(document));

    //--><!]]>
    </script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--

        (function() {
          if(/[?]supporters$/.test(location.href)) {
            var timer = setInterval(function() {
              if(typeof presspatron != 'undefined' && document.getElementById('pp-banner')) {
                clearInterval(timer);
                presspatron.receiveMessage({'data' : 'modal', 'origin' : 'https://dashboard.presspatron.com'}); } }, 300); } })();

    //--><!]]>
    </script>
    <script type="text/javascript" src="https://www.interest.co.nz/sites/default/files/js/js_bepzBW55BJOj3deHFNi0GvKkWObEg6ybqaHDyTBTWtw.js"></script>
    <script type="text/javascript">
    <!--//--><![CDATA[//><!--
    jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"interest_19","theme_token":"xFuerbqdn5dYXooZ86oiDpFT5SredYiwt_HKKoqdtb4","js":{"sites\/all\/modules\/custom\/press_patron\/press_patron.js":1,"\/\/ajax.googleapis.com\/ajax\/libs\/jquery\/1.10.2\/jquery.min.js":1,"0":1,"misc\/jquery-extend-3.4.0.js":1,"misc\/jquery-html-prefilter-3.5.0-backport.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"\/\/ajax.googleapis.com\/ajax\/libs\/jqueryui\/1.10.2\/jquery-ui.min.js":1,"1":1,"sites\/all\/modules\/custom\/tabs\/tabs.js":1,"sites\/all\/modules\/google_analytics\/googleanalytics.js":1,"2":1,"3":1,"4":1,"sites\/all\/themes\/interest_19\/js\/vendor\/slick.min.js":1,"sites\/all\/themes\/interest_19\/js\/scripts.js":1,"sites\/all\/themes\/interest_19\/js\/comments.js":1,"sites\/all\/themes\/interest_19\/js\/expand-image.js":1},"css":{"modules\/system\/system.base.css":1,"modules\/system\/system.menus.css":1,"modules\/system\/system.messages.css":1,"modules\/system\/system.theme.css":1,"misc\/ui\/jquery.ui.core.css":1,"misc\/ui\/jquery.ui.theme.css":1,"misc\/ui\/jquery.ui.tabs.css":1,"sites\/all\/modules\/simplenews\/simplenews.css":1,"modules\/comment\/comment.css":1,"sites\/all\/modules\/date\/date_api\/date.css":1,"sites\/all\/modules\/date\/date_popup\/themes\/datepicker.1.7.css":1,"modules\/field\/theme\/field.css":1,
                  "sites\/all\/modules\/custom\/image_format\/image_format.css":1,"sites\/all\/modules\/custom\/kiwisaver\/kiwisaver.css":1,"modules\/node\/node.css":1,"modules\/search\/search.css":1,"modules\/user\/user.css":1,"sites\/all\/modules\/views\/css\/views.css":1,"sites\/all\/modules\/ctools\/css\/ctools.css":1,"sites\/all\/modules\/panels\/css\/panels.css":1,"sites\/all\/modules\/rate\/rate.css":1,"sites\/all\/modules\/custom\/tabs\/drupal-tabs.css":1,"sites\/all\/modules\/panels\/plugins\/layouts\/onecol\/onecol.css":1,"sites\/all\/modules\/addtoany\/addtoany.css":1,"sites\/all\/modules\/custom\/interest_financial\/interest_financial.css":1,"sites\/all\/modules\/print\/print_ui\/css\/print_ui.theme.css":1,"sites\/all\/themes\/interest_19\/css\/vendor\/slick.css":1,"sites\/all\/themes\/interest_19\/css\/vendor\/slick-theme.css":1,"sites\/all\/themes\/interest_19\/css\/styles.css":1}},"tabs":{"slide":false,"fade":true,"speed":"slow","auto_height":false,"next_text":"next","previous_text":"previous","navigation_titles":0},"googleanalytics":{"trackOutbound":1,"trackMailto":1,"trackDownload":1,"trackDownloadExtensions":"7z|aac|arc|arj|asf|asx|avi|bin|csv|doc(x|m)?|dot(x|m)?|exe|flv|gif|gz|gzip|hqx|jar|jpe?g|js|mp(2|3|4|e?g)|mov(ie)?|msi|msp|pdf|phps|png|ppt(x|m)?|pot(x|m)?|pps(x|m)?|ppam|sld(x|m)?|thmx|qtm?|ra(m|r)?|sea|sit|tar|tgz|torrent|txt|wav|wma|wmv|wpd|xls(x|m|b)?|xlt(x|m)|xlam|xml|z|zip"}});
    //--><!]]>
    </script>

        <!-- SCRIPT NEEDED TO RUN GOOGLE DFP -->
      <!-- Not needed as of now. Publift script doing the work -->
      <!-- <script async='async' src='https://www.googletagservices.com/tag/js/gpt.js'></script> -->

      <!-- Publift Fuse Tag -->
      <script async src="https://cdn.fuseplatform.net/publift/tags/2/2001/fuse.js"></script>
      </head>
    <body class="html not-front not-logged-in no-sidebars page-saving page-saving-call-account">
      <!-- Press Patron Banner -->
      <div id="pp-banner"></div>
      <!-- End Press Patron Banner -->

      <header>
        <div id="header-wrapper">
          <div id="search-block">
            <!-- <div id="search-icon"></div> -->
            <div class="gcse-wrapper">

      <script>
        (function() {
          var cx = '013234808727065659026:_n8ackc_blq';
          var gcse = document.createElement('script');
          gcse.type = 'text/javascript';
          gcse.async = true;
          gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(gcse, s);
        })();
      </script>
      <gcse:search></gcse:search>
              </div>
          </div>
          <div id="logo-block">
            <div id="site-logo"><a href="/"></a></div>
          </div>
          <div id="login-block">
            <a href="/user/register" class="has-button-styles">sign up</a><a href="/user" class="has-button-styles">log in</a>      </div>
        </div>
        <div id="navigation">
          <div id="navigation-wrapper">
            <div id="burger-menu">
            </div>
            <div id="login-block2">
              <a href="/user/register" class="has-button-styles">sign up</a><a href="/user" class="has-button-styles">log in</a>        </div>
            <div id="full-nav">
                <div class="parent-div">
        <a class="parent-link" href="/home">Home </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/podcasts"  >Podcast - subscribe here </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/news">News </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/economic-calendar"  >Economic calendar </a>
                          <a class="child-link white-font" href="/news/2020-economic-rescue-package"  >The crisis rescue package tally </a>
                          <a class="child-link white-font" href="/news/82573/reserve-bank-lays-out-detail-how-it-reviews-our-monetary-policy-settings-and-processes"  >How the OCR is set </a>
                          <a class="child-link white-font" href="/category/tag/tppa"  >TPPA explainer series </a>
                          <a class="child-link white-font" href="/saving/bank-financial-comparator"  >Key bank metrics </a>
                          <a class="child-link white-font" href="/news/105115/budget-202021-summary-all-spending-plans"  >Budget 2020/21 - Spending plan </a>
                          <a class="child-link white-font" href="/news/105190/budget-2020-summary-all-tax-collections"  >Budget 2020/21 - Tax revenue </a>
                          <a class="child-link white-font" href="/news/102724/we-update-nations-economic-benchmarks-second-time-one-after-year-delivery-overall-there"  >New Govt. benchmarks </a>
                          <a class="child-link white-font" href="/opinion/94342/media-world-changing-challenging-readers-who-expect independent-news-data-and-comment"  >Become a Supporter </a>
                          <a class="child-link white-font" href="/podcasts"  >Podcast - subscribe here </a>
                          <a class="child-link white-font" href="https://www.interest.co.nz/gdp-live" target="_blank" >GDP Live </a>
                          <a class="child-link white-font" href="/news/emails-newsletters-sign-up"  >Sign up for our free newsletters </a>
                          <a class="child-link white-font" href="/paid-newsletter/37138"  >Banking newsletter subscription </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/property">Property </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/property/residential-auction-results"  >Residential auction results </a>
                          <a class="child-link white-font" href="/property/commercial-property-sales"  >Commercial property sales </a>
                          <a class="child-link white-font" href="/property/rural-farm-property-sales"  >Farms sold </a>
                          <a class="child-link white-font" href="/property/90395/we-release-new-set-visualisations-showing-how-seven-our-cities-have-grown-over-time"  >'Sprawl' visualisations </a>
                          <a class="child-link white-font" href="https://www.interest.co.nz/property/105655/house-prices-bottom-end-market-have-declined-73-their-march-peak-while-mortgage" target="_blank" >Home loan affordability </a>
                          <a class="child-link white-font" href="/property/house-price-income-multiples"  >Median multiples </a>
                          <a class="child-link white-font" href="/calculators/mortgage-calculator"  >Mortgage calculator </a>
                          <a class="child-link white-font" href="/calculators/mortgage-break-fee-estimator"  >Break fee calculator </a>
                          <a class="child-link white-font" href="/saving/rental-yield-indicator"  >Rental yield indicator </a>
                          <a class="child-link white-font" href="/property/rent-ratio"  >Rent ratio </a>
                          <a class="child-link white-font" href="/property/commercial-property-for-sale"  >Commercial property for sale </a>
                          <a class="child-link white-font" href="/property/lifestyle-blocks"  >Lifestyle blocks for sale </a>
                          <a class="child-link white-font" href="https://www.interest.co.nz/news/emails-newsletters-sign-up" target="_blank" >Sign up for our free Property newsletter </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/borrowing">Borrowing </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/borrowing"  >Mortgage rates </a>
                          <a class="child-link white-font" href="/calculators/mortgage-calculator"  >- Mortgage calculator </a>
                          <a class="child-link white-font" href="/calculators/mortgage-break-fee-estimator"  >- Break fee calculator </a>
                          <a class="child-link white-font" href="/personal-finance/101570/moneyhubs-christopher-walsh-digs-deep-reverse-mortgages-what-they-are-their"  >Reverse mortgage FAQ </a>
                          <a class="child-link white-font" href="/borrowing/revolving-credit"  >Revolving credit </a>
                          <a class="child-link white-font" href="/borrowing/car-loan"  >Car loans </a>
                          <a class="child-link white-font" href="/borrowing/credit-cards"  >Credit cards </a>
                          <a class="child-link white-font" href="/borrowing/personal-loan"  >Personal loans </a>
                          <a class="child-link white-font" href="/borrowing/business-base-rates"  >Business loan rates </a>
                          <a class="child-link white-font" href="/calculators/55377/should-you-fix-or-stay-floating"  >Fix or Float calculator </a>
                          <a class="child-link white-font" href="/property/rent-or-buy"  >Rent or Buy ? </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/saving/term-deposits-1-to-5-years">Saving </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/saving/call-account"  >Savings accounts </a>
                          <a class="child-link white-font" href="/saving/bonus-savings-accounts"  >Bonus savings accounts </a>
                          <a class="child-link white-font" href="/saving/term-deposits-1-to-9-months"  >Term deposits < 1 yr </a>
                          <a class="child-link white-font" href="/saving/term-deposits-1-to-5-years"  >Term deposits 1 - 5 years </a>
                          <a class="child-link white-font" href="/saving/term-pie"  >Term PIEs </a>
                          <a class="child-link white-font" href="/calculators/deposit-calculator"  >Deposit calculator </a>
                          <a class="child-link white-font" href="/saving/interest-codes"  >Interest codes </a>
                          <a class="child-link white-font" href="/credit-ratings-explained"  >Credit ratings explained </a>
                          <a class="child-link white-font" href="/saving/market-platform"  >Private market </a>
                          <a class="child-link white-font" href="/saving/bank-leverage"  >Bank leverage </a>
                          <a class="child-link white-font" href="/saving/deep-freeze-list"  >Deep Freeze list </a>
                          <a class="child-link white-font" href="/saving/porridge-list"  >Porridge list </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/kiwisaver">Kiwisaver </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/kiwisaver/funds"  >Find your fund </a>
                          <a class="child-link white-font" href="/kiwisaver/fund-comparison-table"  >Compare fund categories </a>
                          <a class="child-link white-font" href="/kiwisaver/calculators"  >Calculators </a>
                          <a class="child-link white-font" href="/kiwisaver"  >KiwiSaver news </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/banking">Banking </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/saving/bank-leverage"  >Bank leverage </a>
                          <a class="child-link white-font" href="/credit-ratings-explained"  >Credit ratings explained </a>
                          <a class="child-link white-font" href="/saving/bank-financial-comparator"  >Key bank metrics </a>
                          <a class="child-link white-font" href="/news/82573/reserve-bank-lays-out-detail-how-it-reviews-our-monetary-policy-settings-and-processes"  >How the OCR is set </a>
                          <a class="child-link white-font" href="/opinion/77033/overview-functions-money-and-how-money-and-credit-are-created-nz-economy-examining"  >How money is created </a>
                          <a class="child-link white-font" href="/bonds/64411/if-bank-failed-and-open-bank-resolution-policy-was-implemented-how-would-it-affect-bank"  >How OBR will work </a>
                          <a class="child-link white-font" href="https://www.rbnz.govt.nz/monetary-policy/unconventional-monetary-policy" target="_blank" >About unconventional monetary policy </a>
                          <a class="child-link white-font" href="/borrowing"  >Mortgage interest rates </a>
                          <a class="child-link white-font" href="/saving/term-deposits-1-to-5-years"  >Term deposit interest rates </a>
                          <a class="child-link white-font" href="/category/topic/little-book-scams"  >Scams - how to protect yourself </a>
                          <a class="child-link white-font" href="/paid-newsletter/37138"  >Subscribe to industry newsletter </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/insurance">Insurance </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/insurance-data/car-insurance-compared-january-2018"  >Car insurance - 2018 </a>
                          <a class="child-link white-font" href="/category/tag/house-insurance"  >House cover </a>
                          <a class="child-link white-font" href="/category/tag/climate-change"  >Climate change </a>
                          <a class="child-link white-font" href="http://www.icnz.org.nz/statistics-data/industry-data/" target="_blank" >Industry stats </a>
                          <a class="child-link white-font" href="/users/andrew-hooker"  >Andrew Hooker columns </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/personal-finance">Personal </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/borrowing"  >Mortgage interest rates </a>
                          <a class="child-link white-font" href="/personal-finance/101570/moneyhubs-christopher-walsh-digs-deep-reverse-mortgages-what-they-are-their"  >Reverse mortgages </a>
                          <a class="child-link white-font" href="/saving/term-deposits-1-to-5-years"  >Term deposit interest rates </a>
                          <a class="child-link white-font" href="/category/tag/credit-cards"  >Credit cards </a>
                          <a class="child-link white-font" href="/calculators"  >Calculators </a>
                          <a class="child-link white-font" href="/saving/market-platform"  >Private investments </a>
                          <a class="child-link white-font" href="/kiwisaver"  >KiwiSaver </a>
                          <a class="child-link white-font" href="/saving/gold-spot"  >Gold & silver prices </a>
                          <a class="child-link white-font" href="/saving/gold-coins"  >- Gold coin prices </a>
                          <a class="child-link white-font" href="/saving/gold-bars"  >- Gold bar prices </a>
                          <a class="child-link white-font" href="/saving/scrap-metals"  >- Precious metal scrap prices </a>
                          <a class="child-link white-font" href="/category/topic/little-book-scams"  >Protection from scams </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/rural">Rural </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/rural/beef/bull-m2"  >Bull prices </a>
                          <a class="child-link white-font" href="/rural/beef/steer-p2"  >Steer & heifer prices </a>
                          <a class="child-link white-font" href="/rural/beef/heifer-localtrade"  >Beef local trade prices </a>
                          <a class="child-link white-font" href="/rural/beef/cow-prime"  >Cow prices </a>
                          <a class="child-link white-font" href="/rural/sheep/lamb-y"  >Lamb prices </a>
                          <a class="child-link white-font" href="/rural/sheep/lamb-localtrade"  >Local trade lamb prices </a>
                          <a class="child-link white-font" href="/rural/sheep/wool"  >Wool prices </a>
                          <a class="child-link white-font" href="/rural-data/dairy-industry-payout-history"  >Dairy payout history </a>
                          <a class="child-link white-font" href="/rural/logs"  >Logs </a>
                          <a class="child-link white-font" href="/rural-news/farms-for-sale"  >Farms for sale </a>
                          <a class="child-link white-font" href="/rural"  >All other rural links to data </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/currencies">Currencies </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/currencies/buying-foreign-currency"  >Live rates for buying fx </a>
                          <a class="child-link white-font" href="/currencies/selling-foreign-currency-transfers"  >Live rates to sell TT fx </a>
                          <a class="child-link white-font" href="/currencies/currency-conversion-fees"  >Currency fees </a>
                          <a class="child-link white-font" href="/currencies/rate-pricing"  >Rate pricing </a>
                          <a class="child-link white-font" href="/currencies/spot-rates"  >Spot transactions </a>
                          <a class="child-link white-font" href="/currencies/forward-rates"  >Forward transactions </a>
                          <a class="child-link white-font" href="/currencies/how-currency-swaps-work"  >Currency swaps </a>
                          <a class="child-link white-font" href="/currencies/how-to-do-currency-deals-with-hifx"  >How to do currency deals </a>
                          <a class="child-link white-font" href="/currencies/currency-directory"  >Directory - where to buy/sell </a>
                          <a class="child-link white-font" href="/currencies/subscribe_to_newsletter"  >Daily fx rate sheet email </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/charts">Charts </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/charts/commodities"  >Commodities </a>
                          <a class="child-link white-font" href="/charts/confidence"  >Confidence </a>
                          <a class="child-link white-font" href="/charts/credit"  >Debt (Credit) </a>
                          <a class="child-link white-font" href="/charts/economy"  >Economy </a>
                          <a class="child-link white-font" href="/charts/exchange rates"  >Exchange rates </a>
                          <a class="child-link white-font" href="/charts/interest rates"  >Interest rates </a>
                          <a class="child-link white-font" href="/charts/population"  >Population </a>
                          <a class="child-link white-font" href="/charts/prices"  >Prices </a>
                          <a class="child-link white-font" href="/charts/real estate"  >Real estate </a>
                          <a class="child-link white-font" href="/charts/rural"  >Rural </a>
                          <a class="child-link white-font" href="/charts"  >Full list of all charts </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/calculators">Calculators </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/calculators/deposit-calculator"  >Deposit calculator </a>
                          <a class="child-link white-font" href="/calculators/mortgage-calculator"  >Mortgage calculator </a>
                          <a class="child-link white-font" href="/calculators/borrowing-capacity-calculator"  >How much can you bid? </a>
                          <a class="child-link white-font" href="/calculators/full-function-mortgage-calculator"  >Full-function mortgage calculator </a>
                          <a class="child-link white-font" href="/calculators/lvr-borrowing-capacity-calculator"  >LVR borrowing capacity </a>
                          <a class="child-link white-font" href="/calculators/property-upsize-downsize-calculator"  >Property upsize/downsize </a>
                          <a class="child-link white-font" href="/calculators/principal-payback-milestone-calculator"  >Principal payback milestone </a>
                          <a class="child-link white-font" href="/calculators/mortgage-break-fee-estimator"  >Break fee calculator </a>
                          <a class="child-link white-font" href="/calculators/55377/should-you-fix-or-stay-floating"  >Fix or float calculator </a>
                          <a class="child-link white-font" href="/calculators/credit-card-minimum-payments"  >Credit card real cost </a>
                          <a class="child-link white-font" href="/calculators/cost-of-credit-calculator"  >Real cost of debt </a>
                          <a class="child-link white-font" href="/calculators/retirement-calculator"  >Retirement calculator </a>
                          <a class="child-link white-font" href="/calculators/foreign-currency-calculator"  >Buying foreign currency </a>
                          <a class="child-link white-font" href="/calculators"  >All our calculators </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/bonds">Bonds </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/bonds-data/issues"  >Current prices </a>
                          <a class="child-link white-font" href="/bonds/how-to-read-these-pages"  >How to use our bonds resource </a>
                          <a class="child-link white-font" href="/bonds/how-to-buy-bonds"  >How to buy bonds </a>
                          <a class="child-link white-font" href="/bonds/bond-types"  >Bond types </a>
                          <a class="child-link white-font" href="/bonds/glossary"  >Glossary </a>
                          <a class="child-link white-font" href="/charts/interest-rates/government-bond-rates"  >NZ Govt bond rates </a>
                          <a class="child-link white-font" href="/charts/interest-rates/us-treasures"  >US Treasury bond rates </a>
                      </div>
          </div>
        </div>
      <div class="parent-div">
        <a class="parent-link" href="/business">Business </a>
              <div class="child-dropdown">
            <div class="child-dropdown-inner-wrapper">
                          <a class="child-link white-font" href="/borrowing/business-base-rates"  >Business borrowing rates </a>
                          <a class="child-link white-font" href="/understanding-china"  >Understanding China </a>
                          <a class="child-link white-font" href="/understanding-china"  >- by Professor Ang and guests </a>
                          <a class="child-link white-font" href="/category/tag/tppa"  >TPPA explainer series </a>
                          <a class="child-link white-font" href="/business/how-to-guides"  >How to guides: </a>
                          <a class="child-link white-font" href="/business/60438/we-are-starting-new-13-part-guide-small-business-managers-who-want-achieve-financial"  >- Achieving financial success </a>
                          <a class="child-link white-font" href="/business/60243/first-ten-part-guide-series-how-tackle-often-complex-challenges-companies-face-when"  >- The realities of growth </a>
                          <a class="child-link white-font" href="/category/tag/success-stories"  >Success stories </a>
                          <a class="child-link white-font" href="https://www.interest.co.nz/gdp-live" target="_blank" >GDP Live </a>
                      </div>
          </div>
        </div>
            </div>
            <div id="nav-logo-block">
              <a href="/"></a>
            </div>
          </div>
        </div>
      </header>

    <div id="banner-ad-wrapper">
        <div class="region region-banner">
        <div id="block-dfp-setup-19-interest-19-ros-billboard" class="block block-dfp-setup-19">


      <div class="content">
        <!-- 2332506/interest_19_ROS_Billboard/interest_19_ROS_Billboard -->
            <div data-fuse="21850843980"></div>  </div>
    </div>
      </div>
    </div>


    <div id="page-wrapper">
      <div id="page">


        <div id="content">
          <a id="main-content"></a>

          <div id="main-content-container">

            <div id="main-column-wrapper">
                        <!--<div id="breadcrumb"><h2 class="element-invisible">You are here</h2><div class="breadcrumb"><a href="/">Home</a> » <a href="/saving/term-deposits-1-to-5-years">Saving</a></div></div>-->

                        <h1 class="title" id="page-title"> Standard savings accounts </h1>

                        <div class="tabs">
                        </div>

              <div id="main-column">
                  <div class="region region-content">
        <div id="block-system-main" class="block block-system">


      <div class="content">
        <div class="panel-display panel-1col clearfix" >
      <div class="panel-panel panel-col">
        <div><div class="panel-pane pane-custom pane-1"  >



      <div class="pane-content">
        <p><a href="https://www.rabobank.co.nz/noticesaver/?utm_source=interest.co.nz&amp;utm_medium=banner&amp;utm_campaign=savingsaccount&amp;utm_term=saving_call-account&amp;utm_content=noticesaver" target="_blank"><img src="/banners/rabo-featured-rate-noticesaver-Jul-20.jpg" /></a></p>

    <table border="0" cellpadding="1" cellspacing="1" style="width:760px;"><tbody><tr><td colspan="3">We have updated our coverage of Saving accounts, separating them out by type. Unique pages now exist for the following savings account types:</td>
        </tr><tr><td style="width: 262px;">- <a href="http://www.interest.co.nz/saving/bonus-savings-accounts" target="_blank">Bonus savings accounts</a></td>
          <td style="width: 253px;">- <a href="http://www.interest.co.nz/saving/business-savings-accounts" target="_blank">Business savings accounts</a></td>
          <td style="width: 217px;">- <a href="http://www.interest.co.nz/saving/children-youth-student">Children's accounts</a></td>
        </tr><tr><td style="width: 262px;">- <a href="http://www.interest.co.nz/saving/e-saver-online" target="_blank">Online savings accounts</a></td>
          <td style="width: 253px;">- <a href="http://www.interest.co.nz/saving/call-account" target="_blank">Standard savings accounts</a></td>
        </tr></tbody></table><p style="clear:both;"><a href="" onclick="javascript:window.print()">Printer friendly version of this page</a></p>

    <p style="clear:both;"><a href="http://www.interest.co.nz/saving/term-deposits-1-to-9-months">for term deposits up to 9 months, see here »</a></p>

    <p style="clear:both; padding-bottom:10px;"><a href="http://www.interest.co.nz/calculators/deposit-calculator">Make sense of all these rates by using our Savings Calculator</a></p>
      </div>


      </div>
    <div class="panel-separator"></div><div class="panel-pane pane-node"  >

            <h2 class="pane-title">
          Banks    </h2>


      <div class="pane-content">
        <div about="/node/37807" typeof="sioc:Item foaf:Document">
          <header>
                        <h2><a href="/node/37807" rel="bookmark"></a></h2>
                <span property="dc:title" content="" class="rdf-meta element-hidden"></span><span property="sioc:num_replies" content="0" datatype="xsd:integer" class="rdf-meta element-hidden"></span>    </header>

      <div>
        <table id="interest_financial_datatable" class="interest_financial_datatable">
      <thead>
        <tr>
          <th width="210px" valign="bottom" align="left">Institution</th>
    <th width="12px" class="right" valign="bottom" align="left"><a href="/credit-ratings-explained">Credit Rating</a></th>
    <th width="150px" valign="bottom" align="left">Account type</th>
    <th width="55px" class="right" valign="bottom" align="left">Minimum deposit $</th>
    <th width="55px" class="right" valign="bottom" align="left">Interest rate %</th>    </tr>
      </thead>
      <tbody>
        <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#anz" title="ANZ">ANZ</a></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Online savings </td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Select</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#asb" title="ASB">ASB</a></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">FastSaver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.asb.co.nz/personal/accounts/savings" >0.05</a></td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Unlimited</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Savings On Call</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Savings On Call</td><td width="55px" class="right" valign="middle">$10,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Savings On Call</td><td width="55px" class="right" valign="middle">$25,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Savings On Call</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle">0.08</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Savings On Call</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.08</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#bob" title="Bank of Baroda">Bank of Baroda</a></td><td width="12px" class="right" valign="top">BBB-</td><td width="150px" class="left-align" valign="middle">Savings </td><td width="55px" class="right" valign="middle">$1,000</td><td width="55px" class="right" valign="middle">1.25</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB-</td><td width="150px" class="left-align" valign="middle">Super savings </td><td width="55px" class="right" valign="middle">$1,000</td><td width="55px" class="right" valign="middle">1.25</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#boi" title="Bank of India">Bank of India</a></td><td width="12px" class="right" valign="top">BB+</td><td width="150px" class="left-align" valign="middle">Star savings</td><td width="55px" class="right" valign="middle">$1,000</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB+</td><td width="150px" class="left-align" valign="middle">Star super savings</td><td width="55px" class="right" valign="middle">$1,000</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#bnz" title="BNZ">BNZ</a></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Personal OnCall</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Total Money</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Call</td><td width="55px" class="right" valign="middle">$500,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#psis" title="Co-operative Bank">Co-operative Bank</a></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Online Account</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><b>0.10<img class="interest_financial_indicator-down" src="https://www.interest.co.nz/sites/default/files/images/interest_financial_indicator-down.gif" /></b></td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Smile On Call</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle"><b>0.10<img class="interest_financial_indicator-down" src="https://www.interest.co.nz/sites/default/files/images/interest_financial_indicator-down.gif" /></b></td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Smile On Call</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle"><b>0.10<img class="interest_financial_indicator-down" src="https://www.interest.co.nz/sites/default/files/images/interest_financial_indicator-down.gif" /></b></td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.heartland.co.nz/savings-and-deposits/savings-account?utm_source=interest_nz&utm_medium=logo&utm_campaign=Deposits-savings&utm_content=interest.nz-call-account-page&utm_term=logo" title="Invest in Heartland to invest in New Zealand"><img title="Invest in Heartland to invest in New Zealand" src="https://www.interest.co.nz/images/campaign-logo/heartland-logo-3.jpg" alt="Heartland Bank" style = "border:0 none;"/></a></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Heartland Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.25</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Business Call Accounts</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.heartland.co.nz/savings-and-deposits/savings-account" title="Invest in Heartland to invest in New Zealand">1.00</a></td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Direct Call</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.heartland.co.nz/savings-and-deposits/savings-account" title="Invest in Heartland to invest in New Zealand">1.00</a></td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Heartland Everyday</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Heartland Everyday</td><td width="55px" class="right" valign="middle">$10,000</td><td width="55px" class="right" valign="middle">0.10</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Heartland Everyday</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle">0.15</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Heartland Everyday</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.20</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Heartland Everyday</td><td width="55px" class="right" valign="middle">$250,000</td><td width="55px" class="right" valign="middle">0.30</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">YouChoose </td><td width="55px" class="right" valign="middle">$0</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Heartland Savings Optimiser</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#hsbc" title="HSBC">HSBC</a></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">E-Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.07</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Smart Saver</td><td width="55px" class="right" valign="middle">$0</td><td width="55px" class="right" valign="middle">0.65</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#icbc" title="ICBC ">ICBC </a></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Smart Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.80</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#kiwi" title="Kiwibank">Kiwibank</a></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Notice Saver 90 days</td><td width="55px" class="right" valign="middle">$2,000</td><td width="55px" class="right" valign="middle">1.75</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Notice Saver 32 days</td><td width="55px" class="right" valign="middle">$2,000</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Back-up Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Bill Blaster</td><td width="55px" class="right" valign="middle">$100</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Front Runner</td><td width="55px" class="right" valign="middle">$4,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Front Runner</td><td width="55px" class="right" valign="middle">$15,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Front Runner</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Front Runner</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.25</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#kookmin" title="Kookmin">Kookmin</a></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Personal Cheque</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">Personal Cheque</td><td width="55px" class="right" valign="middle">$250,000</td><td width="55px" class="right" valign="middle">0.20</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.rabobank.co.nz/interest-rates/?utm_source=interest.co.nz&utm_medium=logo&utm_campaign=savingsaccount&utm_term=saving_call-account" title="Click Here To Apply Online"><img title="Click Here To Apply Online" src="https://www.interest.co.nz/images/campaign-logo/rabobank-logo-june-2019.jpg" alt="RaboDirect" style = "border:0 none;"/></a></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">NoticeSaver 60 days</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.rabobank.co.nz/interest-rates/?utm_source=interest.co.nz&utm_medium=rateslink&utm_campaign=savingsaccount&utm_term=saving_call-account" >1.85</a></td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">RaboSaver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.rabobank.co.nz/interest-rates/?utm_source=interest.co.nz&utm_medium=rateslink&utm_campaign=savingsaccount&utm_term=saving_call-account" >0.50</a></td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">RaboSaver</td><td width="55px" class="right" valign="middle">$5,000,000</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.rabobank.co.nz/interest-rates/?utm_source=interest.co.nz&utm_medium=rateslink&utm_campaign=savingsaccount&utm_term=saving_call-account" >0.30</a></td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">PremiumSaver - base</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.rabobank.co.nz/interest-rates/?utm_source=interest.co.nz&utm_medium=rateslink&utm_campaign=savingsaccount&utm_term=saving_bonus-savings-accounts" >0.20</a></td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">PremiumSaver - bonus</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.rabobank.co.nz/interest-rates/?utm_source=interest.co.nz&utm_medium=rateslink&utm_campaign=savingsaccount&utm_term=saving_bonus-savings-accounts" >0.80</a></td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A</td><td width="150px" class="left-align" valign="middle">PremiumSaver - potential rate</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><a class="interest_financial_link" href="https://www.rabobank.co.nz/interest-rates/?utm_source=interest.co.nz&utm_medium=rateslink&utm_campaign=savingsaccount&utm_term=saving_bonus-savings-accounts" >1.00</a></td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#sbs" title="SBS Bank.">SBS Bank.</a></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">i-Save</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Prospector Call</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Prospector Call</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Prospector Call</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.25</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.tsbbank.co.nz?utm_source=interest.co.nz&utm_medium=oncall_logo&utm_campaign=interest.co.nz" title="Find Out More
    "><img title="Find Out More
    " src="https://www.interest.co.nz/images/campaign-logo/tsb-bank-logo-1.gif" alt="TSB Bank" style = "border:0 none;"/></a></td><td width="12px" class="right" valign="top">A-</td><td width="150px" class="left-align" valign="middle">WebSaver</td><td width="55px" class="right" valign="middle">$1,000</td><td width="55px" class="right" valign="middle">0.40</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A-</td><td width="150px" class="left-align" valign="middle">Horizon Savings</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.40</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A-</td><td width="150px" class="left-align" valign="middle">Premier Cheque</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.10</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A-</td><td width="150px" class="left-align" valign="middle">Premier Cheque</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">0.35</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A-</td><td width="150px" class="left-align" valign="middle">Premier Cheque</td><td width="55px" class="right" valign="middle">$35,000</td><td width="55px" class="right" valign="middle">0.55</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A-</td><td width="150px" class="left-align" valign="middle">Premier Cheque</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle">0.95</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">A-</td><td width="150px" class="left-align" valign="middle">Premier Cheque</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">1.15</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#westpac" title="Westpac">Westpac</a></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Notice Saver 32 days</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">AA-</td><td width="150px" class="left-align" valign="middle">Simple Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.05</td></tr>  </tbody>
    </table>
      </div>


    </div>
      </div>


      </div>
    <div class="panel-separator"></div><div class="panel-pane pane-node"  >

            <h2 class="pane-title">
          Brokers    </h2>


      <div class="pane-content">
        <div about="/node/37812" typeof="sioc:Item foaf:Document">
          <header>
                        <h2><a href="/node/37812" rel="bookmark"></a></h2>
                <span property="dc:title" content="" class="rdf-meta element-hidden"></span><span property="sioc:num_replies" content="0" datatype="xsd:integer" class="rdf-meta element-hidden"></span>    </header>

      <div>
        <table id="interest_financial_datatable" class="interest_financial_datatable">
      <thead>
        <tr>
          <th width="210px" valign="bottom" align="left">Institution</th>
    <th width="12px" class="right" valign="bottom" align="left"><a href="/credit-ratings-explained">Credit Rating</a></th>
    <th width="150px" valign="bottom" align="left">Account type</th>
    <th width="55px" class="right" valign="bottom" align="left">Minimum deposit $</th>
    <th width="55px" class="right" valign="bottom" align="left">Interest rate %</th>    </tr>
      </thead>
      <tbody>
        <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#asb" title="ASB Securities">ASB Securities</a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.00</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$250,000</td><td width="55px" class="right" valign="middle">0.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$500,000</td><td width="55px" class="right" valign="middle">0.25</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="http://www.interest.co.nz/directory1.asp#craigs" title="click here for more information"><img title="click here for more information" src="https://www.interest.co.nz/images/campaign-logo/Craigs.gif" alt="Craigs Investment Partners" style = "border:0 none;"/></a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">1.45</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">1.65</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">2.10</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$250,000</td><td width="55px" class="right" valign="middle">2.25</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#Direct" title="Direct Broking">Direct Broking</a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">OMCA</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="http://www.forbar.co.nz" title="click here for more info"><img title="click here for more info" src="https://www.interest.co.nz/images/campaign-logo/Fb_140.gif" alt="Forsyth Barr" style = "border:0 none;"/></a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$3,000</td><td width="55px" class="right" valign="middle">0.00</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">0.25</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Cash Management Trust</td><td width="55px" class="right" valign="middle">$250,000</td><td width="55px" class="right" valign="middle">0.75</td></tr>  </tbody>
    </table>
      </div>


    </div>
      </div>


      </div>
    <div class="panel-separator"></div><div class="panel-pane pane-node"  >

            <h2 class="pane-title">
          Building Societies    </h2>


      <div class="pane-content">
        <div about="/node/37809" typeof="sioc:Item foaf:Document">
          <header>
                        <h2><a href="/node/37809" rel="bookmark"></a></h2>
                <span property="dc:title" content="" class="rdf-meta element-hidden"></span><span property="sioc:num_replies" content="0" datatype="xsd:integer" class="rdf-meta element-hidden"></span>    </header>

      <div>
        <table id="interest_financial_datatable" class="interest_financial_datatable">
      <thead>
        <tr>
          <th width="210px" valign="bottom" align="left">Institution</th>
    <th width="12px" class="right" valign="bottom" align="left"><a href="/credit-ratings-explained">Credit Rating</a></th>
    <th width="150px" valign="bottom" align="left">Account type</th>
    <th width="55px" class="right" valign="bottom" align="left">Minimum deposit $</th>
    <th width="55px" class="right" valign="bottom" align="left">Interest rate %</th>    </tr>
      </thead>
      <tbody>
        <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#hpbs" title="Heretaunga">Heretaunga</a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">On Call</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle"><b>0.50<img class="interest_financial_indicator-down" src="https://www.interest.co.nz/sites/default/files/images/interest_financial_indicator-down.gif" /></b></td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">On Call</td><td width="55px" class="right" valign="middle">$50,000</td><td width="55px" class="right" valign="middle"><b>0.80<img class="interest_financial_indicator-down" src="https://www.interest.co.nz/sites/default/files/images/interest_financial_indicator-down.gif" /></b></td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">On Call</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle"><b>1.20<img class="interest_financial_indicator-down" src="https://www.interest.co.nz/sites/default/files/images/interest_financial_indicator-down.gif" /></b></td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#nelson" title="Nelson">Nelson</a></td><td width="12px" class="right" valign="top">BB+</td><td width="150px" class="left-align" valign="middle">Call</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.75</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB+</td><td width="150px" class="left-align" valign="middle">Target</td><td width="55px" class="right" valign="middle">$100</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB+</td><td width="150px" class="left-align" valign="middle">Target</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB+</td><td width="150px" class="left-align" valign="middle">Cheque</td><td width="55px" class="right" valign="middle">$10,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB+</td><td width="150px" class="left-align" valign="middle">Access</td><td width="55px" class="right" valign="middle">$10,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>  </tbody>
    </table>
      </div>


    </div>
      </div>


      </div>
    <div class="panel-separator"></div><div class="panel-pane pane-node"  >

            <h2 class="pane-title">
          Credit Unions    </h2>


      <div class="pane-content">
        <div about="/node/37810" typeof="sioc:Item foaf:Document">
          <header>
                        <h2><a href="/node/37810" rel="bookmark"></a></h2>
                <span property="dc:title" content="" class="rdf-meta element-hidden"></span><span property="sioc:num_replies" content="0" datatype="xsd:integer" class="rdf-meta element-hidden"></span>    </header>

      <div>
        <table id="interest_financial_datatable" class="interest_financial_datatable">
      <thead>
        <tr>
          <th width="210px" valign="bottom" align="left">Institution</th>
    <th width="12px" class="right" valign="bottom" align="left"><a href="/credit-ratings-explained">Credit Rating</a></th>
    <th width="150px" valign="bottom" align="left">Account type</th>
    <th width="55px" class="right" valign="bottom" align="left">Minimum deposit $</th>
    <th width="55px" class="right" valign="bottom" align="left">Interest rate %</th>    </tr>
      </thead>
      <tbody>
        <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#actu" title="Aotearoa Credit Union">Aotearoa Credit Union</a></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Serious Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.40</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Serious Saver</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Serious Saver</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">0.60</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Home deposit account</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Home deposit account</td><td width="55px" class="right" valign="middle">$1,000</td><td width="55px" class="right" valign="middle">1.75</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Home deposit account</td><td width="55px" class="right" valign="middle">$10,000</td><td width="55px" class="right" valign="middle">2.00</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#fcu" title="First CU">First CU</a></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Online savings</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">1.75</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Moneymaker</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">1.50</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory/" title="NZ Firefighters CU">NZ Firefighters CU</a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Bill Pay Account</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Christmas Club (Membership criteria apply)</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">2.00</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#cua" title="NZCU Auckland">NZCU Auckland</a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">1.50</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">2.00</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#cub" title="NZCU Baywide">NZCU Baywide</a></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Online Saver</td><td width="55px" class="right" valign="middle">$1,000</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Online Saver</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.40</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">0.60</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$100,000</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Goal Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.75</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Christmas Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#cuc" title="NZCU Central">NZCU Central</a></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Money maker</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.40</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Money maker</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Money maker</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">0.60</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Cash Access Shares</td><td width="55px" class="right" valign="middle">$2</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory/#cub" title="NZCU Employees">NZCU Employees</a></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Target Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">1.00</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Loan Provider</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">2.00</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top"></td><td width="150px" class="left-align" valign="middle">Christmas Club</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">3.00</td></tr>
    <tr class="primary_row interest_financial_row_0" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#scu" title="NZCU South">NZCU South</a></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.40</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">0.50</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Success Saver</td><td width="55px" class="right" valign="middle">$20,000</td><td width="55px" class="right" valign="middle">0.60</td></tr>
    <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory#policecu" title="Police CU">Police CU</a></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Achiever Saver (Membership criteria apply)</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.45</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Transactional Account (Membership criteria apply)</td><td width="55px" class="right" valign="middle">$2,000</td><td width="55px" class="right" valign="middle">0.05</td></tr>
    <tr class="interest_financial_row_1" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BBB</td><td width="150px" class="left-align" valign="middle">Christmas Club (Membership criteria apply)</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.45</td></tr>  </tbody>
    </table>
      </div>


    </div>
      </div>


      </div>
    <div class="panel-separator"></div><div class="panel-pane pane-node"  >

            <h2 class="pane-title">
          Finance Companies    </h2>


      <div class="pane-content">
        <div about="/node/37811" typeof="sioc:Item foaf:Document">
          <header>
                        <h2><a href="/node/37811" rel="bookmark"></a></h2>
                <span property="dc:title" content="" class="rdf-meta element-hidden"></span><span property="sioc:num_replies" content="0" datatype="xsd:integer" class="rdf-meta element-hidden"></span>    </header>

      <div>
        <table id="interest_financial_datatable" class="interest_financial_datatable">
      <thead>
        <tr>
          <th width="210px" valign="bottom" align="left">Institution</th>
    <th width="12px" class="right" valign="bottom" align="left"><a href="/credit-ratings-explained">Credit Rating</a></th>
    <th width="150px" valign="bottom" align="left">Account type</th>
    <th width="55px" class="right" valign="bottom" align="left">Minimum deposit $</th>
    <th width="55px" class="right" valign="bottom" align="left">Interest rate %</th>    </tr>
      </thead>
      <tbody>
        <tr class="primary_row interest_financial_row_1" style="border-top:1px solid #CCE2F3;"><td width="210px" class="inst-name" valign="top"><a class="interest_financial_link" href="https://www.interest.co.nz/directory" title="Christian Savings ">Christian Savings </a></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Call</td><td width="55px" class="right" valign="middle">$1</td><td width="55px" class="right" valign="middle">0.10</td></tr>
    <tr class="interest_financial_row_0" style=""><td width="210px" class="inst-name" valign="top"></td><td width="12px" class="right" valign="top">BB</td><td width="150px" class="left-align" valign="middle">Call</td><td width="55px" class="right" valign="middle">$5,000</td><td width="55px" class="right" valign="middle">0.25</td></tr>  </tbody>
    </table>
      </div>


    </div>
      </div>


      </div>
    <div class="panel-separator"></div><div class="panel-pane pane-custom pane-2"  >



      <div class="pane-content">
        <style type="text/css">
    <!--/*--><![CDATA[/* ><!--*/

    @media print {
      header{
        display:none;
      }
      div#sidebar {
        display: none;
      }
    }

    /*--><!]]>*/
    </style>  </div>


      </div>
    </div>
      </div>
    </div>
      </div>
    </div>
    <div id="block-dfp-setup-19-publift-sticky-footer" class="block block-dfp-setup-19">


      <div class="content">
        <div data-fuse="21858320168"></div>  </div>
    </div>
    <div id="block-dfp-setup-19-publift-left-ad-gutter" class="block block-dfp-setup-19">


      <div class="content">

              <!-- 2332506/interest_19_ROS_leftgutter/interest_19_ROS_leftgutter -->
              <div data-fuse="21866065070"></div>  </div>
    </div>
    <div id="block-dfp-setup-19-publift-right-ad-gutter" class="block block-dfp-setup-19">


      <div class="content">

            <!-- 2332506/interest_19_ROS_rightgutter/interest_19_ROS_rightgutter -->
            <div data-fuse="21866065073"></div>  </div>
    </div>
    <div id="block-dfp-setup-19-publift-imp-pixel-1" class="block block-dfp-setup-19">


      <div class="content">

            <!-- 2332506/interest_19_impression_pixel_1/interest_19_impression_pixel_1 -->
            <div data-fuse="21878348251"></div>
              </div>
    </div>
    <div id="block-eyeota-tags-home-eyeota-tag" class="block block-eyeota-tags">


      <div class="content">
        <script type="text/javascript" async defer src="https://ps.eyeota.net/pixel?pid=muoi0ru&t=ajs&sid=interest"></script>  </div>
    </div>
    <div id="block-eyeota-tags-saving-eyeota-tag" class="block block-eyeota-tags">


      <div class="content">
        <script type="text/javascript" async defer src="https://ps.eyeota.net/pixel?pid=muoi0ru&t=ajs&sid=interest&cat=saving"></script>  </div>
    </div>
    <div id="block-press-patron-presspatron-donation-campaign" class="block block-press-patron">


      <div class="content">
        <div id="pp-donation-campaign-wrapper" class="rose">
      <div id="pp-close-button" class="pp-donation-close"></div>
      <p> Your access to our unique content is free - always has been. But ad revenues are diving so we need your direct support.</p>
      <p>
        <a href="https://dashboard.presspatron.com/donations/new?frame=1&t=otsLiLFCX82yC86Cnz4DiJa6" id="pp-donation-campaign-button" class="has-button-styles">Become a supporter</a>
      </p>
      <p>
        <a id="pp-close-link" class="pp-donation-close">Thanks, I'm already a supporter.</a>
      </p>
    </div>
      </div>
    </div>
      </div>
              </div>
            </div>

            <div id="sidebar-wrapper">
              <div id="sidebar">
                  <div class="region region-sidebar">
        <div id="block-in-this-section-0" class="block block-in-this-section">

        <h2>In this section</h2>

      <div class="content">
        <ul class="menu"><li class="first leaf"><a href="/saving/e-saver-online">E-saver accounts</a></li>
    <li class="leaf active-trail"><a href="/saving/call-account" class="active-trail active">Savings accounts</a></li>
    <li class="leaf"><a href="/saving/bonus-savings-accounts">Bonus Savings Accounts</a></li>
    #039;s Accounts</a></li>
    <li class="leaf"><a href="/saving/children-youth-student">Children&
    <li class="leaf"><a href="/saving/business-savings-accounts">Business Savings </a></li>
    <li class="leaf"><a href="/saving/term-deposits-1-to-9-months">Term deposits &lt; 1 year</a></li>
    <li class="leaf"><a href="/saving/term-deposits-1-to-5-years">Term deposits 1 to 5 years</a></li>
    <li class="leaf"><a href="/saving/cash-pie">Cash PIEs</a></li>
    <li class="leaf"><a href="/saving/term-pie">Term PIEs</a></li>
    <li class="leaf"><a href="/bonds-data/issues">Moneymarket</a></li>
    <li class="collapsed"><a href="/saving/account-fees/standard-cheque-account-fees">Account fees</a></li>
    <li class="leaf"><a href="/credit-ratings-explained">Credit ratings explained</a></li>
    <li class="leaf"><a href="/saving/interest-codes">Interest codes</a></li>
    <li class="leaf"><a href="/saving/market-platform" title="">Private investments</a></li>
    <li class="leaf"><a href="/saving/international-investors-faqs">International investors</a></li>
    <li class="leaf"><a href="/saving/deep-freeze-list">Deep Freeze</a></li>
    <li class="leaf"><a href="/saving/bank-leverage">Bank leverage</a></li>
    <li class="last leaf"><a href="/news/emails-newsletters-sign-up" title="">Sign up for emails</a></li>
    </ul>  </div>
    </div>
    <div id="block-dfp-setup-19-interest-19-pos1-mrec" class="block block-dfp-setup-19">


      <div class="content">
        <!-- 2332506/interest_19_POS1_MREC/interest_19_POS1_MREC -->
            <div data-fuse="21850843986"></div>  </div>
    </div>
    <div id="block-dfp-setup-19-interest-19-pos2-mrec" class="block block-dfp-setup-19">


      <div class="content">
        <!-- 2332506/interest_19_POS2_MREC/interest_19_POS2_MREC -->
            <div data-fuse="21850843992"></div>  </div>
    </div>
      </div>
              </div>
            </div>

          </div> <!-- /#main-content-container -->

        </div> <!-- /#content -->

      </div> <!-- /#page -->
    </div> <!-- /#page-wrapper -->  <script type="text/javascript" src="https://www.interest.co.nz/sites/default/files/js/js_buXG3r8iLS7RFtegCzOFRGoTUMN5W9EhHmNhO62eVts.js"></script>
      <div id="burger-nav">
        <div class="gcse-wrapper">

      <script>
        (function() {
          var cx = '013234808727065659026:_n8ackc_blq';
          var gcse = document.createElement('script');
          gcse.type = 'text/javascript';
          gcse.async = true;
          gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(gcse, s);
        })();
      </script>
      <gcse:search></gcse:search>
          </div>
        <div id="burger-close"></div>
    <div class="clearfix"></div>
    <div id="burger-container">
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/home">Home </a>
            <a class="burger-parent-ct white-font" id="burger-parent-0"> > </a>
          </div>
        <div id="burger-child-0" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/podcasts"  > Podcast - subscribe here </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/news">News </a>
            <a class="burger-parent-ct white-font" id="burger-parent-1"> > </a>
          </div>
        <div id="burger-child-1" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/economic-calendar"  > Economic calendar </a>
              <a class="burger-child-link white-font" href="/news/2020-economic-rescue-package"  > The crisis rescue package tally </a>
              <a class="burger-child-link white-font" href="/news/82573/reserve-bank-lays-out-detail-how-it-reviews-our-monetary-policy-settings-and-processes"  > How the OCR is set </a>
              <a class="burger-child-link white-font" href="/category/tag/tppa"  > TPPA explainer series </a>
              <a class="burger-child-link white-font" href="/saving/bank-financial-comparator"  > Key bank metrics </a>
              <a class="burger-child-link white-font" href="/news/105115/budget-202021-summary-all-spending-plans"  > Budget 2020/21 - Spending plan </a>
              <a class="burger-child-link white-font" href="/news/105190/budget-2020-summary-all-tax-collections"  > Budget 2020/21 - Tax revenue </a>
              <a class="burger-child-link white-font" href="/news/102724/we-update-nations-economic-benchmarks-second-time-one-after-year-delivery-overall-there"  > New Govt. benchmarks </a>
              <a class="burger-child-link white-font" href="/opinion/94342/media-world-changing-challenging-readers-who-expect independent-news-data-and-comment"  > Become a Supporter </a>
              <a class="burger-child-link white-font" href="/podcasts"  > Podcast - subscribe here </a>
              <a class="burger-child-link white-font" href="https://www.interest.co.nz/gdp-live" target="_blank" > GDP Live </a>
              <a class="burger-child-link white-font" href="/news/emails-newsletters-sign-up"  > Sign up for our free newsletters </a>
              <a class="burger-child-link white-font" href="/paid-newsletter/37138"  > Banking newsletter subscription </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/property">Property </a>
            <a class="burger-parent-ct white-font" id="burger-parent-2"> > </a>
          </div>
        <div id="burger-child-2" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/property/residential-auction-results"  > Residential auction results </a>
              <a class="burger-child-link white-font" href="/property/commercial-property-sales"  > Commercial property sales </a>
              <a class="burger-child-link white-font" href="/property/rural-farm-property-sales"  > Farms sold </a>
              <a class="burger-child-link white-font" href="/property/90395/we-release-new-set-visualisations-showing-how-seven-our-cities-have-grown-over-time"  > 'Sprawl' visualisations </a>
              <a class="burger-child-link white-font" href="https://www.interest.co.nz/property/105655/house-prices-bottom-end-market-have-declined-73-their-march-peak-while-mortgage" target="_blank" > Home loan affordability </a>
              <a class="burger-child-link white-font" href="/property/house-price-income-multiples"  > Median multiples </a>
              <a class="burger-child-link white-font" href="/calculators/mortgage-calculator"  > Mortgage calculator </a>
              <a class="burger-child-link white-font" href="/calculators/mortgage-break-fee-estimator"  > Break fee calculator </a>
              <a class="burger-child-link white-font" href="/saving/rental-yield-indicator"  > Rental yield indicator </a>
              <a class="burger-child-link white-font" href="/property/rent-ratio"  > Rent ratio </a>
              <a class="burger-child-link white-font" href="/property/commercial-property-for-sale"  > Commercial property for sale </a>
              <a class="burger-child-link white-font" href="/property/lifestyle-blocks"  > Lifestyle blocks for sale </a>
              <a class="burger-child-link white-font" href="https://www.interest.co.nz/news/emails-newsletters-sign-up" target="_blank" > Sign up for our free Property newsletter </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/borrowing">Borrowing </a>
            <a class="burger-parent-ct white-font" id="burger-parent-3"> > </a>
          </div>
        <div id="burger-child-3" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/borrowing"  > Mortgage rates </a>
              <a class="burger-child-link white-font" href="/calculators/mortgage-calculator"  > - Mortgage calculator </a>
              <a class="burger-child-link white-font" href="/calculators/mortgage-break-fee-estimator"  > - Break fee calculator </a>
              <a class="burger-child-link white-font" href="/personal-finance/101570/moneyhubs-christopher-walsh-digs-deep-reverse-mortgages-what-they-are-their"  > Reverse mortgage FAQ </a>
              <a class="burger-child-link white-font" href="/borrowing/revolving-credit"  > Revolving credit </a>
              <a class="burger-child-link white-font" href="/borrowing/car-loan"  > Car loans </a>
              <a class="burger-child-link white-font" href="/borrowing/credit-cards"  > Credit cards </a>
              <a class="burger-child-link white-font" href="/borrowing/personal-loan"  > Personal loans </a>
              <a class="burger-child-link white-font" href="/borrowing/business-base-rates"  > Business loan rates </a>
              <a class="burger-child-link white-font" href="/calculators/55377/should-you-fix-or-stay-floating"  > Fix or Float calculator </a>
              <a class="burger-child-link white-font" href="/property/rent-or-buy"  > Rent or Buy ? </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/saving/term-deposits-1-to-5-years">Saving </a>
            <a class="burger-parent-ct white-font" id="burger-parent-4"> > </a>
          </div>
        <div id="burger-child-4" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/saving/call-account"  > Savings accounts </a>
              <a class="burger-child-link white-font" href="/saving/bonus-savings-accounts"  > Bonus savings accounts </a>
              <a class="burger-child-link white-font" href="/saving/term-deposits-1-to-9-months"  > Term deposits < 1 yr </a>
              <a class="burger-child-link white-font" href="/saving/term-deposits-1-to-5-years"  > Term deposits 1 - 5 years </a>
              <a class="burger-child-link white-font" href="/saving/term-pie"  > Term PIEs </a>
              <a class="burger-child-link white-font" href="/calculators/deposit-calculator"  > Deposit calculator </a>
              <a class="burger-child-link white-font" href="/saving/interest-codes"  > Interest codes </a>
              <a class="burger-child-link white-font" href="/credit-ratings-explained"  > Credit ratings explained </a>
              <a class="burger-child-link white-font" href="/saving/market-platform"  > Private market </a>
              <a class="burger-child-link white-font" href="/saving/bank-leverage"  > Bank leverage </a>
              <a class="burger-child-link white-font" href="/saving/deep-freeze-list"  > Deep Freeze list </a>
              <a class="burger-child-link white-font" href="/saving/porridge-list"  > Porridge list </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/kiwisaver">Kiwisaver </a>
            <a class="burger-parent-ct white-font" id="burger-parent-5"> > </a>
          </div>
        <div id="burger-child-5" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/kiwisaver/funds"  > Find your fund </a>
              <a class="burger-child-link white-font" href="/kiwisaver/fund-comparison-table"  > Compare fund categories </a>
              <a class="burger-child-link white-font" href="/kiwisaver/calculators"  > Calculators </a>
              <a class="burger-child-link white-font" href="/kiwisaver"  > KiwiSaver news </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/banking">Banking </a>
            <a class="burger-parent-ct white-font" id="burger-parent-6"> > </a>
          </div>
        <div id="burger-child-6" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/saving/bank-leverage"  > Bank leverage </a>
              <a class="burger-child-link white-font" href="/credit-ratings-explained"  > Credit ratings explained </a>
              <a class="burger-child-link white-font" href="/saving/bank-financial-comparator"  > Key bank metrics </a>
              <a class="burger-child-link white-font" href="/news/82573/reserve-bank-lays-out-detail-how-it-reviews-our-monetary-policy-settings-and-processes"  > How the OCR is set </a>
              <a class="burger-child-link white-font" href="/opinion/77033/overview-functions-money-and-how-money-and-credit-are-created-nz-economy-examining"  > How money is created </a>
              <a class="burger-child-link white-font" href="/bonds/64411/if-bank-failed-and-open-bank-resolution-policy-was-implemented-how-would-it-affect-bank"  > How OBR will work </a>
              <a class="burger-child-link white-font" href="https://www.rbnz.govt.nz/monetary-policy/unconventional-monetary-policy" target="_blank" > About unconventional monetary policy </a>
              <a class="burger-child-link white-font" href="/borrowing"  > Mortgage interest rates </a>
              <a class="burger-child-link white-font" href="/saving/term-deposits-1-to-5-years"  > Term deposit interest rates </a>
              <a class="burger-child-link white-font" href="/category/topic/little-book-scams"  > Scams - how to protect yourself </a>
              <a class="burger-child-link white-font" href="/paid-newsletter/37138"  > Subscribe to industry newsletter </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/insurance">Insurance </a>
            <a class="burger-parent-ct white-font" id="burger-parent-7"> > </a>
          </div>
        <div id="burger-child-7" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/insurance-data/car-insurance-compared-january-2018"  > Car insurance - 2018 </a>
              <a class="burger-child-link white-font" href="/category/tag/house-insurance"  > House cover </a>
              <a class="burger-child-link white-font" href="/category/tag/climate-change"  > Climate change </a>
              <a class="burger-child-link white-font" href="http://www.icnz.org.nz/statistics-data/industry-data/" target="_blank" > Industry stats </a>
              <a class="burger-child-link white-font" href="/users/andrew-hooker"  > Andrew Hooker columns </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/personal-finance">Personal </a>
            <a class="burger-parent-ct white-font" id="burger-parent-8"> > </a>
          </div>
        <div id="burger-child-8" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/borrowing"  > Mortgage interest rates </a>
              <a class="burger-child-link white-font" href="/personal-finance/101570/moneyhubs-christopher-walsh-digs-deep-reverse-mortgages-what-they-are-their"  > Reverse mortgages </a>
              <a class="burger-child-link white-font" href="/saving/term-deposits-1-to-5-years"  > Term deposit interest rates </a>
              <a class="burger-child-link white-font" href="/category/tag/credit-cards"  > Credit cards </a>
              <a class="burger-child-link white-font" href="/calculators"  > Calculators </a>
              <a class="burger-child-link white-font" href="/saving/market-platform"  > Private investments </a>
              <a class="burger-child-link white-font" href="/kiwisaver"  > KiwiSaver </a>
              <a class="burger-child-link white-font" href="/saving/gold-spot"  > Gold & silver prices </a>
              <a class="burger-child-link white-font" href="/saving/gold-coins"  > - Gold coin prices </a>
              <a class="burger-child-link white-font" href="/saving/gold-bars"  > - Gold bar prices </a>
              <a class="burger-child-link white-font" href="/saving/scrap-metals"  > - Precious metal scrap prices </a>
              <a class="burger-child-link white-font" href="/category/topic/little-book-scams"  > Protection from scams </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/rural">Rural </a>
            <a class="burger-parent-ct white-font" id="burger-parent-9"> > </a>
          </div>
        <div id="burger-child-9" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/rural/beef/bull-m2"  > Bull prices </a>
              <a class="burger-child-link white-font" href="/rural/beef/steer-p2"  > Steer & heifer prices </a>
              <a class="burger-child-link white-font" href="/rural/beef/heifer-localtrade"  > Beef local trade prices </a>
              <a class="burger-child-link white-font" href="/rural/beef/cow-prime"  > Cow prices </a>
              <a class="burger-child-link white-font" href="/rural/sheep/lamb-y"  > Lamb prices </a>
              <a class="burger-child-link white-font" href="/rural/sheep/lamb-localtrade"  > Local trade lamb prices </a>
              <a class="burger-child-link white-font" href="/rural/sheep/wool"  > Wool prices </a>
              <a class="burger-child-link white-font" href="/rural-data/dairy-industry-payout-history"  > Dairy payout history </a>
              <a class="burger-child-link white-font" href="/rural/logs"  > Logs </a>
              <a class="burger-child-link white-font" href="/rural-news/farms-for-sale"  > Farms for sale </a>
              <a class="burger-child-link white-font" href="/rural"  > All other rural links to data </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/currencies">Currencies </a>
            <a class="burger-parent-ct white-font" id="burger-parent-10"> > </a>
          </div>
        <div id="burger-child-10" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/currencies/buying-foreign-currency"  > Live rates for buying fx </a>
              <a class="burger-child-link white-font" href="/currencies/selling-foreign-currency-transfers"  > Live rates to sell TT fx </a>
              <a class="burger-child-link white-font" href="/currencies/currency-conversion-fees"  > Currency fees </a>
              <a class="burger-child-link white-font" href="/currencies/rate-pricing"  > Rate pricing </a>
              <a class="burger-child-link white-font" href="/currencies/spot-rates"  > Spot transactions </a>
              <a class="burger-child-link white-font" href="/currencies/forward-rates"  > Forward transactions </a>
              <a class="burger-child-link white-font" href="/currencies/how-currency-swaps-work"  > Currency swaps </a>
              <a class="burger-child-link white-font" href="/currencies/how-to-do-currency-deals-with-hifx"  > How to do currency deals </a>
              <a class="burger-child-link white-font" href="/currencies/currency-directory"  > Directory - where to buy/sell </a>
              <a class="burger-child-link white-font" href="/currencies/subscribe_to_newsletter"  > Daily fx rate sheet email </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/charts">Charts </a>
            <a class="burger-parent-ct white-font" id="burger-parent-11"> > </a>
          </div>
        <div id="burger-child-11" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/charts/commodities"  > Commodities </a>
              <a class="burger-child-link white-font" href="/charts/confidence"  > Confidence </a>
              <a class="burger-child-link white-font" href="/charts/credit"  > Debt (Credit) </a>
              <a class="burger-child-link white-font" href="/charts/economy"  > Economy </a>
              <a class="burger-child-link white-font" href="/charts/exchange rates"  > Exchange rates </a>
              <a class="burger-child-link white-font" href="/charts/interest rates"  > Interest rates </a>
              <a class="burger-child-link white-font" href="/charts/population"  > Population </a>
              <a class="burger-child-link white-font" href="/charts/prices"  > Prices </a>
              <a class="burger-child-link white-font" href="/charts/real estate"  > Real estate </a>
              <a class="burger-child-link white-font" href="/charts/rural"  > Rural </a>
              <a class="burger-child-link white-font" href="/charts"  > Full list of all charts </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/calculators">Calculators </a>
            <a class="burger-parent-ct white-font" id="burger-parent-12"> > </a>
          </div>
        <div id="burger-child-12" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/calculators/deposit-calculator"  > Deposit calculator </a>
              <a class="burger-child-link white-font" href="/calculators/mortgage-calculator"  > Mortgage calculator </a>
              <a class="burger-child-link white-font" href="/calculators/borrowing-capacity-calculator"  > How much can you bid? </a>
              <a class="burger-child-link white-font" href="/calculators/full-function-mortgage-calculator"  > Full-function mortgage calculator </a>
              <a class="burger-child-link white-font" href="/calculators/lvr-borrowing-capacity-calculator"  > LVR borrowing capacity </a>
              <a class="burger-child-link white-font" href="/calculators/property-upsize-downsize-calculator"  > Property upsize/downsize </a>
              <a class="burger-child-link white-font" href="/calculators/principal-payback-milestone-calculator"  > Principal payback milestone </a>
              <a class="burger-child-link white-font" href="/calculators/mortgage-break-fee-estimator"  > Break fee calculator </a>
              <a class="burger-child-link white-font" href="/calculators/55377/should-you-fix-or-stay-floating"  > Fix or float calculator </a>
              <a class="burger-child-link white-font" href="/calculators/credit-card-minimum-payments"  > Credit card real cost </a>
              <a class="burger-child-link white-font" href="/calculators/cost-of-credit-calculator"  > Real cost of debt </a>
              <a class="burger-child-link white-font" href="/calculators/retirement-calculator"  > Retirement calculator </a>
              <a class="burger-child-link white-font" href="/calculators/foreign-currency-calculator"  > Buying foreign currency </a>
              <a class="burger-child-link white-font" href="/calculators"  > All our calculators </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/bonds">Bonds </a>
            <a class="burger-parent-ct white-font" id="burger-parent-13"> > </a>
          </div>
        <div id="burger-child-13" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/bonds-data/issues"  > Current prices </a>
              <a class="burger-child-link white-font" href="/bonds/how-to-read-these-pages"  > How to use our bonds resource </a>
              <a class="burger-child-link white-font" href="/bonds/how-to-buy-bonds"  > How to buy bonds </a>
              <a class="burger-child-link white-font" href="/bonds/bond-types"  > Bond types </a>
              <a class="burger-child-link white-font" href="/bonds/glossary"  > Glossary </a>
              <a class="burger-child-link white-font" href="/charts/interest-rates/government-bond-rates"  > NZ Govt bond rates </a>
              <a class="burger-child-link white-font" href="/charts/interest-rates/us-treasures"  > US Treasury bond rates </a>
          </div>
        <div class="burger-parent-wrapper">
        <a class="burger-parent-link white-font" href="/business">Business </a>
            <a class="burger-parent-ct white-font" id="burger-parent-14"> > </a>
          </div>
        <div id="burger-child-14" class="burger-child-wrapper" >
        <div class="burger-child-back white-font"> back </div>
              <a class="burger-child-link white-font" href="/borrowing/business-base-rates"  > Business borrowing rates </a>
              <a class="burger-child-link white-font" href="/understanding-china"  > Understanding China </a>
              <a class="burger-child-link white-font" href="/understanding-china"  > - by Professor Ang and guests </a>
              <a class="burger-child-link white-font" href="/category/tag/tppa"  > TPPA explainer series </a>
              <a class="burger-child-link white-font" href="/business/how-to-guides"  > How to guides: </a>
              <a class="burger-child-link white-font" href="/business/60438/we-are-starting-new-13-part-guide-small-business-managers-who-want-achieve-financial"  > - Achieving financial success </a>
              <a class="burger-child-link white-font" href="/business/60243/first-ten-part-guide-series-how-tackle-often-complex-challenges-companies-face-when"  > - The realities of growth </a>
              <a class="burger-child-link white-font" href="/category/tag/success-stories"  > Success stories </a>
              <a class="burger-child-link white-font" href="https://www.interest.co.nz/gdp-live" target="_blank" > GDP Live </a>
          </div>
      </div>
      </div>

      <footer>
        <div id = "footer-wrapper">
          <div id="footer-logo"><a href="/"></a></div>
          <div id="footer-links-1">
            <a href="/about-us">About</a>
            <a href="/feedback">Contact us</a>
          </div>
          <div id="footer-links-2">
            <a href="/about-us">About</a>
            <a href="/feedback">Contact us</a>
            <a href="/sitemap">Sitemap</a>
            <a href="/terms-conditions">Terms and Conditions</a>
            <a href="/privacy">Privacy</a>
            <a href="/advertise">Advertise</a>
          </div>
          <div id="copyright" class="white-font">
            <span>&copy; 2020 interest.co.nz</span>
            <span id="calculate-partnership"><a href="https://www.interest.co.nz">interest.co.nz</a> is partnered with <a target="_blank" href="https://www.calculate.co.nz">Calculate.co.nz</a> for New Zealand's highest quality calculators and analysis.</span>
          </div>
        </div>
      </footer>
    </body>
    </html>
    """
