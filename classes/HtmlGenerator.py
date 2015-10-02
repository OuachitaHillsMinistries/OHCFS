class HtmlGenerator:
    def _element(self, name, content, props=None):
        propsMarkup = self._propsMarkup(props)

        return '<{}{}>{}</{}>'.format(name,propsMarkup,content,name)

    def _propsMarkup(self, props):
        propsMarkup = ''
        if props != None:
            for prop, value in props.iteritems():
                propsMarkup += ' {}="{}"'.format(prop, value)
        return propsMarkup

    def h1(self, content):
        return self._element('h1',content)

    def _li(self, content):
        return self._element('li',content)

    def list(self, items):
        itemMarkup = ''
        for item in items:
            itemMarkup += self._li(item)
        return self._element('ul',itemMarkup)

    def link(self, url, text, classes=None):
        if classes==None:
            props = {'href':url}
        else:
            props = {'href':url,'class':classes}
        return self._element('a',text,props)

    def table(self, tabularData):
        htmlBody = self._tableBody(tabularData)
        return self._element('table', htmlBody)

    def _tableBody(self, tabularData):
        htmlRows = ''
        for row in tabularData:
            htmlRows += self._tableRow(row)
        return self._element('tbody', htmlRows)

    def _tableRow(self, row):
        htmlCells = ''
        for cell in row:
            htmlCells += self._tableCell(cell)
        return self._element('tr', htmlCells)

    def _tableCell(self, cell):
        return self._element('td', cell)
