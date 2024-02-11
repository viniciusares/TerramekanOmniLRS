# 1st cell, imports and function
# wheel trace, height of x_section

import math
import numpy

def height_x_section(y,max_height,AoR,width):
  y_lim = max_height/(2*numpy.tan(AoR))
  if abs(y)<abs(width/2-y_lim):
    print(f'For y equal {y}, Height is max_height: {max_height}')
    return max_height
  elif (abs(y)>abs(width/2-y_lim) and abs(y)<abs(width/2+y_lim)):
    y_excess = abs(y) - (width/2-y_lim)
    height_discount = y_excess*numpy.tan(AoR)
    height = max_height - height_discount
    print(f'For y equal {y}, Height is {height}')
    return height
  elif abs(y)>abs(width/2+y_lim):
    print(f'For y equal {y}, outside bounds, Height is 0')
    return 0

height_x_section(y = -5,max_height = 2,AoR = 26.5*(numpy.pi/180),width = 10)


# 1.5 cell
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def getZ_trazepe_in3D(x, y, trapeze_height, AoR, width): #def height_x_section #5 #6

  trapeze_height = -0.6 + 1.4*np.sin(1.3 * x)
  trapeze_height=depth_f_of_x[y_idx]

  wall_limits = abs(trapeze_height) / (2 * np.tan(AoR))
  wall_limit_inner = width/2 -wall_limits
  wall_limit_outer = width/2 +wall_limits

  if abs(y) < wall_limit_inner:  # trapeze mesa region, close to center #5
    height = trapeze_height
  elif abs(y) > wall_limit_outer:  # outside trapeze limit, then zero
      height = 0
  else: # colapsed wall region
      y_excess = abs(y) - wall_limit_inner # variable to build a triangular region
      height_discount = y_excess * np.tan(AoR) # the amount that differs from mesa height
      height = trapeze_height - height_discount # this is for an "up" block of sand
      if trapeze_height < 0: # then it is a trench
        height = trapeze_height + height_discount # "up" block is overwritten to create a trench

  return height

def getZ_trazepe_inYZ_arrayX(x_values, y, trapeze_height, AoR, width):
  Z = np.zeros_like(x_values) #2
  for i in range(len(x_values)): #2
    Z[i] = getZ_trazepe_inYZ(x_values[i], trapeze_height, AoR, width)
  return Z

def getZ_trazepe_inYZ(y, trapeze_height, AoR, width): #def height_x_section #3 #4
  wall_limits = abs(trapeze_height) / (2 * np.tan(AoR))
  wall_limit_inner = width/2 -wall_limits
  wall_limit_outer = width/2 +wall_limits

  if abs(y) < wall_limit_inner:  # trapeze mesa region, close to center
    return trapeze_height
  elif abs(y) > wall_limit_outer:  # outside trapeze limit, then zero
    return 0
  else: # colapsed wall region
    y_excess = abs(y) - wall_limit_inner # variable to build a triangular region
    height_discount = y_excess * np.tan(AoR) # the amount that differs from mesa height
    height = trapeze_height - height_discount # this is for an "up" block of sand
    if trapeze_height < 0: # then it is a trench
      height = trapeze_height + height_discount # "up" block is overwritten to create a trench
    return height

def getZ_trazepe_inYZ_array(y_values, trapeze_height, AoR, width): #2
  Z = np.zeros_like(y_values) #2
  for i in range(len(y_values)): #2
    Z[i] = getZ_trazepe_inYZ(y_values[i], trapeze_height, AoR, width)
  return Z

# 2nd cell, rectangle colapsed to trapeze
# Generate y values from -10 to 10
y_values = np.linspace(-10, 10, 100)
# Calculate corresponding heights
AoR=26.5 * (np.pi / 180)
#height_values = -height_x_section(y_values, max_height=2, AoR=26.5 * (np.pi / 180), width=10)
height_values = -getZ_trazepe_inYZ_array(y_values, trapeze_height=2, AoR=AoR, width=10) #2

# Plotting
plt.plot(y_values, height_values)
plt.title('Wheel Trace - Height of Cross Section')
plt.xlabel('y')
plt.ylabel('Height')
plt.grid(True)

height_values2 = -getZ_trazepe_inYZ_array(y_values, trapeze_height=1, AoR=AoR, width=10) #2
plt.plot(y_values, height_values2)

height_values3 = -getZ_trazepe_inYZ_array(y_values, trapeze_height=0.1, AoR=AoR, width=10) #2
plt.plot(y_values, height_values3)

height_values4 = -getZ_trazepe_inYZ_array(y_values, trapeze_height=-1, AoR=AoR, width=10) #2
plt.plot(y_values, height_values4)

height_values5 = -getZ_trazepe_inYZ_array(y_values, trapeze_height=-0.1, AoR=AoR, width=10) #2
plt.plot(y_values, height_values5)

fig = plt.figure()
ax = fig.add_subplot(212)

# 3rd cell, 3D
x_coords = np.linspace(-10, 10, 80) # Generate x values as a sine wave
y_coords = np.linspace(-12, 12, 50) # Generate y values from -10 to 10
XX,YY = np.meshgrid(x_coords, y_coords) # Create a meshgrid from x and y

depth_f_of_x = -0.6 + 1.4*np.sin(1.3 * x_coords)
height_values = np.zeros_like(XX) # Calc heights using height_x_section function
AoR=26.5 * (np.pi / 180)

for x_idx in range(XX.shape[0]):
    for y_idx in range(YY.shape[1]):
      z=getZ_trazepe_inYZ(y=YY[x_idx, y_idx], trapeze_height=depth_f_of_x[y_idx], AoR=AoR, width=10)
      height_values[x_idx, y_idx] = z

fig = plt.figure()
ax = fig.add_subplot(131, projection='3d')
ax.set_title('Wheel Trace based on Angle of Repose')
ax.plot_surface(XX, YY, height_values, cmap='copper') # Plotting the surface plot
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('Height')
ax.set_zlim(-3.5, 2.5) # Reduce the scale of the z-axis and set axis limits
ax.view_init(elev=12, azim=85)  # Adjust elev and azim as needed

ax = fig.add_subplot(132, projection='3d')
ax.plot_surface(XX, YY, height_values, cmap='copper')
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('Height')
ax.view_init(elev=12, azim=5)  # Adjust elev and azim as needed
ax.set_zlim(-2.0, 1.5)

ax = fig.add_subplot(133, projection='3d')
ax.plot_surface(XX, YY, height_values, cmap='copper')
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('Height')
ax.view_init(elev=0, azim=0)  # Adjust elev and azim as needed
ax.set_ylim(-7.5, 7.5)
ax.set_zlim(-2.4, 1.0)

# 4th cell, cross sections
x_coords = np.linspace(-10, 10, 100)
y_coords = np.linspace(-12, 12, 80)
XX, YY = np.meshgrid(x_coords, y_coords)

depth_f_of_x = -0.4 + 1.4*np.sin(1.3 * x_coords)
height_values = np.zeros_like(XX)
AoR = 26.5 * (np.pi / 180)

for x_idx in range(XX.shape[0]):
    for y_idx in range(YY.shape[1]):
      z=getZ_trazepe_inYZ(y=YY[x_idx, y_idx], trapeze_height=depth_f_of_x[y_idx], AoR=AoR, width=10)
      height_values[x_idx, y_idx] = z

fig = plt.figure()

# Plot the original 3D surface plot
ax = fig.add_subplot(231, projection='3d')
ax.set_title('Original 3D Surface Plot')
ax.plot_surface(XX, YY, height_values, cmap='copper')
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('Height')
ax.set_zlim(-3.5, 2.5)
ax.view_init(elev=30, azim=45)

# Plot cross-section along the x-axis
ax = fig.add_subplot(232)
plt.title('Cross-section YZ')
plt.plot(y_coords, height_values[:, 29])
plt.plot(y_coords, height_values[:, 28])
plt.plot(y_coords, height_values[:, 25])
plt.plot(y_coords, height_values[:, 23])
plt.plot(y_coords, height_values[:, 50])
plt.xlabel('y')
ax.set_xlim(-7, 7) # actually the axis height
ax.set_ylim(-1.9, 0.9) # actually the axis height
plt.ylabel('Height')

# Plot cross-section along the y-axis
ax = fig.add_subplot(233)
plt.title('Cross-section XZ')
plt.plot(x_coords, height_values[21, :])
plt.plot(x_coords, height_values[20, :])
# height_values[x, :] #could try x=28,39,41,54
plt.plot(x_coords, height_values[60, :])
plt.plot(x_coords, height_values[61, :])
plt.xlabel('x')
plt.ylabel('Height')

# Plot cross-section along the z-axis
ax = fig.add_subplot(234)
plt.title('Cross-section along the z-axis')
contour_plot = plt.contour(XX, YY, height_values, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
ax.set_xlim(-6.2, 3.65)
ax.set_ylim(-17.5, 17.5)


plt.tight_layout()
plt.show()