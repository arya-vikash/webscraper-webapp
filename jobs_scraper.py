from bs4 import BeautifulSoup
import requests
import time


def find_jobs(familier_skill):
    jobs_data=[]
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=&txtLocation=&cboWorkExp1=0').text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_= "clearfix job-bx wht-shd-bx")
    for index,job in enumerate(jobs):
        post_time=job.find('span',class_='sim-posted').span.text
        if post_time.split(' ')[1].strip() in ['today','1']:
            job_skills=job.find('span',class_='srp-skills').text.replace(' ','')
            if familier_skill:
                if familier_skill in job_skills.lower():
                    job_title=job.header.h2.a.text
                    company_name=job.find('h3',class_='joblist-comp-name').text
                    more_info=job.header.h2.a['href']
        
                    
                    job_dict={
                        'job_title':job_title,
                        'company_name':company_name,
                        'skills':job_skills,
                        'link':more_info,
                        'post_time':post_time
                    }
                    jobs_data.append(job_dict)
            else:
                job_title=job.header.h2.a.text
                company_name=job.find('h3',class_='joblist-comp-name').text
                more_info=job.header.h2.a['href']
       
                
                job_dict={
                    'job_title':job_title,
                    'company_name':company_name,
                    'skills':job_skills,
                    'link':more_info,
                    'post_time':post_time
                }
                jobs_data.append(job_dict)
    if len(jobs_data)>=1:
        return ['non_empty',jobs_data]
    else:
        return ['empty',f"Seems like there are no recent job uploads  for {familier_skill}"]



        
 

        