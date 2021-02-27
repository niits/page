"use strict";

export default {
  webdriver: 'webdriver' in window,
  _Selenium_IDE_Recorder: '_Selenium_IDE_Recorder' in window,
  callSelenium: 'callSelenium' in window,
  _selenium: '_selenium' in window,
  __webdriver_script_fn: '__webdriver_script_fn' in document,
  __driver_evaluate: '__driver_evaluate' in document,
  __webdriver_evaluate: '__webdriver_evaluate' in document,
  __selenium_evaluate: '__selenium_evaluate' in document,
  __fxdriver_evaluate: '__fxdriver_evaluate' in document,
  __driver_unwrapped: '__driver_unwrapped' in document,
  __webdriver_unwrapped: '__webdriver_unwrapped' in document,
  __selenium_unwrapped: '__selenium_unwrapped' in document,
  __fxdriver_unwrapped: '__fxdriver_unwrapped' in document,
  __webdriver_script_func: '__webdriver_script_func' in document,
  selenium: document.documentElement.getAttribute("selenium") !== null,
  webdriver: document.documentElement.getAttribute("webdriver") !== null,
  driver: document.documentElement.getAttribute("driver") !== null
};
