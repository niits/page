"use strict";

export default {
  navigator: {
    user_agent: navigator.userAgent.toLowerCase().includes("headlesschrome"),
    missing_window_chrome:
      navigator.userAgent.includes("Chrome") && window.chrome == null,
  },
};
