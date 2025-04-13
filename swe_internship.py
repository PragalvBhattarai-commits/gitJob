import json, base64, requests

def swe_internship():
  # Get data from github repo
  url = "https://api.github.com/repos/speedyapply/2025-SWE-College-Jobs/contents/INTERN_INTL.md?ref=main"
  response = requests.get(url)

  # Get content out of the github response, then decode it
  data = response.json()
  encoded_data = data["content"]
  decoded_data = base64.b64decode(encoded_data).decode('utf-8')

  # Functions to read from and write to swe_internship.json
  def read_data():
    with open("swe_internship.json", "r") as f:
      data = json.load(f)
      return data

  def write_data(current_jobs):
    with open("swe_internship.json", "w") as f:
      json.dump(current_jobs, f, indent=2)
    
  # Hashmaps to keep track of previous_jobs, current_jobs, and new_jobs
  # Variable to keep track of num_jobs
  previous_jobs = read_data()
  current_jobs = {}
  new_jobs = {}
  num_jobs = 0

  # For loop to go through decoded_data and extract company name
  for i in range(len(decoded_data)):
    if (i != len(decoded_data) - 10):
      if (decoded_data[i] == "s") and (decoded_data[i+1] == "t") and (decoded_data[i+2] == "r") and (decoded_data[i+3] == "o") and (decoded_data[i+4] == "n") and (decoded_data[i+5] == "g"):

        company = ""
        j = i+7
        while (decoded_data[j] != "<") and (decoded_data[j+1] != "/") and (decoded_data[j] != "|"):
          company += decoded_data[j]
          j += 1
        i = j+8
        num_jobs += 1

        if (company in current_jobs) and (len(company)!= 0) and (ord(company[0]) != 32):
          current_jobs[company] += 1
        else:
          current_jobs[company] = 1

  # For loop to find new jobs or new jobs added
  for key in current_jobs.keys():
    if key in previous_jobs:

      if current_jobs[key] == previous_jobs[key]:
        pass
      elif current_jobs[key] > previous_jobs[key]:
        new_jobs[key] = current_jobs[key] - previous_jobs[key]

    else: 
      new_jobs[key] = current_jobs[key]

  # Update swe_internships.json with current_jobs, as well as add total number of jobs to new_jobs
  new_jobs["total_jobs"] = num_jobs
  write_data(current_jobs)

  return new_jobs
