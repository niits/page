"use strict";

export default { 
    user_agent: navigator.userAgent.toLowerCase().includes("phantom"),
    _phantom: window._phantom == true,
    callPhantom: window.callPhantom == true,
    __phantomas: window.__phantomas == true,
 }