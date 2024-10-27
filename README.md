# asteroids

## venv
Install a virtual environment. This only has to be complete once. You should see a ./venv/ directory created.
`python3 -m venv venv`

This application was developed with a virtual environment. Be sure to use the virtual environment by using the following command.
`source venv/bin/activate`

When the virtual environment is activated, you should see "(venv)" at the beginning of your terminal prompt.

## install library requirements into venv
`pip install -r requirements.txt`

## run
`python3 main.py`

## future ideas to add
* Add a scoring system
* Implement multiple lives and respawning
* Add an explosion effect for the asteroids
* Add acceleration to the player movement
* Make the objects wrap around the screen instead of disappearing
* Add a background image
* Create different weapon types
* Make the asteroids lumpy instead of perfectly round
* Make the ship have a triangular hit box instead of a circular one
* Add a shield power-up
* Add a speed power-up
* Add bombs that can be dropped
