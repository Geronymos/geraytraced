#ifdef GL_ES
precision mediump float;
#endif

#define PI 3.1415926535897932384626433832795

uniform float time;
uniform vec2 mouse;
uniform vec2 resolution;

struct Ray {
	vec3 origin;
	vec3 direction;
};

struct Sphere {
	vec3 origin;
	float radius;
};

struct Intersection {
	bool intersects;
	vec3 point1;
	vec3 normal; 
};

// np.clip = clamp()
vec3 x_rot(vec3 v, float r) {
	mat3 R = mat3(
		1.,0.,0.,
		0., cos(r), -sin(r),
		0., sin(r), cos(r)
	);
	return R * v;
}

vec3 y_rot(vec3 v, float r) {
	mat3 R = mat3(
		cos(r), 0., sin(r),
		0.,1.,0.,
		-sin(r),0.,cos(r)
	);
	return R * v;
}

vec3 z_rot(vec3 v, float r) {
	mat3 R = mat3(
		cos(r), -sin(r), 0.,
		sin(r), cos(r), 0.,
		0.,0.,1.
	);
	return R * v;
}

// return (is_intersecting, intersection_point, normal)
Intersection intersect(Ray ray, Sphere sphere) {
	Intersection intersection = {false, 0,0};

	vec3 L = sphere.origin - ray.origin;
	float tc = dot(L, ray.direction);

	if ( tc < 0.0 ) return intersection;

	float d = sqrt(pow(length(L),2) - pow(tc,2) );

	if ( d > sphere.radius ) return intersection;

	//solve for t1c
	float t1c = sqrt( pow(sphere.radius,2) - pow(d,2) );
	float t1 = tc - t1c;
	vec3 P1 = ray.origin + ray.direction * t1;
	// add second point

	vec3 normal = normalize(sphere.origin - P1);

	intersection.intersects = true;
	intersection.point1 = P1;
	intersection.normal = normal;

	return intersection;
}

void main( void ) {	

	vec2 uv = gl_FragCoord.xy / resolution.xy;
	vec2 rotation = uv - 0.5;
	vec2 umouse = mouse.xy / resolution.xy;

	struct Ray player;
	player.origin = vec3(0.,0.,0.);
	player.direction = vec3(1.,0.,0.);

	struct Sphere sphere;
	sphere.origin = vec3(10.,0.,0.);
	sphere.radius = 4.;

	struct Ray ray;
	ray.origin = player.origin;
	ray.direction = y_rot(z_rot(player.direction, rotation.x * PI/2), rotation.y * PI/2);

	Intersection intersection = intersect(ray, sphere);

	float red = 0.1;
	float green = 0.1;
	float blue = 0.1;

	if ( intersection.intersects ) {

		red = dot(intersection.normal, vec3(1., umouse.x*2-1, umouse.y*-2-1)) *.1;
		green = dot(intersection.normal, vec3(1., sin(time)*4.,-4.)) *.1;
		
	}

	gl_FragColor = vec4( red, green, blue, 1.0);
	
}