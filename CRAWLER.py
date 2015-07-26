                                #CRAWLER#

## main programme:
## crawl_web(page)
####################################################################
##                              CRAWLER
####################################################################
def search_key_word(liste):
        keys=[]
        for e in liste:
                keys.append(e[0])
        return keys
def hash_table(liste):
        index=[]
        for e in liste:
                for k in e[1]:
                        index.append([k,[e]])
                del(e[1])
        for e in index:
                for j in index:
                        if e[0]==j[0]:
                                union(e[1],j[1])
        for e in index:
                e[1]=extract_in_index(e[1])
        
        for e in index:
                for j in index:
                        if ((e[0]==j[0])and(e[1]!=j[1])):
                                e[1]=j[1]
        index=no_repeat(index)
        return index
def extract_in_index(index):
        n=[]
        for e in index:
                for j in e:
                        n.append(j)
        return n

                        
def get_page(url):
        try:
                import urllib
                return urllib.urlopen(url).read()
        except:
                return""
def analyse_page_h1(page):
        start_key=page.find('<h1>')
        if(start_key==-1):
                return None
        else:
                end_key=page.find('</h1>')
                word=page[start_key+4:end_key]
                word=word.split()
                return word
def extract_link(page):
        start_link=page.find('<a href=')
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url
def get_next_target(page):
        start_link=page.find('a href=')
        if start_link!=-1:
                start_quote=page.find('"',start_link)
                end_quote=page.find('"',start_quote+1)
                url=page[start_quote+1:end_quote]
                return url, end_quote
        else:
                return None,0
def collect_all_links(page):
        index=[]
        while True:
                url,endpos=get_next_target(page)
                if url:
                        index.append(url)
                        page=page[endpos:]
                else:
                        break
        return index
def union(a,b):
        for e in b:
                if e not in a:
                        a.append(e)
        return a
def crawl_page(page):
        tocrawl=collect_all_links(page)
        crawled=[]
        while tocrawl:
                url=tocrawl.pop()
                if url not in crawled:
                        union(tocrawl,collect_all_links(get_page(page)))
                        crawled.append(url)
        return crawled
def crawl_web(page):
        all_web_links=crawl_page(page)
        for e in all_web_links:
                page=get_page(e)
                union(all_web_links,crawl_page(page))
        return all_web_links
def no_repeat(index):
        new_index=[]
        while index:
              e=index.pop()
              if e not in index:
                      new_index.append(e)
        return new_index
##########################################################################
##              KEY WORD
##########################################################################
def get_next_word(page):
        start_key=page.find('<h1>')
        if start_key!=-1:
                start_word=page.find('>',start_key)
                end_key=page.find('</h1>',start_word+1)
                key_word=page[start_word+1:end_key]
                return key_word, end_key
        else:
                return None,0
def assign_url_to_word(url):
        page=get_page(url)
        key_words=[]
        start_quote_url=url.find('/web')
        start_word_url=url.find('/',start_quote_url+4)
        end_word_url=url.find('.html')
        key_word=url[start_word_url+1:end_word_url]
        index_key_word_url=[key_word,[url]]
        return key_word
def collect_all_key_from_page(page):
        index_word=[]
        while True:
                key,endpos=get_next_word(page)
                if key:
                        index_word.append(key)
                        page=page[endpos:]
                else:
                        break
        return index_word
def extract_all_keys_form_url(page):
        liste=no_repeat(crawl_web(page))
        index=[]
        index_tmp=[]
        for e in liste:
                tmp_key=[]
                tmp_key_word=assign_url_to_word(e)
                index.append([tmp_key_word,[e]])
        return index
def trouver(index):
        search=raw_input("Votre recherche:     ")
        q=search
        req=None
        for e in index:
                if e[0]==q:
                        req=e[1]
        return req
def indexation(index):
        ind=[]
        for e in index:
                for i in e:
                        ind.append(i)
        ind=no_repeat(ind)
        new_ind=[]
        while ind:
                a=ind.pop()
                new_ind.append([a])
        return new_ind
def collect_all_keys_web(page):
        liste=no_repeat(crawl_web(page))
        all_url_keys=[]
        for e in liste:
                tmp_list_keys=[]
                page_tmp=get_page(e)
                tmp_list_keys=collect_all_key_from_page(page_tmp)
                tmp_list_keys.append(assign_url_to_word(e))
                tmp_list_keys=no_repeat(tmp_list_keys)
                all_url_keys.append([e,tmp_list_keys])
        return all_url_keys
def reverse_liste(index):
        tmp=[]
        i=len(index)-1
        while i>0:
                tmp.append(index[i])
                i=i-1
        return tmp        
def add_word(page):
        index=crawl_web(page)
        index=no_repeat(index)
        new_index=[]
        while index:
                tmp=index.pop()
                url_plus_word=[]
                url_plus_word=assign_url_to_word(tmp)
                new_index.append(url_plus_word)
        return new_index
####################################################################
##                              DATA STRUCTURE
####################################################################
def analyse_page_alpha(page):
        start_key=page.find('<h1>')
        start_word=page.find('>',start_key)
        end_key=page.find('</h1>')
        key_word=page[start_word+1:end_key]
        return key_word
####################################################################
##                              TIME EXECUTION
####################################################################
def time_execution(code):
        start=time.clock()
        result=eval(code)
        run_time=time.clock()-start
        return result, run_time
def make_string(letters):
        s=""
        for e in letters:
                s=s+e
        return s
def add_to_index(index,keyword,url):
        for e in index:
                if e[0]==keyword:
                        e[1].append(url)
        return index.append([keyword,[url]])
def make_big_index(size):
        index=[]
        letters=['a','a','a','a','a','a','a','a']
        while len(index)<size:
                word=make_string(letters)
                add_to_index
