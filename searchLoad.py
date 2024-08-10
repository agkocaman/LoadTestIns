from locust import HttpUser, TaskSet, task, between

class SearchTests(TaskSet):
    @task
    def search(self):
        searchwords = ["ayakkabı", "bilgisayar", "defter", "kumanda", "buzdolabı"]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        for word in searchwords:
            with self.client.get(f"/arama?q={word}", headers=headers, catch_response=True) as response:
                if response.status_code == 200 and "arama" in response.url:
                    if word in response.text:
                        response.success()
                    else:
                        response.failure(f"Expected results for '{word}' were not found.")
                else:
                    response.failure(f"Failed to search for '{word}'. Status code: {response.status_code}")

class WebsiteUser(HttpUser):
    tasks = [SearchTests]
    wait_time = between(1, 5)
    host = "https://www.n11.com"
