# selenium

- Selenium 的功能
  - 框架底层使用JavaScript 模拟真实用户对浏览器进行操作。测试脚本执行时，浏览器自动按照脚本代码做出点击，输入，打开，验证等操作，就像真实用户所做的一样，从终端用户的角度测试用户程序
  - 可用于较难的爬虫：动态JS 加载、登录验证、表单提交等
  - 使用简单，可使用Python、Java 等多种语言编写用户脚本

- 为什么要学习Selenium
  - requests 爬虫局限性较大，分析困难、被封禁概率高
  - 可用于较难爬虫
    - 伪装成真实的浏览器，被封禁的概率更低
    - 动态JS 加载
    - 登录验证
    - 表单提交等
- Selenium 缺点，相比requests，性能比较差，爬取的慢

- Selenium 的框架

Windows/MAC

Python爬虫代码（依赖selenium库）-> 浏览器驱动（ChromeDriver）-> 真实的浏览器（Chrome）





「定位页面元素的8种主要方式」

- id定位：driver.find_element_by_id(value)
- name属性值定位：driver.find_element_by_name(value)
- 类名定位： driver.find_element_by_class_name(value)
- 标签名定位： driver.find_element_by_tag_name(value)
- 链接文本定位：driver.find_element_by_link_text(value)
- 部分链接文本：driver.find_element_by_partial_link_text(value)
- xpath路径表达式：driver.find_element_by_xpath(value)
- css选择器：driver.find_element_by_css_selector(value)



定位元素后，需要对网页进行各种操作，比如点击、刷新、保存等。

点击展开新的页面，点击方法：element.click()

其他主要操作方法：

- 请求某个url：driver.get(url)
- 刷新页面操作：refresh()
- 回退到之前的页面：back()
- 前进到之后的页面：forward()
- 获取当前访问页面url：current_url
- 获取当前浏览器标题：title
- 保存图片：get_screenshot_as_png()/get_screenshot_as_file(file)
- 网页源码：page_source

























