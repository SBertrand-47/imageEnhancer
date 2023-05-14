// Create a variable to hold your canvas
let canvas;

function setup() {
  // Create your canvas and assign it to your variable
  canvas = createCanvas(windowWidth, windowHeight);
  // Move the canvas to the #canvas-container div
  canvas.parent('canvas-container');
  // Set the frame rate to limit the speed of drawing
  frameRate(30);
}

function draw() {
  // Use a semi-transparent background to create a trail effect
  background(0, 0, 0, 20);

  // Draw a circle with random position, size, and color
  fill(random(255), random(255), random(255));
  noStroke();
  ellipse(random(width), random(height), random(20, 100));
}

// Make the canvas responsive
function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}
