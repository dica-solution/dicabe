from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(0, 0)

    # def on_start(self):
    #     self.client.post("/api/users/login", json=
    #     {
    #         "user": {
    #             "email": "nguyenthanhquang.cse@gmail.com",
    #             "password": "dica@123"
    #         }
    #     })

    @task
    def profile(self):
        self.client.get("/api/profiles/nt-quang")
