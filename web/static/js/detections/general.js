export default {
  window: {
    emit: !window.emit,
    spawn: !window.spawn,
    outerWidth: !window.outerWidth,
    outerHeight: !window.outerHeight,
  }, 
  navigator: {
    onLine: !navigator.onLine,
    plugins_length: navigator.plugins.length == 0,
  },
  Function: {
    bind: !Function.prototype.bind,
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
