#ifdef GL_ES
precision mediump float;
#endif

uniform float time;
uniform vec2 mouse;
uniform vec2 resolution;

void main( void ) {	
	vec2 uv = gl_FragCoord.xy / resolution.xy;
	vec2 umouse = mouse.xy / resolution.xy;

	bool cursor = length(uv - umouse) < .2;

	gl_FragColor = vec4( cursor, 0.0 , 0.0, 1.0);
	
}