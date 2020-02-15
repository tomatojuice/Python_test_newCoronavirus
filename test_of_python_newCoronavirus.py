from pyecharts import options as opts
from pyecharts.charts import Map
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# このパスはchromedriverをダウンロードしたパスを設定。
# chromedriverとchromeのバージョンがあってないとエラーになる
browser = webdriver.Chrome(executable_path='C:\\Users\\tomat\\chromedriver_win32\\chromedriver.exe')
wait = WebDriverWait(browser, 10)

# 新浪のサイトから情報取得
browser.get('https://news.sina.cn/zt_d/yiqing0121')

provinces = []
values = []
for i in range(2,69,2):
    province = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mylist > div.mapCont.mapMoreCont > div.m_list > div:nth-child({}) > span.c1'.format(i))))
    provinces.append(province.text)
    value = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mylist > div.mapCont.mapMoreCont > div.m_list > div:nth-child({}) > span.c2'.format(i))))
    values.append(value.text)


def map_visualmap() -> Map:
    c = (
        Map()
        .add("", [list(z) for z in zip(provinces, values)], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="中国のリアルタイムのコロナウイルス感染者数"),
            visualmap_opts=opts.VisualMapOpts(max_=600),
        )
    )
    return c.render()

map_visualmap()
f