const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");

const size = [500,500];

canvas.width = size[0];
canvas.height = size[1];

time_start = new Date().getTime()

// ctx.fillRect(10,10,10,10);

function myShader(x,y,t) {
  const uv = [x/size[0],y/size[1]];
  const r = (Math.sin(uv[0]*10+t)+1)/2*255;
  const g = (Math.sin(uv[1]*10+t)+1)/2*255;
  return [r,g,0];
}

function draw() {
  const t = (new Date().getTime() - time_start) /1000;
  console.log(t);
  for (var x=0; x < size[0]; x++) {
    for (var y=0; y < size[1]; y++) {
      ctx.fillStyle = `rgb(${myShader(x,y,t).join(",")})`
      ctx.fillRect(x,y,1,1);
    }
  }
  
  requestAnimationFrame(draw);
}

draw();
// while (true) {
//   draw();
// }