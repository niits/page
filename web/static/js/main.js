import fingerprint from "./detections/index.js";
import flatten from "./util.js";

function sendFingerprint(reasons) {
  var xhr = new XMLHttpRequest();

  xhr.open("POST", "", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(
    JSON.stringify({
      data: {
        detected_by: reasons,
        fingerprint,
        hash_id,
      },
    })
  );
}

function detect() {
  let reasons = [];
  let start = Date.now();
  alert("Press OK");
  let elapse = Date.now() - start;
  if (elapse < 15) {
    reasons.push("timer");
  }

  var err;
  try {
    null[0]();
  } catch (e) {
    err = e;
  }
  if (indexOfString(err.stack, "phantomjs") > -1) {
    reasons.push("err.stack");
  }

  if (reasons.length > 0) {
    sendFingerprint(reasons);
  }
}

function checkFingerprint() {
  let flatted = flatten(fingerprint);

  let reasons = Object.entries(flatted)
    .filter(function (entry) {
      return entry[1];
    })
    .map(function (item) {
      return item[0];
    });

  if (reasons.length > 0) {
    sendFingerprint(reasons);
  }
}

if (window.addEventListener) {
  window.addEventListener("load", checkFingerprint, false);
} else if (window.attachEvent) {
  window.attachEvent("onload", checkFingerprint);
}

document.getElementById("button").onclick = detect;
