def assert_comment(self,expect,response):
    self.assertIn(expect,response.json().get('msg'))
    self.assertEqual(200,response.status_code)
