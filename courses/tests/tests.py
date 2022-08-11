import requests

class CourseViewTests:
    headers = { 'Authorization': 'Token 9d8a88d520b87eb53b5759c420120e968afcdfcb' }
    url_base_courses = 'http://localhost:8000/api/v2/courses/'

    def test_get_courses(self):
        response = requests.get(url=self.url_base_courses, headers=self.headers)
        assert response.status_code == 200

    def test_get_course(self):
        response = requests.get(url=f'{self.url_base_courses}5/', headers=self.headers)
        assert response.status_code == 200

    def test_post_course(self):
        new_course = {
            "title": "Programming with Rust",
            "url": "https://rust.org"
        }

        response = requests.post(url=self.url_base_courses, headers=self.headers, data=new_course)

        assert response.status_code == 201
        assert response.json()['title'] == new_course['title']


    def test_put_course(self):
        course_updated = {
            "title": "Course of Cloujure",
            "url": "https://cloujure.net"
        }

        response = requests.put(url=f'{self.url_base_courses}10/', headers=self.headers, data=course_updated)

        assert response.status_code == 200
        assert response.json()['title'] == course_updated['title']