"use strict";

export default {
  webdriver: "webdriver" in window,
  __webdriver_script_fn: "__webdriver_script_fn" in document,
  __driver_evaluate: "__driver_evaluate" in document,
  __webdriver_evaluate: "__webdriver_evaluate" in document,
  __fxdriver_evaluate: "__fxdriver_evaluate" in document,
  __driver_unwrapped: "__driver_unwrapped" in document,
  __webdriver_unwrapped: "__webdriver_unwrapped" in document,
  __fxdriver_unwrapped: "__fxdriver_unwrapped" in document,
  __webdriver_script_func: "__webdriver_script_func" in document,
  document_webdriver:
    document.documentElement.getAttribute("webdriver") !== null,
  document_driver: document.documentElement.getAttribute("driver") !== null,
  window_document_webdriver:
    window.document.documentElement.getAttribute("webdriver") !== null,
};
