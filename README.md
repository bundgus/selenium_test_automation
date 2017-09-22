# Test Automation with Selenium

Don’t forget to edit selenium_base.py

```python
self.driver = webdriver.Chrome("C:/path/to/chromedriver")
self.login = 'replace me'
self.password = 'replace me'
```

Execute the test
```bash
python test_meta_shopping_report.py
```

The log folder will contain a log in csv format with the following columns:

* a timestamp for when the overall test started
* the timestamp for the specific test
* the class and function name of the specific test
* and the elapsed time for the specific test 

In the log folder there will also be a time-stamped screen shot of the report page taken for each test run.
