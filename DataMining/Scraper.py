#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1 #BIO URLS

import requests
from lxml import etree

page = requests.get('https://www2.eecs.berkeley.edu/Faculty/Lists/list.html?_ga=2.265667791.114403426.1690419501-1056980878.1690419501#Z')
html_content = page.content

html_tree = etree.HTML(html_content)
xpath_expression = '//a/@href'
links = html_tree.xpath(xpath_expression)

bio_urls = []
substring = "/Faculty/Homepages/"
for link in links:
    if substring in link:
        bio_url = "https://www2.eecs.berkeley.edu/" + link
        bio_urls.append(bio_url)
bio_urls = list(set(bio_urls)) # drop duplicates


# In[ ]:


2 #WRITE BIO URLS
file_handle_text = open("bio_urls.txt", "w")
for idx, bio_url in enumerate(bio_urls):
    if idx < len(bio_urls) - 1:
        file_handle_text.write(f"{idx + 1}. {bio_url}\n")
    else:
        file_handle_text.write(f"{idx + 1}. {bio_url}")
    
file_handle_text.close()


# In[ ]:


3 #BIO TEXT

bios = []
for bio_url in bio_urls[0:1]:
    print(bio_url)
    page = requests.get(bio_url)
    html_content = page.content
    html_tree = etree.HTML(html_content)
    xpath_expression = '//div/text()'
    text = html_tree.xpath(xpath_expression)
    
    clean_bio_text = [string for string in text if len(string.strip()) > 20]
    if len(clean_bio_text) > 0:
        bio_text_str = ":".join(clean_bio_text).strip()
        bios.append(bio_text_str)
    else:
        bios.append("No Biography Found")
    
print(len(bios))


# In[ ]:


4 #WRITE BIOS
file_handle_text = open("bios.txt", "w")
for idx, bio in enumerate(bios):
    if idx < len(bios) - 1:
        file_handle_text.write(f"{idx + 1}. {bio}\n")
    else:
        file_handle_text.write(f"{idx + 1}. {bio}")
    
file_handle_text.close()


# In[ ]:


5 #courses taught / research areas

page = requests.get('https://www2.eecs.berkeley.edu/Research/Areas/')
html_content = page.content

html_tree = etree.HTML(html_content)
xpath_expression = '//a/text()'
topics = html_tree.xpath(xpath_expression)
research_areas = []
for topic in topics:
    if "(" and ")" in topic:
        research_areas.append(topic)


xpath_expression = '//a/@href'
links = html_tree.xpath(xpath_expression)
substring = "/Research/Areas/"
course_codes = []
for link in links:
    if substring in link:
        if 'www' not in link:
            course_code = link.replace("/Research/Areas/", "")
            course_codes.append(course_code)     
        

research_area_urls = {}

for link in links:
    if substring in link:
        research_area_url = "https://www2.eecs.berkeley.edu" + link
        if len(research_area_url) < 55:
            if 'AI' in research_area_url:
                research_area_urls["Artificial Intelligence (AI)"] = research_area_url
            if 'ARC' in research_area_url:
                research_area_urls["Computer Architecture & Engineering (ARC)"] = research_area_url
            if 'BIO' in research_area_url:
                research_area_urls["Biosystems & Computational Biology (BIO)"] = research_area_url
            if 'CIR' in research_area_url:
                research_area_urls["Control, Intelligent Systems, and Robotics (CIR)"] = research_area_url    
            if 'CPSDA' in research_area_url:
                research_area_urls["Cyber-Physical Systems and Design Automation (CPSDA)"] = research_area_url
            if 'DBMS' in research_area_url:
                research_area_urls["Database Management Systems (DBMS)"] = research_area_url
            if 'EDUC' in research_area_url:
                research_area_urls["Education (EDUC)"] = research_area_url
            if 'ENE' in research_area_url:
                research_area_urls["Power and Energy (ENE)"] = research_area_url
            if 'GR' in research_area_url:
                research_area_urls["Graphics (GR)"] = research_area_url    
            if 'HCI' in research_area_url:
                research_area_urls["Human-Computer Interaction (HCI)"] = research_area_url
            if 'IDNCS' in research_area_url:
                research_area_urls["Information, Data, Network, and Communication Sciences (IDNCS)"] = research_area_url
            if 'INC' in research_area_url:
                research_area_urls["Integrated Circuits (INC)"] = research_area_url
            if 'MEMS' in research_area_url:
                research_area_urls["Micro/Nano Electro Mechanical Systems (MEMS)"] = research_area_url
            if 'OSNT' in research_area_url:
                research_area_urls["Operating Systems & Networking (OSNT)"] = research_area_url    
            if 'PHY' in research_area_url:
                research_area_urls["Physical Electronics (PHY)"] = research_area_url
            if 'PS' in research_area_url:
                research_area_urls["Programming Systems (PS)"] = research_area_url
            if 'SCI' in research_area_url:
                research_area_urls["Scientific Computing (SCI)"] = research_area_url
            if 'SEC' in research_area_url:
                research_area_urls["Security (SEC)"] = research_area_url
            if 'SP' in research_area_url:
                research_area_urls["Signal Processing (SP)"] = research_area_url    
            if 'THY' in research_area_url:
                research_area_urls["Theory (THY)"] = research_area_url
            
print(research_area_urls)

 


# In[ ]:


# MAX retries for URL reached. Unable to run script

courses_taught_arr = []
for bio_url in bio_urls[1:]:
    page = requests.get(bio_url)
    html_content = page.content
    html_tree = etree.HTML(html_content)
    xpath_expression = '//a/text()'
    topics = html_tree.xpath(xpath_expression)
    courses_taught = ""
    for topic in topics:
        if topic in research_areas:     
            
            course_link = research_area_urls[topic]
        
            course_page = requests.get(course_link)
            course_html_content = course_page.content
            
            course_html_tree = etree.HTML(course_html_content)
            course_xpath_expression = '//a/text()'
            related_courses = course_html_tree.xpath(course_xpath_expression)
            for idx, related_course in enumerate(related_courses):
                if len(related_course) > 30:
                    if "CS" == related_course[0:2]:
                        courses_taught += f"{related_course} "
                    elif "EE" == related_course[0:2]:
                        courses_taught += f"{related_course} "

            courses_taught_arr.append(courses_taught)
            
            
 


# In[ ]:


6 #WRITE Courses Taught
file_handle_text = open("courses_taught.txt", "w")
for idx, course in enumerate(courses_taught_arr):
    if idx < len(result) - 1:
        file_handle_text.write(f"{idx + 1}. {course}\n")
    else:
        file_handle_text.write(f"{idx + 1}. {course}")
    
file_handle_text.close()


# In[ ]:




