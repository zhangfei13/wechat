var canvas = document.getElementById("canvas");

var ctx = canvas.getContext("2d");

var bgCanvas = document.getElementById("bg-canvas");

var bgCtx = bgCanvas.getContext("2d");

var staticCanvasWidth = canvas.width;

var staticCanvasHeight = canvas.height;

var bgImgae;

var clickX;

var clickY;

var moveX;

var moveY;

var keyDown=null;

var canvasWidth = canvas.offsetWidth;

var canvasHeight = canvas.offsetHeight;


var particleCanvas, particleCtx;