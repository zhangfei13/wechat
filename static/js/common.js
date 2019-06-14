function getMovePosition(ev){         //返回移动坐标
    if (ev.layerX || ev.layerX == 0){
        moveX = ev.layerX;
        moveY = ev.layerY;
    }else if (ev.offsetX || ev.offsetX == 0) { // Opera
        moveX = ev.offsetX;
        moveY = ev.offsetY;
    }
}

function getClickPosition(ev){        //返回点击坐标
    clickChip=1;
    if(ev.layerX || ev.layerX == 0){
        clickX = ev.layerX;
        clickY = ev.layerY;
    }else if (ev.offsetX || ev.offsetX == 0) { // Opera
        clickX = ev.offsetX;
        clickY = ev.offsetY;
    }
}

function isTrueListener(x,y){        //判断坐标是否当前位置，返回true or false
    if(ctx.isPointInPath(x,y)){
        return true;
    }else{
        return false;
    }
}

function getKeyDown(e) {            //返回鼠标按下的键值
    keyDown=e.keyCode ? e.keyCode :e.which;
}

function requestAnimFrame(callback,element){        //游戏刷新速率
        return window.setTimeout(callback, 1000 / 60);
};

function getXMLHttpRequest(){            //返回适用当前环境request对象，数据交互
    try{
        try{
            return new ActiveXobject("Microsoft.XMLHTTP");
        }
        catch(e){
            return new ActiveXobject("Msxm12.XMLHTTP");
        }
    }
    catch(e){
        return new XMLHttpRequest();
    }
}