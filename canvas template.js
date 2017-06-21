var x;
var y;
var rect;
var root;
var mouseX;
var mouseY;
var FPS = 60;
function randomColour(){
	x = Math.floor((Math.random() * 10) + 0);
	if(x==0){
		randomcolour = 'green'
	} else if(x==1){
		randomcolour = 'red'
	} else if(x==3){
		randomcolour = 'white'
	} else if(x==4){
		randomcolour = 'yellow'
	} else if(x==5){
		randomcolour = 'pink'
	} else if(x==6){
		randomcolour = 'blue'
	} else if(x==7){
		randomcolour = 'orange'
	} else if(x==8){
		randomcolour = 'purple'
	} else if(x==9){
		randomcolour = 'brown'
	} else if(x==10){
		randomcolour = 'orange'
	} 
	return{
		colour:randomcolour
	};
}
function calculateMousePos(evt) {
	rect = canvas.getBoundingClientRect();
	root = document.documentElement;
	mouseX = evt.clientX - rect.left - root.scrollLeft;
	mouseY = evt.clientY - rect.top - root.scrollTop;
	return {
		x:mouseX,
		y:mouseY
	};
}
function circle(x,y,radius,colour){
	var tau = Math.PI*2;
	canvasContext.fillStyle = colour;
	canvasContext.beginPath();
	canvasContext.arc(x,y,radius,0,tau,true)
	canvasContext.fill();
}
function text(textt,sizefont,x,y,colour){
	canvasContext.fillStyle = colour;
	canvasContext.textAlign  = 'centre';
	canvasContext.font = sizefont;
	canvasContext.fillText(textt,x,y);
}
function draw(x,y,width,height,colour){
	canvasContext.fillStyle = colour;
	canvasContext.fillRect(x,y,width,height);
}
function input(){
	var xx = event.keyCode;
	console.log(xx,' was pressed');
	document.getElementById('text').value = xx;
	document.getElementById('text').innerHTML = xx;
}
function mouse(){
	console.log('mouse')
}
function drawEverything(){
	//canas code
}
window.onload = function(){
	console.log("Webpage loaded");
	canvas = document.getElementById('gameCanvas');
	document.addEventListener('keydown', input);
	canvas.addEventListener("mousedown", mouse, false);
	canvasContext= canvas.getContext("2d");
	canvas.addEventListener('mousemove',
	function(evt) {
				var mousePos = calculateMousePos(evt);
				y = mousePos.y;
				x = mousePos.x;
		});
	setInterval(drawEverything,1000/FPS);
}