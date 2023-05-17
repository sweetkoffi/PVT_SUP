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
                     "about":'class name;caret',
                     "donation":'link text;Make a Donation'
                     "theApacheWay"

                 },
                  "sub-endpoints":
                  {
                      "about":{
                                "overview":'link text;Overview',
                                "process":'link text;Process',
                                "governance":'link text;Governance',
                                "theApacheWay":'link text;The Apache Way',
                                "membership":'link text;Membership',
                                "community":'link text;Community',
                                "diversity":'link text;Diversity & Inclusion',
                                "codeofconduct":'link text;Code of Conduct',
                                "glossary":'link text;Glossary',
                                "aboutourname":'link text;About Our Name',
                                "faq":'link text;FAQ',
                                "supportAppache":'link text;Media/Analysts',
                                "media":'link text;Contact',
                                "contact":'link text;Support Apache'
                            },

                    "Donation":{"donatenow": {
                                    "donation":'link text;Donate Now',
                                    "creditCard":'link text;Via ACH',
                                    "creditCard":'link text;Via Paypal',
                                    "creditCard":'link text;Via Credit Card',
                                }
                                
                 
                 }
                }
                }

}
