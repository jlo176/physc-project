Web VPython 3.2


# Rod Projectile & Split Simulation:
# This is an interactive 2D physics simulation meant to model the projectile motion and  rotation of a two-mass baton system. Additionally, the sepeartion of the two masses can be modeled as well if desired.

# Project Overview:
# This simulation demonstrates the fundamental physics of a two-mass baton system under uniform gravity. It visualizes how a rigid baton rotates independently around its Center of Mass (COM)  while the COM itself tracks a smooth, predictable parabolic trajectory. 
# The masses on either end of the rod are also tracked to visualize the rotation of the baton.

# A key feature is our mid-air splitting mechanism, where users are able to  sever the  rod connecting the masses during flight, observing how conservation of linear momentum and rotational tangential velocity dictate the post-split trajectorie of the two end masses. 


# Interactive Controls & Parameters:
# Adjust these slider values before launching the simulation to modify the setup:

# Ball 1 Mass (m_1) & Ball 2 Mass (m_2): Changes the masses of the respective balls. The COM will also automatically shift closer to the heavier mass dynamically. The radius of each sphere also scales with the mass, which is reflected in the simulation.
# Starting Speed (speed) & Angle (angle): Controls the initial velocity vector magnitude and launch angle of the COM.
# Starting Angular Speed (w): Sets the initial rotational speed (rad/s) of the baton spinning around its COM.
# Starting Axis of Orientation (th): Alters the initial spatial tilt/angle of the rod relative to the horizontal plane.
# Rod Length (L): Sets the total distance separating the centers of Ball 1 and Ball 2, ostensibly the length of the red rod.
# Starting Impulse (I): Dictates the magnitude of an instantaneous axial force that is applied directly to both masses when the "split rod" function is triggered, which drives the masses further apart.

# Action Buttons:
#Run / Pause: Toggles the time-dependent physics engine on and off. Sliders are disabled once Run is pressed  to maintain consistency.
#Split Rod: Sever the connection of the end masses mid-flight. Alternatively, you can click anywhere inside the canvas to trigger the split.
