import unittest
from classes import WebApp
from mock import Mock  # ReturnValues


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.mockFieldStorage = Mock()
        self.mockHtmlGenerator = Mock({
            'h1': 'heading',
            'link': 'link',
            'list': 'navList',
            'table': 'table',
            'div': 'div'
        })
        self.mockCanvasserManager = Mock({
            'getEveryoneFromFilters': [['everyone']],
            'getCanvasserAttributeNames': ['names']
        })
        self.mockedWebApp = WebApp.WebApp(self.mockFieldStorage, self.mockHtmlGenerator, self.mockCanvasserManager)

    def _assertContains(self, needle, haystack):
        contains = haystack.count(needle) > 0
        self.assertTrue(contains)

    def _getMockedOutput(self, pageSlug=None):
        if pageSlug is not None:
            self.mockFieldStorage = Mock({'getvalue': pageSlug})
            self.mockedWebApp = WebApp.WebApp(
                self.mockFieldStorage,
                self.mockHtmlGenerator,
                self.mockCanvasserManager
            )
        return self.mockedWebApp.getOutput()

    def testMakesCanvassersLink(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(2, 'link', 'app.py?function=canvassers', 'Manage Canvassers', None)

    def testMakesList(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(4, 'list', ['link', 'link'])

    def testMarksNavLinkAsCurrent(self):
        self._getMockedOutput('canvassers')
        self.mockHtmlGenerator.mockCheckCall(2, 'link', 'app.py?function=canvassers', 'Manage Canvassers', 'current')

    def testMakesHeaderLink(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(0, 'link', 'app.py', 'OHCFS', 'current')

    def testUsesLinkToMakeHeading(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(1, 'h1', 'link')

    def testMakesDailyLink(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(3, 'link', 'app.py?function=daily', 'Daily', None)

    def testGetsEveryoneFromFilters(self):
        self._getMockedOutput('canvassers')
        self.mockCanvasserManager.mockCheckCall(1, 'getEveryoneFromFilters', [])

    def testMakesTableFromEveryone(self):
        self._getMockedOutput('canvassers')
        self.mockHtmlGenerator.mockCheckCall(6, 'table', [['everyone']], ['names'])

    def testOutputsCanvasserList(self):
        output = self._getMockedOutput('canvassers')
        self._assertContains('table', output)

    def testGetsCanvasserAttributeNames(self):
        self._getMockedOutput('canvassers')
        self.mockCanvasserManager.mockCheckCall(0, 'getCanvasserAttributeNames')

    def testSurroundsHeadWithDiv(self):
        self._getMockedOutput()
        self.mockHtmlGenerator.mockCheckCall(
            5,
            'div',
            '<link rel="stylesheet" type="text/css" href="../style.css">headingnavList',
            'header'
        )
