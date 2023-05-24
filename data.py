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
                      "gaming":{"video":"rand_ind:css selector;ytd-video-renderer"
                          
                      },
                  }
                },  
                # Website : pcGamer Problem with this website , need to move the mouse
                "https://www.pcgamer.com/": {
        "specifics": "ablock=true;",
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
                "hardware": "rand_ind:class name;listingresult"
            }
        }
    },
    "https://apache.org/": # Website : Apache
                {"specifics":"ablock=true;",
                 "endpoints":
                 {
                     "about":'partial link text;About',
                     "donation":'partial link text;Make a Donation',
                     "theApacheWay":'partial link text;The Apache Way',
                     "joinUs":'partial link text;Join Us',
                     "downaloads":'partial link text;downloads',
                     "projects":'partial link text;Projects',
                     "people":'partial link text;People',
                     "community":'partial link text;Community',
                     "secondInfrast":'partial link text;Insfrastructure',
                     "sponsors":'partial link text;Sponsors',
                     "license":'partial link text;License'
                     

                 },
                  "sub-endpoints":
                  {
                      "about":{
                                "overview":'relies_preview:partial link text;Overview',
                                "process":'relies_preview:partial link text;Process',
                                "governance":'relies_preview:partial link text;Governance',
                                "theapache":'relies_preview:partial link text;The Apache Way',
                                "membership":'relies_preview:partial link text;Membership',
                                "community":'relies_preview:partial link text;Community',
                                "diversity":'relies_preview:partial link text;Diversity & Inclusion',
                                "codeofconduct":'relies_preview:partial link text;Code of Conduct',
                                "glossary":'relies_preview:partial link text;Glossary',
                                "aboutourname":'relies_preview:partial link text;About Our Name',
                                "faq":'relies_preview:partial link text;FAQ',
                                "supportappache":'relies_preview:partial link text;Media/Analysts',
                                "media":'relies_preview:partial link text;Contact',
                                "contact":'relies_preview:partial link text;Support Apache'
                            },
                    "Donation":{
                     "donateNow": {
                                    "donateNow":'relies_preview: partial link text;Donate Now',
                                    "viaAch":'relies_preview: partial link text;Via ACH',
                                    "viaPaypal":'relies_preview: partial link text;Via Paypal',
                                    "creditCard":'relies_preview: partial link text;Via Credit Card',
                                },
                                "buySwag":'relies_preview: partial link text;Buy Swag', 
                                "AsfSponsorship":'relies_preview: partial link text;ASF Sponsorship',
                                "targetedSposor":'relies_preview: partial link text;Targeted Sponsorship',
                                "CorporateGiving":'relies_preview: partial link text;Corporate Giving',

                     "theApacheWay":{
                                    "sustainOpenSourc":'relies_preview: partial link text;Sustainable Open Source',
                                    "howItWorks":'relies_preview: partial link text;How it Works',
                                    "Merit":'relies_preview:partial link text;Merit',
                                    "theapachewaysub":'direct-link;theapacheway',
                                    "Success at Apache":'relies_preview: partial link text;Success at Apache'
                         
                                    },
                     "joinUs":{"gettingStarted":'relies_preview: partial link text;Getting Started',
                               "helpWanted":'relies_preview: partial link text;Help Wanted',
                               "ApacheCon":'relies_preview: partial link text;ApacheCon', 
                               "comEvents":'relies_preview: partial link text;Community Events',
                               "travelAssistance":'relies_preview: partial link text;Travel Assistance',
                               "summerOfCode":'relies_preview: partial link text;Summer of Code',
                               "etiquette":'relies_preview: partial link text;Etiquette'  
                               },
                     "downloads":{"distribution":'relies_preview:partial link text;Distribution',
                                  "releases":'relies_preview:partial link text;Releases',
                                  "infrastStatus":'relies_preview: partial link text;Infrastructure Status',
                                  "infrastStatistics":'relies_preview: partial link text;Infrastructure Statistics'
                         
                     },
                     "projects":{
                                 "projectList":'relies_preview:partial link text;Project List',
                                 "howThetWork": 'relies_preview:partial link text;How they work',
                                 "independence": 'relies_preview:partial link text;Independence',
                                 "dateFounded": 'relies_preview:partial link text;Date Founded',
                                 "names": 'relies_preview:partial link text;Names',
                                 "categories": 'relies_preview:partial link text;Categories',
                                 "languages": 'relies_preview:partial link text;Languages',
                                 "statistics": 'relies_preview:partial link text;Statistics',
                                 "apacheIncub": 'relies_preview:partial link text;Apache Incubator',
                                 "helpWanted": 'relies_preview:partial link text;Help Wanted',
                                 "brandManag": 'relies_preview:partial link text;Brand Management',
                                 "glossaryOfTherms": 'relies_preview:partial link text;Glossary of Terms',         
                     },
                     # select on the project endoint - new sub-endpoint to subdomain-name :projects.apache.org 
                     "projectList":{"overviewProject":'ind_1:css selector;ul.list-unstyled:nth-of-type(1) li a'},
                     "people":{
                                    "roles":'relies_preview: partial link text;Roles',
                                    "members":'relies_preview: partial link text;Members',
                                    "committers":'relies_preview: partial link text;Committers',
                                    "boardOfDir":'relies_preview: partial link text;Board of Directors',
                                    "offiersProject":'relies_preview: partial link text;Offiers & Project VPs',
                                    "diversityInclusion":'relies_preview: partial link text;Diversity & Inclusion',
                                    "codeOfCOnduct":'relies_preview: partial link text;Code of Conduct',
                                    "committerDir":'relies_preview: partial link text;Committer Directory',
                                    "HeatMap":'relies_preview: partial link text;Heat Map',
                     },
                     "community":{
                         "commDev":'relies_preview: partial link text;Community Development',
                         "codeOfConduct":'relies_preview: partial link text;Code of Conduct',
                         "getInvol":'relies_preview: partial link text;Get Involved',
                         "mentoring":'relies_preview: partial link text;Mentoring',
                         "helpWanted":'relies_preview: partial link text;Help Wanted',
                         "commEvents":'relies_preview: partial link text;Community Events',
                         "faq":'relies_preview: partial link text;FAQ',
                         "mailingList":'relies_preview: partial link text;Mailing Lists',
                     },
                     "infrastructure":{
                         "infOver":'relies_preview: partial link text;Infra overview',
                         "polAndTool":'relies_preview: partial link text;Policiers and Tools',
                         "cwiki":'relies_preview: partial link text;CWiki',
                         
                     },
                     "license":{
                         "apacheLicense":'relies_preview: partial link text;Apache License 2.0',
                         "licensFaq":'relies_preview: partial link text;Licensing FAQ',
                         "contribLiAgre":'relies_preview: partial link text;Contributor License Agreements',
                         "softwGrant":'relies_preview: partial link text;Software Grants',
                         "tradeMark":'relies_preview: partial link text;Trademarks',
                         "exports":'relies_preview: partial link text;Exports',
                         
                     },
                      "sponsors":{
                         "sponTheAsf":'relies_preview: partial link text;Sponsor the ASF',
                         "sponThanks":'relies_preview: partial link text;Sponsor thanks',
                         "corporateGiv":'relies_preview: partial link text;Corporate Giving',
                         "indivDonations":'relies_preview: partial link text;Individual Donations',
                         "buyStuff":'relies_preview: partial link text;Buy Stuff'
                     }
               
                 }
                }
                },# Website : The atlantic
                "https://www.theatlantic.com/":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:class name;NavHamburgerButton_box__Sq9Ip',
                 "endpoints":
                 { 
                  "popular":'partial link text;Popular',
                  "latest": 'partial link text;Latest',
                  "newsletters":'partial link text;Newsletters',
                  "login":'partial link text;Sign In',
                  "subscribe":'partial link text;Subscribe'
                },
                  "sub-endpoints":
                  {
                      "main_menu":{
                          "politics":'relies_preview: partial link text;Politics',
                          "technology":'relies_preview: partial link text;Technology',
                          "business":'relies_preview: partial link text;Business',
                          "global":'relies_preview: partial link text;Global',
                          "health":'relies_preview: partial link text;Business',
                          "features":'relies_preview: partial link text;Features',
                          "shadowland":'relies_preview: partial link text;Shadowland',
                          "ideas":'relies_preview: partial link text;Ideas',
                          "science":'relies_preview: partial link text;Science',
                          "culture":'relies_preview: partial link text;Culture',
                          "books":'relies_preview: partial link text;Books',
                          "education":'relies_preview: partial link text;Education',
                          "family":'relies_preview: partial link text;Family',
                          "progress":'relies_preview: partial link text;Progress',
                          "fiction":'relies_preview: partial link text;Fiction',
                          "photo":'relies_preview: partial link text;Photo',
                          "planet":'relies_preview: partial link text;Planet',
                          "podcast":'relies_preview: partial link text;Podcasts',
                          "projects":'relies_preview: partial link text;Projects',
                          "events":'relies_preview: partial link text;Events',
                          "explArchive":'relies_preview: partial link text;Explore The Atlantic Archive',
                          "playCrossword":'relies_preview: partial link text;Play The Atlantic crossword',
                          "latestIssue":'relies_preview: partial link text;Latest Issue',
                          "pastIssue":'relies_preview: partial link text;Past Issues',
                          "giveGift":'relies_preview: partial link text;Give a Gift',  
                      },

                      "politics":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "technology":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "business":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "global":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "health":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "features":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "shadowland":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "ideas":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "science":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "culture":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "books":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "education":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "family":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "progress":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "fiction":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      "photo":{"article":"rand_ind:class name;article"},
                      "podcast":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      #"events":{"article":"rand_ind:class name;LandingRiver_promoItem__LuiRv"},
                      
                      

                  }
                },
}
