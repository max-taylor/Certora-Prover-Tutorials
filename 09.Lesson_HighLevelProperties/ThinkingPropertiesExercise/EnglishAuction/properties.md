# Valid States

If there is a highest bidder, then the highest bid must be > 0
highestBidder() != 0 <=> highestBid > 0

# State Transitions

Adding a new bid, increases the highest bid

# Variable Transitions

Adding a new bid, increases the highest bid
Withdrawing deletes the callers bid total

# High-level

When bidding, the contract should take the specified amount of tokens from the caller and store them in the contract

If the user isn't the highest bidder, they can withdraw their tokens

Ending the auction transfers the token amount to the seller and the bidder receives the NFT

Starting an auction, takes an NFT from the user

# Unit tests

Adding a new bid, increases the highest bid, sets the highest bidder to be the caller and increases the caller's bid total

Only the seller can start the auction, it can only be started and once
