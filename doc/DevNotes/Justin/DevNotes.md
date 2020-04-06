# January 20, 2020
## I read through previous publications in order to familiarize myself with the project.
## We started practicing the procedure to locate an accelerometer within a device
	- We placed the accelerometer on a turntable bouded in place by a rectangular frame
	- The device was moved between runs and the force experienced in each run was recorded.
	- 10 trials were done in the x axis of the device
	- The device stopped working during the experiment
# January 27, 2020
## We continued the experiment in the x direction and then in the y direction
	- The position was estimated using 2 methods:
		-- linear regression
		-- averaging over the solutions of several linear system using the difference between the radius and force directions
# February 3, 2020
## We started the Acceleration to Position Converter Project
	- We created a program. Its a converter from acceleration to position, it uses discrete integration
	- We created another program that graphs data as a 3D scatter plot
# February 10, 2020
## We made changes to the code of the previous session so that it would be more automated.
	- It now input the raw data file and creates a position file to be used by the other program.
	- We tested out the code with some real data, drift is a big problem. We tried to fix it with someerror margin but to no avail.