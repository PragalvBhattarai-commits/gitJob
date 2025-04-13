import json, base64, requests

def new_grad_jobs():
  # Get job data from github repo and decode it
  url = "https://api.github.com/repos/SimplifyJobs/New-Grad-Positions/contents/README.md?ref=dev"
  response = requests.get(url)

  data = response.json()
  encoded_data = data["content"]
  decoded_data = base64.b64decode(encoded_data).decode('utf-8')

  # Functions to read from and write to new_grad_data.json
  def read_data():
    with open("new_grad_data.json", "r") as f:
      data = json.load(f)
      return data

  def write_data(current_jobs):
    with open("new_grad_data.json", "w") as f:
      json.dump(current_jobs, f, indent=2)


  # Functions to check previous data, compare to current data, and return any new information.
  # Variable to keep track of number of jobs
  previous_jobs = read_data()
  current_jobs = {}
  new_jobs = {}
  num_jobs = 0

  # Fill current_jobs with all of the current jobs
  for i in range(len(decoded_data)):
    if (decoded_data[i] == "[") and (decoded_data[i-1] == "*"):
      company = ""
      
      j = i+1
      while (decoded_data[j] != "]"):
        company += decoded_data[j]
        j+=1
      i = j
      num_jobs += 1

      if company in current_jobs:
        current_jobs[company] += 1
      else:
        current_jobs[company] = 1

  # Compare current_jobs with previous_jobs to find new_jobs
  for key in current_jobs.keys():
    if key in previous_jobs:
      
      if current_jobs[key] == previous_jobs[key]:
        pass
      elif current_jobs[key] > previous_jobs[key]:
        new_jobs[key] = current_jobs[key] - previous_jobs[key]
    
    else: 
      new_jobs[key] = current_jobs[key]

  # Add the total number of jobs to new_jobs, updata new_grad_data.json with current_jobs 
  new_jobs["total_jobs"] = num_jobs
  write_data(current_jobs)

  return new_jobs