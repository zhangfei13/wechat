document.body.onload=game;        //启动游戏

function game(){
    init();            //初始化元素对象
    //loops();        //游戏函数
    createParticleCanvas();
}

function backDraw(){        //背景，静态元素
    bgImgae = new Image();
    bgImgae.src="/static/img/bg.jpg";
    bgImgae.onload = function(){
        bgCtx.drawImage(bgImgae, 0, 0);
    };
}

function init(){        //初始化
    canvas.addEventListener("click", getClickPosition,false);        //监听鼠标点击
    canvas.addEventListener("mousemove", getMovePosition,false);        //监听鼠标移动
    canvas.addEventListener('keydown', getKeyDown, false);        //监听键盘
    //聚焦canvas画布时触发
    canvas.focus();
    //backDraw();        //初始化静态元素，执行一次

}

function loops(){        //循环游戏动态元素
    stop = requestAnimFrame(loops);
    ctx.fillStyle="rgba(110,30,21,0.1)";
    ctx.rect(0,0,canvas.width/10,canvas.width/10);
    ctx.fill();
}

function createParticleCanvas() {
	// 创建用于粒子效果的Canvas
	particleCanvas = document.createElement("canvas1");
	particleCtx = particleCanvas.getContext("2d");
	// Canvas的大小
	particleCanvas.width = window.innerWidth;
	particleCanvas.height = window.innerHeight;
	// Canvas的位置
	particleCanvas.style.position = "absolute";
	particleCanvas.style.top = "0";
	particleCanvas.style.left = "0";
	// 设置Canvas在元素的上面
	particleCanvas.style.zIndex = "1001";
	// 确保它下面的其他元素是可点击的
	particleCanvas.style.pointerEvents = "none";
	// 把Canvas添加到页面中
	document.body.appendChild(particleCanvas);

	particleCtx.beginPath()
    particleCtx.moveTo(0,0)
    particleCtx.lineTo(particleCanvas.width, particleCanvas.height)
    particleCtx.stroke()
}