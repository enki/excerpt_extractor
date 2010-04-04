from eextractor import get_summary

if __name__ == "__main__":
    urllist=("http://www.sfgate.com/cgi-bin/article.cgi?f=/c/a/2009/06/04/DD7V1806SV.DTL&type=performance",
              "http://www.chloeveltman.com/blog/2009/05/two-very-different-symphonies.html#links",
              "http://www.chloeveltman.com/blog/2009/06/child-prodigy-at-peabody-essex-museum.html#links",
              "http://www.sfgate.com/cgi-bin/article.cgi?f=/c/a/2009/06/04/NS9617O7JK.DTL&type=performance",
              "http://blogs.mercurynews.com/aei/2009/06/04/ramya-auroprem-joins-cast-of-spelling-bee/",
              "http://www.mercurynews.com/karendsouza/ci_12510394",
              "http://www.reason.com/news/show/134059.html")
    for u in urllist:
        print u
        try:
            print unicode(get_summary(u)['desc']) + '\n'
        except UnicodeEncodeError:
            pass
    
