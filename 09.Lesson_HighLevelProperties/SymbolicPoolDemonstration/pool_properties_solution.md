# Valid States

# High Level

If depositing more than 0 tokens, the user should receive > 0 shares
The total supply of the pool is greater or equal to the sum of all user balances
The ordering of transactions shouldn't affect another user's action

# State Transition

balanceOf(user) increases => deposit was called
balanceOf(user) decreases => withdraw was called

# Unit tests

Calling deposit should increase; totalSupply, balanceOf(user), asset.balanceOf(address(this)) and decrease the user's balance
