export default {
  _Selenium_IDE_Recorder: "_Selenium_IDE_Recorder" in window,
  callSelenium: "callSelenium" in window,
  _selenium: "_selenium" in window,
  __selenium_evaluate: "__selenium_evaluate" in document,
  __selenium_unwrapped: "__selenium_unwrapped" in document,
  document_selenium: document.documentElement.getAttribute("selenium") !== null,
};
