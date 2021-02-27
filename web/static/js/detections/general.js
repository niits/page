"use strict";

export default {
  window: {
    mising_outer_width: !window.outerWidth,
    mising_outer_height: !window.outerHeight,
  }, 
  navigator: {
    mising_onLine: !navigator.onLine,
    empty_plugins: navigator.plugins.length == 0,
  },
  Function: {
    mising_bind: !Function.prototype.bind,
    toString: {
      bind:
        Function.prototype.bind.toString().replace(/bind/g, "Error") !=
        Error.toString(),
      toString,
      toString:
        Function.prototype.toString.toString().replace(/toString/g, "Error") !=
        Error.toString(),
    },
  },
};
