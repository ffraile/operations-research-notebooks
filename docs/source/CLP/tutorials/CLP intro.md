#%% md
# Continuous Linear Programming
## Definition
Continuous Linear Programming (CLP) spans a wide set of OR problems that can be modeled based on the following assumptions:
- Unknown variables are continuous: The result variable and the decision variables can take any real value. Also, all the different coefficients can take any real value.
- Objectives and constraints are linear expressions: The relationships between the variables are expressed as linear expressions. 

Clearly, CLP establishes a rather simplified model of real world problems. Many additional assumptions are needed to represent real problems as a set of linear expressions. Yet, CLP is a very powerful tool in OR and it can provide valuable insights to decision making in different fields. The main reason is that, once these assumptions are taken, linear algebra provides a lot of valuable resources to find a solution and analyse it.  

The main types of problems that will be covered in the CLP exercises belong to two problem types:

- Blending problems: In blending problems, the objective is to find the optimal combination of components in a set of products that either minimise costs or maximise profits 
- Production mix: Production mix problems help us determine the optimal allocation of resources in the production of good or services to either minimise costs or maximise profits

## Set up
As mentioned above, in CLP the result unknown variable, noted as $z$, can take any real value:
$$

$$

First, we have an objective function, which will have a specific value z, which is unkown.
And the value of this unknown, the value of z is a function of another set of unknowns, which are called decision variables and that represent our decisions.we are going to note these unknowns as x, plus an integer subindex that goes from 1 to n. Therefore, we will have n different decision variables, that are going to be continuous. And, in extension, z is also going to be continous.
So now we know from where does the C in Continous comes from. Now, in CLP, the function f is a linear function.
Now, what we want is to maximise or minimise z, and since, which as we said is a linear function and therefore can be expressed as the sum of the product of the decision variables multiplied by a set of coefficients, which are noted as c1 to cn.
And our optimisation function is subject to a set of constraints, which are also linear functions of the decision variables, that is, the sum product of the decision variables times a set of coefficients noted as must be less than, greater than, or equal to another coefficient noted as b. Note that coefficients a have two sub-indexes, the second is equal to the index of the corresponding decision variable, and the first is equal to the sub-index of b.
This is because we will have several constraints, that is, our optimisation function is subject to a set of m constraints.
So, for the second constraint we will have again a set of coefficients a and another coefficient b, which different index, and the same for the rest of constraints down to m.
We are going to refer to these expressions to the left as the Left hand side, and to the other side of the relationship as the right hand side.
Now, note that we can use the sum operator to represent the objective function in a more compressed form, that is, this guy to the left is equal to the sum of the product of cj times xj for j equal to 1 up to n. Note that this is can also be represented as the dot product of two vectors, the vector x with the decision variables and the vector c of the coefficients.
We can do the same transformations to the left hand sides of the constraints, expressing them as the sum product of the decision variables times the a coefficients. And, we may as well express all the left hand sides of the constraints as the product of a matrix A that contains all the different coefficients times the decision variable vector.
These alternative compact forms allow us to deal with problems with an arbitrary number of decision variables and an arbitrary number of constraints.