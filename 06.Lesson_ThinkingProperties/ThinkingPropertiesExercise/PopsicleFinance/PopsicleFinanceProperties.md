# Properties

## Valid States

- If the sum of user deposits > 0, then the totalSupply > 0
-

## Variable transition

- User's erc20 token balance should increase on a deposit
- User's erc20 token balance should decrease on a withdrawal
- User's ETH balance should increase when claiming owed fees

## State transitions

## High-level

- Should be able to collect fees for providing liquidity
- Should be able to mint shares in return for depositing tokens
- Should be able to burn shares in exchange for collateral

## Unit tests

- Depositing ETH, returns ERC20 tokens
- Burning ERC20 tokens, should allow fee's to be claimed, then on a fee claim the collateral should be returned

# Categorised

1. VS-1, H-2 and H-3, otherwise protocol is insolvent
2. H-1, fee claiming is important, but more important to return underlying collateral
