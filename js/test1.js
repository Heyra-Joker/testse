var md5 = require("./md5");

function th() {
  let t = [
    "toFixed",
    "are",
    "from",
    "7148477Zvhvwg",
    "RBViU",
    "2206zFhabd",
    "npqMt",
    "3733190PAxtAC",
    "params",
    "join",
    "877500BkQoFz",
    "1106vFqiET",
    "180Sdjows",
    "sort",
    "intercepto",
    "afnxU",
    "encode",
    "WlpfQ",
    "WPaLL",
    "BYBvJ",
    "ZiIMA",
    "fromEntrie",
    "entries",
    "zNUqR",
    "getTime",
    "114584jJgnQG",
    "sSTIj",
    "map",
    "aWYsA",
    "tQoai",
    "195770HmlUEJ",
    "decode",
    "QuIYo",
    "yetUn",
    "toString",
    "KbQaB",
    "use",
    "request",
    "8RFobLa",
    "HHtdN",
    "HCCYy",
    "concat",
    "vXrWu",
    "url",
    "5355498qbvOQC",
    "iGlyD",
    "localeComp",
    "juVTJ",
  ];
  return (th = function () {
    return t;
  })();
}

function tb(t, e) {
  let n = th();
  return (tb = function (t, e) {
    return n[(t -= 241)];
  })(t, e);
}

function tx(t) {
  let e = tb,
    n = {};
  return (
    (n["tQoai"] = function (t, e) {
      return t === e;
    }),
    (n["HHtdN"] = function (t, e) {
      return t % e;
    }),
    (n["npqMt"] = function (t, e) {
      return t & e;
    }),
    (n["afnxU"] = function (t, e) {
      return t ^ e;
    }),
    (n["juVTJ"] = function (t, e) {
      return t & e;
    }),
    (n["iGlyD"] = function (t, e) {
      return t | e;
    }),
    (n["RBViU"] = function (t, e) {
      return t & e;
    }),
    t["map"]((t, r) =>
      n["tQoai"](n["HHtdN"](r, 3), 0)
        ? n["npqMt"](n["afnxU"](t, 123), 255)
        : n["tQoai"](n["HHtdN"](r, 3), 1)
        ? n["juVTJ"](n["iGlyD"](t, 177), 255)
        : n["afnxU"](n["RBViU"](t, 203), 89)
    )
  );
}

function tg(t) {
  let e = tb,
    n = {};
  return (
    (n["yetUn"] = function (t, e) {
      return t & e;
    }),
    (n["QuIYo"] = function (t, e) {
      return t + e;
    }),
    (n["WPaLL"] = function (t, e) {
      return t * e;
    }),
    t["map"]((t, r) =>
      n["yetUn"](n["QuIYo"](n["QuIYo"](t, n["WPaLL"](r, 17)), 3), 255)
    )
  );
}

function tI(t) {
  let e = tb;
  let n = {
    aWYsA: function (t, e) {
      return t(e);
    },
    WlpfQ: function (t, e) {
      return t(e);
    },
    KbQaB: function (t, e) {
      return t(e);
    },
  };
  let r = new TextEncoder().encode(t);
  console.log(r);
  let s = n["aWYsA"](tx, Array.from(r));
  console.log(s);
  let u = n["WlpfQ"](tg, s);
  console.log(u);
  let a = new TextDecoder().decode(new Uint8Array(u));
  const res_a= md5(a);
  console.log(md5(res_a))
}

// http://a
// a1c30ac1e90de04c11a11d96eafad41a
tI("/api/v1?t=1719124242&url=https%3A%2F%2Fhaijiao.com%2Fpost%2Fdetails%3Fpid%3D1379359");
