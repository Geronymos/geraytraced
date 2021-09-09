#include <SFML/Graphics.hpp>
#include <iostream>

using namespace std;

// from https://glusoft.com/tutorials/sfml/shader-example
int main() {
	float winW = 800;
	float winH = 600;

	sf::Vector3f player_position = sf::Vector3f(0.,0.,0.);

	sf::RenderWindow window(sf::VideoMode(winW, winH), "SFML Shader Example");
	// window.setMouseCursorVisible(false); // hide the cursor

	// Create a texture and a sprite for the shader
	sf::Texture tex;
	tex.create(winW, winH);
	sf::Sprite spr(tex);

	sf::Shader shader;
	shader.loadFromFile("fire.glsl", sf::Shader::Fragment); // load the shader

	if (!shader.isAvailable()) {
		std::cout << "The shader is not available\n";
	}

	// Use a timer to obtain the time elapsed
	sf::Clock clk;
	clk.restart(); // start the timer

	while (window.isOpen()) {
		// Event handling
		sf::Event event;

		while (window.pollEvent(event)) {
			switch ( event.type ) {
				case sf::Event::KeyPressed: 
					switch (event.key.code) {
						case sf::Keyboard::W:
							cout << "W" << endl; 
							player_position.x++;
							break;
						case sf::Keyboard::A:
							cout << "A" << endl;
							player_position.y--; 
							break;
						case sf::Keyboard::S:
							cout << "S" << endl;
							player_position.x--; 
							break;
						case sf::Keyboard::D:
							cout << "D" << endl;
							player_position.y++; 
							break;
					}
					break;
				case sf::Event::Resized: 
					// Set the resolution parameter (the resoltion is divided to make the fire smaller)
					winW = event.size.width;
					winH = event.size.height;
					cout << winW << "x" << winH << endl;
					shader.setUniform("resolution", sf::Vector2f(winW, winH));
			}
				
		}

		// Set the others parameters who need to be updated every frames
		shader.setUniform("time", clk.getElapsedTime().asSeconds());

		shader.setUniform("player_pos", player_position);

		sf::Vector2i mousePos = sf::Mouse::getPosition(window);
		shader.setUniform("mouse", sf::Vector2f(mousePos.x, winH - mousePos.y));
		// Draw the sprite with the shader on it
		window.clear();
		window.draw(spr, &shader);
		window.display();
	}

	return 0;
}