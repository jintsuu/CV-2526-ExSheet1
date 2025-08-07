# Exercise set 1

*All assignments need to be implemented within the function skeletons found in `submission.py`
and you need to hand in this file in the form `submission_<STUDENTID>.py` at the link provided
for this exercise sheet via e-mail.*

## Exercise 1.1

Use `torch.arange` to create a sequence and `einops.rearrange` (suggestion) to reshape it.
In particular, create a tensor with values from 0 to 11, then reshape this sequence into a 
`(3,4)` tensor and return it. Implement the functionality within `assignment_ex1`.

### Exercise 1.2

Create a `torch` 32-bit floating point tensor `T0`   that holds a sequence of integers from `0` to `16*3*3` and reshape that tensor to shape `(16,3,3)`. Then, create a second tensor `T1` which is `T0` multiplied by 3. Finally, use `torch.matmul` to multiply all 16 3x3 matrices from `T0` with the 16 3x3 matrices in `T1` and return the result where all `3*3` matrices are *summed up*. Implement the functionality within `assignment_ex2`.

### Exericse 1.3

Use `torch.arange` to create a sequence of integers from 0 to 35, then rearrange that sequence into a `(6,6)` tensor and, finally, create a `(9,2,2)` tensor from the previous one that holds all non-overlapping `(2,2)` patches. Return this last tensor. Implement the functionality within `assignment_ex3`.
