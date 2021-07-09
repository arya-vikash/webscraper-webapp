from bs4 import BeautifulSoup
import requests

def find_deals():
    l=[]
    html_text0=requests.get('https://www.flipkart.com/dotd-store?=Web&wid=3.dealCard.OMU_3&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_wc_view-all_3').text

    soup0=BeautifulSoup(html_text0,'lxml')

    all_deals=soup0.find_all('div',class_="_1FNrEw")
    time_left=soup0.find('div',class_="_3iNFSg").span.text
    for deal in all_deals:
        deal_link=deal.a['href']
        deal_name=deal.find('div',class_="_3LU4EM").text
        deal_offer=deal.find('div',class_='_2tDhp2').text
        deal_category=deal.find('div',class_='_3khuHA').text
        deal_image=deal.find('img',class_='_396cs4 _3exPp9')

        deal_dict={
            'deal_name':deal_name,'deal_link':deal_link,'deal_category':deal_category,
            'deal_offer':deal_offer,'deal_image':deal_image['src']
        }
        
        l.append(deal_dict)
        tl=time_left.split(':')
    return [tl[0],tl[1],l]

