from apify_client import ApifyClient
import os 
from dotenv import load_dotenv
load_dotenv()

apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

def fetch_linkedin_jobs(search_query, location="india", rows=10):
    """
    Fetch LinkedIn jobs (this one seems to be working)
    """
    try:
        run_input = {
            "title": search_query,
            "location": location,
            "rows": rows,
            "proxy": {
                "useApifyProxy": True,
                "apifyProxyGroups": ["RESIDENTIAL"],
            }
        }
        run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
        jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
        return jobs
    except Exception as e:
        print(f"Error fetching LinkedIn jobs: {e}")
        return get_sample_jobs()  # Return sample data if API fails

def fetch_naukri_jobs(search_query, location="india", rows=10):
    """
    Naukri API requires payment, so return sample data
    """
    try:
        # Try the API first
        run_input = {
            "keyword": search_query,
            "maxJobs": rows,
            "freshness": "all",
            "sortBy": "relevance",
            "experience": "all",
        }
        run = apify_client.actor("wsrn5gy5C4EDeYCcD").call(run_input=run_input)
        jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
        return jobs
    except Exception as e:
        print(f"Naukri API error (using sample data): {e}")
        return get_sample_jobs()

def get_sample_jobs():
    """
    Return sample job data when APIs fail
    """
    return [
        {
            "title": "Software Developer",
            "companyName": "Tech Solutions Inc.",
            "location": "Bangalore, India", 
            "link": "https://linkedin.com/jobs/view/123",
            "description": "Looking for skilled software developers with strong programming background."
        },
        {
            "title": "Frontend Engineer", 
            "companyName": "Digital Innovations",
            "location": "Hyderabad, India",
            "link": "https://linkedin.com/jobs/view/124",
            "description": "Join our team to build amazing user experiences with modern web technologies."
        },
        {
            "title": "Full Stack Developer",
            "companyName": "StartUp Ventures", 
            "location": "Pune, India",
            "link": "https://linkedin.com/jobs/view/125",
            "description": "Opportunity to work on cutting-edge technologies in a fast-paced environment."
        }
    ]