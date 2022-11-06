# This is a learn project with automated check and print with best solution avaliable
weight = 41.5

flat_charge_gs = 20
flat_charge_gsp = 125
flat_charge_ds = 0

cost_gs = ''
cost_gsp = flat_charge_gsp
cost_ds = ''

# Ground Shipping
if weight <= 2:
  cost_gs = weight * 1.5 + flat_charge_gs
elif weight <= 6:
  cost_gs = weight * 3 + flat_charge_gs
elif weight <= 10:
  cost_gs = weight * 4 + flat_charge_gs
else: cost_gs = weight * 4.75

print ('Ground Shipping: ', cost_gs, '$')

# Ground Shipping Premium
print ('Ground Shipping Premium: ', cost_gsp, '$')

# Drone Shipping
if weight <= 2:
  cost_ds = weight * 4.5 + flat_charge_ds
elif weight <= 6:
  cost_ds = weight * 9 + flat_charge_ds
elif weight <= 10:
  cost_ds = weight * 12 + flat_charge_ds
else: cost_ds = weight * 14.25

print ('Drone Shipping: ', cost_ds, '$')

# Check the best solution

if cost_gs > cost_ds < cost_gsp:
  print ('\nDrone Shipping recommended!')
elif cost_gs < cost_ds < cost_gsp:
  print ('\nGround Shipping recommended!')
else: print ( '\nGround Shipping Premium recommended!')
