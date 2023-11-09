from django.http import HttpResponse
from django.shortcuts import render

jobList = [{
  "id": 1,
  "Job_Name": "Data Analyst",
  "Description": "Team-oriented exuding time-frame",
  "Company Name": "Crist Group"
}, {
  "id": 2,
  "Job_Name": "Sales Representative",
  "Description": "Streamlined dedicated extranet",
  "Company Name": "Haag Inc"
}, {
  "id": 3,
  "Job_Name": "Data Analyst",
  "Description": "Fully-configurable global strategy",
  "Company Name": "Hills-Beier"
}, {
  "id": 4,
  "Job_Name": "Marketing Manager",
  "Description": "Persistent fresh-thinking protocol",
  "Company Name": "Blanda, Grady and Mitchell"
}, {
  "id": 5,
  "Job_Name": "Data Analyst",
  "Description": "Synchronised stable archive",
  "Company Name": "Crona Inc"
}, {
  "id": 6,
  "Job_Name": "Data Analyst",
  "Description": "Focused system-worthy application",
  "Company Name": "Mertz Group"
}, {
  "id": 7,
  "Job_Name": "Data Analyst",
  "Description": "Right-sized interactive alliance",
  "Company Name": "Lubowitz-Emard"
}, {
  "id": 8,
  "Job_Name": "Software Engineer",
  "Description": "Innovative mobile system engine",
  "Company Name": "Mosciski-Stark"
}, {
  "id": 9,
  "Job_Name": "Software Engineer",
  "Description": "Multi-tiered discrete matrices",
  "Company Name": "Jaskolski-Shields"
}, {
  "id": 10,
  "Job_Name": "Software Engineer",
  "Description": "Vision-oriented tangible open architecture",
  "Company Name": "Ziemann-Harris"
}, {
  "id": 11,
  "Job_Name": "Data Analyst",
  "Description": "Cross-group motivating superstructure",
  "Company Name": "Weimann-Batz"
}, {
  "id": 12,
  "Job_Name": "Data Analyst",
  "Description": "Business-focused scalable infrastructure",
  "Company Name": "Doyle LLC"
}, {
  "id": 13,
  "Job_Name": "Graphic Designer",
  "Description": "Balanced systemic system engine",
  "Company Name": "Cormier-Rodriguez"
}, {
  "id": 14,
  "Job_Name": "Data Analyst",
  "Description": "Fully-configurable multi-state throughput",
  "Company Name": "Greenholt, Beier and Brekke"
}, {
  "id": 15,
  "Job_Name": "Sales Representative",
  "Description": "Configurable empowering benchmark",
  "Company Name": "Bernhard, Schmitt and Miller"
}, {
  "id": 16,
  "Job_Name": "Data Analyst",
  "Description": "Total impactful circuit",
  "Company Name": "Gislason Group"
}, {
  "id": 17,
  "Job_Name": "Sales Representative",
  "Description": "Grass-roots modular infrastructure",
  "Company Name": "Larkin-Flatley"
}, {
  "id": 18,
  "Job_Name": "Marketing Manager",
  "Description": "Intuitive disintermediate model",
  "Company Name": "Wisozk-Krajcik"
}, {
  "id": 19,
  "Job_Name": "Graphic Designer",
  "Description": "Devolved client-server contingency",
  "Company Name": "Koch-Nolan"
}, {
  "id": 20,
  "Job_Name": "Data Analyst",
  "Description": "Adaptive web-enabled capacity",
  "Company Name": "Stark, Fadel and Watsica"
}]

def jobs(request):
    context = {'jobList': jobList, 'data':'this is data'}
    return render(request, 'jobs/jobs.html', context)

def job(request, pk):
    jobObj = None
    for i in jobList:
        if i['id'] == pk:
            jobObj = i
    context = {'jobObj': jobObj, 'data':'1233'}
    return render(request, 'jobs/job.html',context)