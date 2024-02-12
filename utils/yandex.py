from selenium import webdriver
import time
from utils.keyPress import F12

def download_yapanorama(x, y, i=0):
    with webdriver.Chrome() as browser_driver:
        browser_driver.set_page_load_timeout(8)
        browser_driver.get(r"file:///D:/PetProjects/panoramaWalker/yandex/main.html")
        time.sleep(1)
        js_code = f"""var locateRequest = ymaps.panorama.locate([{x}, {y}]);
                    locateRequest.then(
                      function (panoramas) {{
                        if (panoramas.length) {{
                          console.log("Panorama found " + panoramas[0]);       
                        }} else {{
                          console.log("No panoramas were found for this point.");    
                        }}
                      }},
                      function (err) {{
                        console.log("An error occurred while trying to get the panorama.");
                        console.log(err);
                      }}
                    );
                    var player = null;
                    locateRequest.then(
                      function (panoramas) {{
                        if (panoramas.length) {{
                          document.player = new ymaps.panorama.Player('div_id', panoramas[0], {{
                                // direction - gaze direction.
                                direction: [0, -50]
                              }});
                        }} else {{
                          console.log("There are no panoramas at this location.");
                        }}
                      }}
                    );"""

        browser_driver.execute_script(js_code)
        time.sleep(1)
        F12()
        js_expand = """var button = document.querySelector('.ymaps-2-1-79-islets_round-button__icon');
              if (button) {
                button.click();
              } else {
                console.log("Button not found");
              }"""
        browser_driver.execute_script(js_expand)
        time.sleep(1)
        browser_driver.save_screenshot(f'panorama_screenshot_{i}.png')

