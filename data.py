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

{"https://www.pcgamer.com/":
                {"specifics":"ablock=true;",
                 "main_menu": 'class name;wrapper',
                 "endpoints":
                 {
                     
                
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{
                            "news":'partial link text;news',
                            "reviews":'partial link text;reviews',
                            "hardware":'partial link text;hardware',
                            "BestOf":'partial link text;best-of',
                            "top100":'partial link text;the-top-100-pc-games-2022',
                            },
                    "hardware":{"hardware":"rand_ind:class name;listingresult"
                                }

                        
                  
                 }
                }
}



