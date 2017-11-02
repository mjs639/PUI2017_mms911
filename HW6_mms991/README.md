#HW6_mms991

# Group members
Michael Sampson
Bianca Bruso
Gokmen Dedemen

## Assignment 1
The code for this assignment was written and contributed to by Bianca and Gokmen.
I reviewed the code for accuracy and understanding but did not contribute a single line.

The assignment asked us to grab data from two souces: 1) energy use for NYC buildings and 2) building attributes (number of units) for those same buildings. The records were connected using BBL (borough block and lot number) as the key

Once the data was merged, we were tasked with modelling energy use intensity (EUI) by the number of units in the building (and vice versa).
The data fit better when we model EUI on Units instead of the other way around (GOF: chi2 for EUI on units < chi2 for Units on EUI).

We also tested a third model that included second order polynomial term for number of units in the buildings.
This model is slightly more complex than the one with just the number of units and produced a slightly high R-squared value.
However, to asses if the added complexity was worth it, we performed a likelihood ratio test.
The results of this test (LR test statistic = -6787.7135119358154, p-value = 1) suggest that we fail to reject the null hypothesis that states the more parsimonious, less restricted model fits the data the best.

Note:
I started working on this independent but got kicked off the CUSP data facility and couldn't reconnect.
I posted a version of my draft of the homework as well.
