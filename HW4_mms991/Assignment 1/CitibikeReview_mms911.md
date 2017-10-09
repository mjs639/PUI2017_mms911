## The Question

The research question is clear.
Jon is interested in comparing trip duration for subscribers and customers. Specifically, he is interested to find out if subscribers are less likely to have a trip duration that is less than 45 minutes compared to customers. 


## The Hypotheses

The null hypothesis put forward by Jon is forumulated in such a way that he will be able to cleary answer his research question. I would clean up the wording a little with the following edits,
	
> The proportion of members whose trip duration lasted 45 minutes or more in a single trip is equal to or greater than the proportion of customers whose trip duration lasted 45 minutes or more in a single trip.

It appears that the formulation of the Null and Alternative hypotheses match the verbal description of the hypotheses.

One thing to note and keep an eye on here is that Citi Bike subscribers are alloted 45 minutes for a single trip before usage fees kick in (they pay an extra charge if their trip duration is greater than 45 minutes).
Customers on the other hand are only alloted 30 minutes. So it will be interesting to see if subscribers, despite being alloted more time per trip, consistently take shorter trips compared to customers. The results of Jon's test could be quite surprising. More likely, however, is that the results will confirm that subscribers, repeat users who are likely more familiar with the fee structure compared to customers, are less likely to incure fees by going over their alloted time.


## The Data

Jon pulled in Citi Bike data from December 2016. The data contains the relevant variables needed to test Jon's hypothesis:
 * `Trip Duration`,
 * `User Type`, and
 * `Over45`,a user-defined binary variable which labels cases that had a trip duraction greater than or equal to 45 minutes as "Over45" and those cases whose trip duration was less than 45 as "Under45"



## The Statistical Test

__Option 1:__
Jon could test his hypothesis by conducting a two-sample Z-test of proportions. The formula for this test would be as follows:
Z = p(subs) - p(custs) / sqrt( p(all) x ( 1/n(subs) + 1/n(custs) ) )

$$ Z = \frac{p_{subs} - p_{custs}}{\sqrt{p_{all} * (\frac{1}{/n_{subs}} + \frac{1}{/n_{custs}})}} $$

One caveat with this approach is that the Z test expects the proportions of the variable of interest to be normally distributed. This may be a reasonable assumption but it should be checked. It's entirely possible that the `Trip duration` variable is normally distributed. However the `Over45` binary variable will not be normally distributed.

__Option 2:__
Given that Jon's has classfied each case into a binary, categorical variable (`Over45`) and is seeking to test if two groups differ on the rate at which they fall into these two categories (or proportion), it is reasonable for Jon to use the $\chi^2$ to test for equality of proportions.


## Other Interesting Variations

Since the alloted time per trip is different for the two groups (subscribers = 45 mins, customers = 30 mins), it may be interesting to ask a different question that takes this into considerations. For example, Jon might ask,
> "Are subscribers less likely to go over their alloted time compared to customers?"

