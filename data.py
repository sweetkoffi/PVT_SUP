WEBSITE_LIST = {"https://www.youtube.com/":
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
                 }  
                }

{"https://www.pcgamer.com/": # Problem with this website , need to move the mouse
                {"specifics":"ablock=true;",
                 "endpoints":
                 {
                     "Popup_close":'class name;exit-intent__close-button'
                
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{
                            "news":'partial link text;news',
                            "reviews":'partial link text;reviews',
                            "hardware":'partial link text;hardware',
                            "BestOf":'partial link text;best-of',
                            "top100":'partial link text;the-top-100-pc-games-2022'
                            },
                    "hardware":{"hardware":"rand_ind:class name;listingresult"
                                }

                 
                 }
                }
}

{"https://apache.org/": # Working ON
                {"specifics":"ablock=true;",
                 "endpoints":
                 {
                     "about":'partial link;About',
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
                                "overview":'relies_preview:link text;Overview',
                                "process":'relies_preview: partial link text;Process',
                                "governance":'relies_preview: partial link text;Governance',
                                "theApacheWay":'relies_preview: partial link text;The Apache Way',
                                "membership":'relies_preview: partial link text;Membership',
                                "community":'relies_preview: partial link text;Community',
                                "diversity":'relies_preview: partial link text;Diversity & Inclusion',
                                "codeofconduct":'relies_preview: partial link text;Code of Conduct',
                                "glossary":'relies_preview: partial link text;Glossary',
                                "aboutourname":'relies_preview: partial link text;About Our Name',
                                "faq":'relies_preview: partial link text;FAQ',
                                "supportAppache":'relies_preview: partial link text;Media/Analysts',
                                "media":'relies_preview: partial link text;Contact',
                                "contact":'relies_preview: partial link text;Support Apache'
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
                                 "independence": 'relies_preview:partial link text;Independence',
                                 "independence": 'relies_preview:partial link text;Independence',
                                 "independence": 'relies_preview:partial link text;Independence'   

                                 
                     },
                     "projectList":{"overviewProject":'ind_1:css selector;ul.list-unstyled:nth-of-type(1) li a'}

                                      
                 }
                }
                }

}



