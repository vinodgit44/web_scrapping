from bs4 import BeautifulSoup
import requests

html_text=requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
#print(html_text)
soup=BeautifulSoup(html_text,"lxml")
print("write skills to filter out")
unknown_skills=input('>')
def find_jobs():
    count = 0
    job = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for job in job:
        published = job.find("span", class_="sim-posted").text
        if "ago" in published:  #checking for jobs posted few days ago
            company_name = job.find("h3", class_='joblist-comp-name').text.replace(' ', '')
            detail = job.find("ul", class_="top-jd-dtl clearfix")
            info = job.header.h2.a["href"]
            exp = detail.find("li").text.split()[-2]
            location = detail.find("span").text
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            print("filtering skills")  #filtering jobs which require unknown skill
            if unknown_skills not in skills:

                count += 1
                ##saving filtered data on file
                with open(f"job_data/{count}.txt","w") as f:
                    print(f'writing on file {count}.txt')

                    f.write(f'Company Name : {company_name.strip()}\n')
                    f.write(f'Experience: {exp.strip()}\n')
                    f.write(f'Job Location: {location.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f'Link for More Info. : {info.strip()}\n')
                    print(f'writing done on file {count}.txt ')


                    print('data writtern on file')
                    print(f'Company  : {count}')
                    print(f'Company Name : {company_name.strip()}')
                    print(f'Experience: {exp.strip()}')
                    print(f'Job Location: {location.strip()}')
                    print(f'Required Skills: {skills.strip()}')

                    print(f'Link for More Info. : {info.strip()}')
                    print("****************************************")



find_jobs()




