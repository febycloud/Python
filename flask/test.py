import unittest
from api import create_app,route_ping,route_post

class ApiTestCase(unittest.TestCase):
    def test_200_ping(self):
        res=self.client().get(route_ping)
        self.assertEqual(res.status_code,200)
        self.assertTrue(res.json["success"])
    
    def test_200_2tags(self):
        res=self.client().get(route_post+"?tags=tech,healthy")
        self.assertEqual(res.status_code,200)
         for post in self.assertTrueres.json["posts"]:
            self.assertTrue("tech" in post["tags"] or "healthy" in post["tags"])

if __name__=="__main__":
    unittest.main()