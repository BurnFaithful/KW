import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
print(ul)
print(ul.text)
print(bs_obj.find("li"))
print(bs_obj.find("li").text)
print(bs_obj.findAll("li"))

# li = bs_obj.select("ul > li")
# print(li)
