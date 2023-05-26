WEBSITE_LIST = {
    "https://www.youtube.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "login-page":   'direct-link;signin',
                  "video":  'css selector;ytd-rich-item-renderer'
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{"trending":'relies_prev:partial link text;Trending',
                                   "music":   'relies_prev:partial link text;Music',
                                   "gaming":  'relies_prev:partial link text;Gaming',
                                   "news":    'relies_prev:partial link text;News',
                                   "sports":  'relies_prev:partial link text;Sports',
                                   "learning":'relies_prev:partial link text;Learning'
                                   },
                      "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                  },
                      "music":{"video":'rand_ind:css selector;ytd-video-renderer'
                               },
                      "gaming":{"video":'rand_ind:css selector;ytd-video-renderer'
                          
                      },
                  }
                },  
                # Website : pcGamer Problem with this website , need to move the mouse
                "https://www.pcgamer.com/": {
                "specifics": "Problem with this website , need to move the mouse for the popup to appear",
                "endpoints": {
                "Popup_close": 'class name;exit-intent__close-button'
                },
                "sub-endpoints": {
                "main_menu": {
                    "news": 'partial link text;news',
                    "reviews": 'partial link text;reviews',
                    "hardware": 'partial link text;hardware',
                    "BestOf": 'partial link text;best-of',
                    "top100": 'partial link text;the-top-100-pc-games-2022'
                },
             "hardware": {
                "hardware": 'rand_ind:class name;listingresult'
            }
        }
    },
    "https://apache.org/": # Website : Apache
                {"specifics":"ablock=true;",
                 "endpoints":
                 {
                     "about":'refresh_sens:partial link text;About',
                     "donation":'refresh_sens:partial link text;Make a Donation',
                     "theApacheWay":'refresh_sens:partial link text;The Apache Way',
                     "joinUs":'refresh_sens:partial link text;Join Us',
                     "downaloads":'refresh_sens:partial link text;downloads',
                     "projects":'refresh_sens:partial link text;Projects',
                     "people":'refresh_sens:partial link text;People',
                     "community":'refresh_sens:partial link text;Community',
                     "secondInfrast":'refresh_sens:partial link text;Insfrastructure',
                     "sponsors":'refresh_sens:partial link text;Sponsors',
                     "license":'refresh_sens:partial link text;License'
                     

                 },
                  "sub-endpoints":
                  {
                      "about":{
                                "overview":'relies_prev:partial link text;Overview',
                                "process":'relies_prev: partial link text;Process',
                                "governance":'relies_prev: partial link text;Governance',
                                "theapache":'relies_prev: partial link text;The Apache Way',
                                "membership":'relies_prev: partial link text;Membership',
                                "community":'relies_prev: partial link text;Community',
                                "diversity":'relies_prev: partial link text;Diversity & Inclusion',
                                "codeofconduct":'relies_prev: partial link text;Code of Conduct',
                                "glossary":'relies_prev: partial link text;Glossary',
                                "aboutourname":'relies_prev: partial link text;About Our Name',
                                "faq":'relies_prev: partial link text;FAQ',
                                "supportappache":'relies_prev: partial link text;Media/Analysts',
                                "media":'relies_prev: partial link text;Contact',
                                "contact":'relies_prev: partial link text;Support Apache'
                            },
                    "Donation":{
                     "donateNow": {
                                    "donateNow":'relies_prev: partial link text;Donate Now',
                                    "viaAch":'relies_prev: partial link text;Via ACH',
                                    "viaPaypal":'relies_prev: partial link text;Via Paypal',
                                    "creditCard":'relies_prev: partial link text;Via Credit Card',
                                },
                                "buySwag":'relies_prev: partial link text;Buy Swag', 
                                "AsfSponsorship":'relies_prev: partial link text;ASF Sponsorship',
                                "targetedSposor":'relies_prev: partial link text;Targeted Sponsorship',
                                "CorporateGiving":'relies_prev: partial link text;Corporate Giving',

                     "theApacheWay":{
                                    "sustainOpenSourc":'relies_prev: partial link text;Sustainable Open Source',
                                    "howItWorks":'relies_prev: partial link text;How it Works',
                                    "Merit":'relies_prev:partial link text;Merit',
                                    "theapachewaysub":'direct-link;theapacheway',
                                    "Success at Apache":'relies_prev: partial link text;Success at Apache'
                         
                                    },
                     "joinUs":{"gettingStarted":'relies_prev: partial link text;Getting Started',
                               "helpWanted":'relies_prev: partial link text;Help Wanted',
                               "ApacheCon":'relies_prev: partial link text;ApacheCon', 
                               "comEvents":'relies_prev: partial link text;Community Events',
                               "travelAssistance":'relies_prev: partial link text;Travel Assistance',
                               "summerOfCode":'relies_prev: partial link text;Summer of Code',
                               "etiquette":'relies_prev: partial link text;Etiquette'  
                               },
                     "downloads":{"distribution":'relies_prev:partial link text;Distribution',
                                  "releases":'relies_prev:partial link text;Releases',
                                  "infrastStatus":'relies_prev: partial link text;Infrastructure Status',
                                  "infrastStatistics":'relies_prev: partial link text;Infrastructure Statistics'
                         
                     },
                     "projects":{
                                 "projectList":'relies_prev:partial link text;Project List',
                                 "howThetWork": 'relies_prev:partial link text;How they work',
                                 "independence": 'relies_prev:partial link text;Independence',
                                 "dateFounded": 'relies_prev:partial link text;Date Founded',
                                 "names": 'relies_prev:partial link text;Names',
                                 "categories": 'relies_prev:partial link text;Categories',
                                 "languages": 'relies_prev:partial link text;Languages',
                                 "statistics": 'relies_prev:partial link text;Statistics',
                                 "apacheIncub": 'relies_prev:partial link text;Apache Incubator',
                                 "helpWanted": 'relies_prev:partial link text;Help Wanted',
                                 "brandManag": 'relies_prev:partial link text;Brand Management',
                                 "glossaryOfTherms": 'relies_prev:partial link text;Glossary of Terms',         
                     },
                     # select on the project endoint - new sub-endpoint to subdomain-name :projects.apache.org 
                     "projectList":{"overviewProject":'ind_1:css selector;ul.list-unstyled:nth-of-type(1) li a'},
                     "people":{
                                    "roles":'relies_prev: partial link text;Roles',
                                    "members":'relies_prev: partial link text;Members',
                                    "committers":'relies_prev: partial link text;Committers',
                                    "boardOfDir":'relies_prev: partial link text;Board of Directors',
                                    "offiersProject":'relies_prev: partial link text;Offiers & Project VPs',
                                    "diversityInclusion":'relies_prev: partial link text;Diversity & Inclusion',
                                    "codeOfCOnduct":'relies_prev: partial link text;Code of Conduct',
                                    "committerDir":'relies_prev: partial link text;Committer Directory',
                                    "HeatMap":'relies_prev: partial link text;Heat Map',
                     },
                     "community":{
                         "commDev":'relies_prev: partial link text;Community Development',
                         "codeOfConduct":'relies_prev: partial link text;Code of Conduct',
                         "getInvol":'relies_prev: partial link text;Get Involved',
                         "mentoring":'relies_prev: partial link text;Mentoring',
                         "helpWanted":'relies_prev: partial link text;Help Wanted',
                         "commEvents":'relies_prev: partial link text;Community Events',
                         "faq":'relies_prev: partial link text;FAQ',
                         "mailingList":'relies_prev: partial link text;Mailing Lists',
                     },
                     "infrastructure":{
                         "infOver":'relies_prev: partial link text;Infra overview',
                         "polAndTool":'relies_prev: partial link text;Policiers and Tools',
                         "cwiki":'relies_prev: partial link text;CWiki',
                         
                     },
                     "license":{
                         "apacheLicense":'relies_prev: partial link text;Apache License 2.0',
                         "licensFaq":'relies_prev: partial link text;Licensing FAQ',
                         "contribLiAgre":'relies_prev: partial link text;Contributor License Agreements',
                         "softwGrant":'relies_prev: partial link text;Software Grants',
                         "tradeMark":'relies_prev: partial link text;Trademarks',
                         "exports":'relies_prev: partial link text;Exports',
                         
                     },
                      "sponsors":{
                         "sponTheAsf":'relies_prev: partial link text;Sponsor the ASF',
                         "sponThanks":'relies_prev: partial link text;Sponsor thanks',
                         "corporateGiv":'relies_prev: partial link text;Corporate Giving',
                         "indivDonations":'relies_prev: partial link text;Individual Donations',
                         "buyStuff":'relies_prev: partial link text;Buy Stuff'
                     }
               
                 }
                }
                },# Website : The atlantic
                "https://www.theatlantic.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:class name;NavHamburgerButton_box__Sq9Ip',
                 "endpoints":
                 { 
                  "popular":'refresh_sens:partial link text;Popular',
                  "latest": 'refresh_sens:partial link text;Latest',
                  "newsletters":'refresh_sens:partial link text;Newsletters',
                  "login":'refresh_sens:partial link text;Sign In',
                  "subscribe":'refresh_sens:partial link text;Subscribe'
                },
                  "sub-endpoints":
                  {
                      "main_menu":{
                          "politics":'relies_prev: partial link text;Politics',
                          "technology":'relies_prev: partial link text;Technology',
                          "business":'relies_prev: partial link text;Business',
                          "global":'relies_prev: partial link text;Global',
                          "health":'relies_prev: partial link text;Business',
                          "features":'relies_prev: partial link text;Features',
                          "shadowland":'relies_prev: partial link text;Shadowland',
                          "ideas":'relies_prev: partial link text;Ideas',
                          "science":'relies_prev: partial link text;Science',
                          "culture":'relies_prev: partial link text;Culture',
                          "books":'relies_prev: partial link text;Books',
                          "education":'relies_prev: partial link text;Education',
                          "family":'relies_prev: partial link text;Family',
                          "progress":'relies_prev: partial link text;Progress',
                          "fiction":'relies_prev: partial link text;Fiction',
                          "photo":'relies_prev: partial link text;Photo',
                          "planet":'relies_prev: partial link text;Planet',
                          "podcast":'relies_prev: partial link text;Podcasts',
                          "projects":'relies_prev: partial link text;Projects',
                          "events":'relies_prev: partial link text;Events',
                          "explArchive":'relies_prev: partial link text;Explore The Atlantic Archive',
                          "playCrossword":'relies_prev: partial link text;Play The Atlantic crossword',
                          "latestIssue":'relies_prev: partial link text;Latest Issue',
                          "pastIssue":'relies_prev: partial link text;Past Issues',
                          "giveGift":'relies_prev: partial link text;Give a Gift',  
                      },

                      "politics":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "technology":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "business":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "global":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "health":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "features":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "shadowland":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "ideas":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "science":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "culture":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "books":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "education":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "family":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "progress":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "fiction":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "photo":{"article":'relies_prev~rand_ind:class name;article'},
                      "podcast":{"article":'relies_prev~rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      #"events":{"article":'rand_ind:class name;LandingRiver_promoItem__LuiRv'},
                      "explArchive":{"issue":'relies_prev~rand_ind:css selector;ul.MagazineDecadeCarousel_carousel__DE0j_ a'},
                      #"playCrossword":{"puzzle":'rand_ind:css selector;ul.crossList li a"}
                     "latestIssue":{"issue":'relies_prev~rand_ind:css selector;ul.MagazineDecadeCarousel_carousel__DE0j_ a'},
                     "pastIssue":{"issue":'relies_prev~rand_ind:css selector;a.BackIssuesGrid_item__b4V1e'}

                  }
                },
                #Website : wayfair.com / Blocage / Captcha
                 "https://www.wayfair.com/":
                {"specifics":"Captcha - no impact for clic executing javascript",
                 "main_menu":'refresh_sens:class name;_1ihiofm0',
                 "endpoints":
                 { 
                  "login-page": 'class name;_15h04s00',#ask to verify , Captcha                  
                 
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{"departements":'relies_prev: partial link text;Departement' #ask to verify , Captcha
                  },
                    "department":'rand_id:css selector;.jgOtFB a',
                    "furniture":'refresh_sens~ind_1:css selector;ul._1vzvuld1 li',
                    "bedding":'refresh_sens~ind_2:css selector;ul._1vzvuld1 li',
                    "rugs":'refresh_sens~ind_3:css selector;ul._1vzvuld1 li',
                    "decor":'refresh_sens~ind_4:css selector;ul._1vzvuld1 li',
                    "organization":'refresh_sens~ind_5:css selector;ul._1vzvuld1 li',
                    "ligthing":'refresh_sens~ind_6:css selector;ul._1vzvuld1 li',
                    "kitchen":'refresh_sens~ind_7:css selector;ul._1vzvuld1 li',
                    "baby":'refresh_sens~ind_8:css selector;ul._1vzvuld1 li',
                    "homeimprov":'refresh_sens~ind_9:css selector;ul._1vzvuld1 li',
                    "appliance":'refresh_sens~ind_10:css selector;ul._1vzvuld1 li',
                    "pet":'refresh_sens~ind_11:css selector;ul._1vzvuld1 li',
                    "holiday":'refresh_sens~ind_12:css selector;ul._1vzvuld1 li',
                },
                "furniture":{
                    "living_room":'relies_prev~ind_1:css selector;div.blhUVp li ul li'
                }

                },
                 #Website : ancestry.com
                 "https://www.ancestry.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "login-page":'refresh_sens:partial link text;LOG IN',
                  "genealogy":'refresh_sens:partial link text;GENEALOGY',
                  "dna":'refresh_sens:partial link text;DNA',
                  "freetrial":'refresh_sens:partial link text;FREE TRIAL',
                  "espagnol":'refresh_sens:partial link text;ES'

                 
                 },
                  "sub-endpoints":
                  {
                      "genealogy":{"trees":'relies_prev: partial link text;Trees',
                                   "search":'relies_prev: partial link text;Search',
                                   "dna":'relies_prev: partial link text;DNA',
                                   "explore":'relies_prev: partial link text;Explore',
                                   "help":'relies_prev: partial link text;Help',
                                   "extras":'relies_prev: partial link text;Extras',
                                   "subscribe":'relies_prev: partial link text;Subscribe'
                  }, 
                  "trees":{"familyhistory":'reliews_prev:partial link text;Family History Learning Hub',
                           "uploadgedcom":'reliews_prev:partial link text;Upload a GEDCOM ',}
                },
                  "search":{"allcollections":'reliews_prev:partial link text;All Collections ',
                            "censusvoter":'reliews_prev:partial link text;Census & Voter Lists ',
                            "birthmarriagedeath":'reliews_prev:partial link text;Birth, Marriage & Death ',
                            "immigration":'reliews_prev:partial link text;Immigration & Travel ',
                            "publicmember":'reliews_prev:partial link text;Public Member Trees ',
                            "military":'reliews_prev:partial link text;Military',
                            "cardcatalog":'reliews_prev:partial link text;Card Catalog',
                            "membersearch":'reliews_prev:partial link text;Member Search', 
                  },
                   "dna":{"ancestrydna":'reliews_prev:partial link text;AncestryDNA®',
                            "activatekit":'reliews_prev:partial link text;Activate a Kit',
                            "learninghub":'reliews_prev:partial link text;AncestryDNA® Learning Hub',
                            "includedinresults":'reliews_prev:partial link text;What’s Included in Your Results',
                            "familydna":'reliews_prev:partial link text;DNA + Family Trees',
                            "howdnaworks":'reliews_prev:partial link text;How AncestryDNA® Works',
                  },
                   "help":{"supportcenter":'reliews_prev:partial link text;Support Center',
                            "community":'reliews_prev:partial link text;Community',
                            "messageboards":'reliews_prev:partial link text;Message Boards',
                            "hireandexpert":'reliews_prev:partial link text;Hire an Expert',
                            "sitestatus":'reliews_prev:partial link text;Site Status',
                  },
                   "extras":{"apps":'reliews_prev:partial link text;iOS & Android Apps',
                            "photobooks":'reliews_prev:partial link text;Photo Books & Posters',
                            "progenealogists":'reliews_prev:partial link text;ProGenealogists',
                            "ancestryacademy":'reliews_prev:partial link text;Ancestry Academy',
                            "gift":'reliews_prev:partial link text;Gift Memberships',
                            "ancestrylab":'reliews_prev:partial link text;Ancestry Lab',
                            "heritagetravel":'reliews_prev:partial link text;Heritage Travel',
                  },

                },
                #Website : Tom's Guide --- Some problems with 2 popups ( delay for the second pop up to appear - longer than what expected for a retry )
                #under certains circonstances - works ---- css selector;button.exit-intent__close-button","id;onesignal-slidedown-cancel-button","class name;menu-item-more","ind_1:css selector;ul.sub-menu li
                  "https://www.tomsguide.com/":
                {"specifics":"Mouse need to be moved for the popup to appear, Two popup - second - delay",
                 "endpoints":
                 { 
                  "bestpicks":'direct-link;best-picks',
                  "news":'direct-link;news',
                  "reviews":'direct-link;reviews',
                  "howtos":'partial link text;how-to',
                  "phones":'partial link text;phones',
                  "streaming":'partial link text;Streaming',
                  "deals":'direct-link;deals',
                  "more":'refresh_sens:class name;menu-item-more'
                  
                 },
                  "sub-endpoints":
                  {
                      "more":{
                          "antivirus":'ind_1:css selector;ul.sub-menu li',
                      },
                 
                  }
                },  
                # Website : java.com --- Iframe at the begining -- driver.switch_to.frame("frame_name") -- then the selector
                "https://www.java.com/":
                {"specifics":"iframe need to be switched driver.switch_to.frame('frame_name');",
                 "endpoints":
                 { 
                  "popupbypass":'class mame;required'
                 },
                  "sub-endpoints":
                  {
                
                 
                  }
                },
                #Huawei.com
                "https://www.huawei.com/":
                {"specifics":"ablock=true;",
                 "endpoints":
                 { 
                  "consumer":'refresh_sens:partial link text;Consumer Products',
                  "business":'refresh_sens:partial link text;Business Products',
                  "support":'refresh_sens:partial link text;Support',
                  "partners":'refresh_sens:partial link text;Partners & Developers',
                  "about":'refresh_sens:partial link text;About Huawei',
                  "login":'partial link text;Log in'
                 },
                  "sub-endpoints":
                  {
                        "consumer":{
                            "smartphone":'relies_prev~ind_1:css selector;ul.row li',
                            "pc":'relies_prev~ind_2:css selector;ul.row li',
                            "tablet":'relies_prev~ind_3:css selector;ul.row li',
                            "wearable":'relies_prev~ind_4:css selector;ul.row li',
                            "audio":'relies_prev~ind_5:css selector;ul.row li',
                            "router":'relies_prev~ind_6:css selector;ul.row li',
                            "emui":'relies_prev~ind_7:css selector;ul.row li',
                            "accessories":'relies_prev~ind_8:css selector;ul.row li',
                            "allproducts":'relies_prev~ind_9:css selector;ul.row li',
                            "consumerwebsite":'relies_prev:partial link text;Consumer Website'
                        },
                        "business":{
                            "carriernetwork":'relies_prev~ind_1:css selector;.col-md-4:nth-of-type(1) ul li a',
                            "enterprisenetworking":'relies_prev~ind_2:css selector;.col-md-4:nth-of-type(1) ul li a',
                            "enterpriseoptical":'relies_prev~ind_3:css selector;.col-md-4:nth-of-type(1) ul li a',
                            "enterprisewireless":'relies_prev~ind_4:css selector;.col-md-4:nth-of-type(1) ul li a',
                            "datastorage":'relies_prev~ind_1:css selector;.col-md-4:nth-of-type(2) ul li a',
                            "ascendcomputing":'relies_prev~ind_2:css selector;.col-md-4:nth-of-type(2) ul li a'
                            #"enterpriseservices":'relies_prev~ind_1:css selector;.col-md-3:nth-of-type(1) ul li a',
                            #"cloudservices":'relies_prev~ind_1:css selector;.col-md-3:nth-of-type(1) ul li a',
                            #"telecom":'relies_prev~ind_1:css selector;.col-md-3:nth-of-type(1) ul li a',
                            #"education":'relies_prev~ind_2:css selector;.col-md-3:nth-of-type(2) ul li a',
                            #"finance":'relies_prev~ind_3:css selector;.col-md-3:nth-of-type(2) ul li a',
                            #"electricpower":'relies_prev~ind_4:css selector;.col-md-3:nth-of-type(2) ul li a',
                            #"manufacturing":'relies_prev~ind_5:css selector;.col-md-3:nth-of-type(2) ul li a',
                            #"airport":'relies_prev~ind_6:css selector;.col-md-3:nth-of-type(2) ul li a',
                            #"urbanrail":'relies_prev~ind_7:css selector;.col-md-3:nth-of-type(2) ul li a',
                            #"seemore":'relies_prev~ind_8:css selector;.col-md-3:nth-of-type(2) ul li a'
                        },
                          "support":{
                                    "findservicecenter":'relies_prev:partial link text;Find Service Center',
                                    "productsupport":'relies_prev:partial link text;Product Support',
                                    "productenviron":'relies_prev:partial link text;Product Environmental Information',
                                    "callus":'relies_prev:partial link text;Call Us',
                                    "emaailus":'relies_prev:partial link text;Email Us',
                        },
                          "partners":{
                              "becompartner":'relies_prev:partial link text;Become Partner',
                              "findpartner":'relies_prev:partial link text;Find a Partner',
                              "technicalcertif":'relies_prev:partial link text;Technical Certification',
                              "becomecustomer":'relies_prev:partial link text;Become Consumer Products Partner',
                              "seemore":'relies_prev:partial link text;See More', 
                        },
                          "about":{
                              "ourcompany":'relies_prev:partial link text;Our Company',
                              "annualreports":'relies_prev:partial link text;Annual Reports',
                              "corporategovernance":'relies_prev:partial link text;Corporate Governance',
                              "executives":'relies_prev:partial link text;Executives',
                              "contactus":'relies_prev:partial link text;Contact Us',
                        },
                  }
                },
                # Website : CBCNEWS.COM
                "https://www.nbcnews.com/":
                {
                "specifics":"ablock=true;",
                 "main_menu":'refres_sens:css selector;div.local.h-h > div > button',
                 "endpoints":
                 { 
                  "whatchnow":'partial link text;Watch Now',
                  "about":'ind_1:css selector;footer ul li a'
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{
                          "usnews":'relies_prev:css selector;li.menu-list-item:nth-of-type(2) a',
                          "politics":'relies_prev:css selector;li.menu-list-item:nth-of-type(3) a',
                          "world":'relies_prev:css selector;li.menu-list-item:nth-of-type(4) a',
                          "local":'relies_prev:css selector;li.menu-list-item:nth-of-type(5) a',
                          "business":'relies_prev:css selector;li.menu-list-item:nth-of-type(6) a',
                          "health":'relies_prev:css selector;li.menu-list-item:nth-of-type(7) a',
                          "investigations":'relies_prev:css selector;li.menu-list-item:nth-of-type(8) a',
                          "cultures":'relies_prev:css selector;li.menu-list-item:nth-of-type(9) a',
                          "science":'relies_prev:css selector;li.menu-list-item:nth-of-type(10) a',
                          "sports":'relies_prev:css selector;li.menu-list-item:nth-of-type(11) a',
                          "tech":'relies_prev:css selector;li.menu-list-item:nth-of-type(12) a',
                          "videos":'relies_prev:css selector;li.menu-list-item:nth-of-type(13) a',
                          "photos":'relies_prev:css selector;li.menu-list-item:nth-of-type(14) a',
                          "weather":'relies_prev:css selector;li.menu-list-item:nth-of-type(15) a',
                          "select":'relies_prev:css selector;li.menu-list-item:nth-of-type(16) a',
                          "asianamerica":'relies_prev:css selector;li.menu-list-item:nth-of-type(17) a',
                          "nbcblk":'relies_prev:css selector;li.menu-list-item:nth-of-type(18) a',
                          "nbclatino":'relies_prev:css selector;li.menu-list-item:nth-of-type(19) a',
                          "nbcout":'relies_prev:css selector;li.menu-list-item:nth-of-type(20) a',
                         
                      },
                      "usnews":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "politics":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "world":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "local":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "business":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "health":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "investigations":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "cultures":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "science":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "sports":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'},
                      "tech":{"articles":'relies_prev~rand_ind:css selector;ul.styles_items__Ldw92 li a'}
                  }
                  },
                "https://www.costco.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;navigation-dropdown',
                 "endpoints":
                 { 
                  "closepopup":   '"id;closeEmailPopup"',
                  "signin":'id;header_sign_in',
                  #"productmainpage":''

                 },
                  "sub-endpoints":
                  {
                      "main_menu":{
                          "appliances":'',
                          "baby":'',
                          "beauty":'',
                          "clothing":'',
                          "computers":'',
                          "costconext":'',
                          "electronics":'',
                          "floral":'',
                          "furniture":'',
                          "gift":'',
                          
                      }
                  }
                }, 
                 
}


