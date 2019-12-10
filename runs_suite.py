import unittest

from report import HTMLTestReportCN

suite=unittest.defaultTestLoader.discover("./scripts")

if __name__ == '__main__':
    with open("./report/report.html","wb") as f:
        runner = HTMLTestReportCN.HTMLTestRunner(stream=f)
        runner.run(suite)








