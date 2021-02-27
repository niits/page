import fingerprint from "./detections/index.js";

var xhr = new XMLHttpRequest();

xhr.open("POST", "/", true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.send(
  JSON.stringify({
    data: {
      fingerprint,
      hash_id,
    },
  })
);
