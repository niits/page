export default {
  user_agent: navigator.userAgent.includes("HeadlessChrome"),
  missing_window_chrome:
    navigator.userAgent.includes("Chrome") && window.chrome == null,
};
