import jiebaimport requests from bs4 import BeautifulSoupimport reimport timeimport pandas as pdimport datetimedate=input()url='http://push2ex.eastmoney.com/getTopicZTPool?cb=callbackdata7397354\    &ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0\        &pagesize=1000&sort=fbt:asc&date='+date+'&_=1646049522006'    def getHTMLText(url,code='utf-8'):    try:        r = requests.get(url)        r.raise_for_status()        r.encoding = code        return r.text    except:        return '爬取失败'        html=getHTMLText(url)Code_list=re.findall('"c":"(.*?)","m"',html)Name_list=re.findall('"n":"(.*?)","p"',html)Percentage_list=re.findall('"zdp":(.*?),"amount"',html)percentage_list=list(map(float,Percentage_list))Price_list=re.findall('"p":(.*?),"zdp"',html)price_list=list(map(float,Price_list))price_list=[x/1000 for x in price_list]Amount_list=re.findall('"amount":(.*?),"ltsz"',html)amount_list=list(map(float,Amount_list))amount_list=[x/10000 for x in amount_list]hs_list=re.findall('"hs":(.*?),"lbc"',html)Fund_list=re.findall('"fund":(.*?),"zbc"',html)fund_list=list(map(float,Fund_list))fund_list=[x/10000 for x in fund_list]Firsttime_list=re.findall('"fbt":(.*?),"lbt"',html)#firsttime_list=['0'+x if len(x)<6 else x for x in Firsttime_list]firsttime_list=[datetime.datetime.strptime(date+x, "%Y%m%d%H%M%S") for x in Firsttime_list]Lasttime_list=re.findall('"lbt":(.*?),"fund"',html)lasttime_list=[datetime.datetime.strptime(date+x, "%Y%m%d%H%M%S") for x in Lasttime_list]zb_list=re.findall('"zbc":(.*?),"hybk"',html)lb_list=re.findall('"lbc":(.*?),"fbt"',html)industry_list=re.findall('"hybk":"(.*?)","zttj"',html)dataframe = pd.DataFrame({'股票代码':Code_list,'股票名称':Name_list,                          '涨跌幅':percentage_list,'收盘价':price_list,                          '成交额（万元）':amount_list,                          '封板金额（万元）':fund_list,                          '换手率':hs_list,                          '首次封板时间':firsttime_list,                          '最后封板时间':lasttime_list,                          '炸板次数':zb_list,                          '连板数':lb_list,                          '行业板块':industry_list                          })print(dataframe)