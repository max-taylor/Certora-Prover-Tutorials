methods {
  getTokenAtIndex(uint256 index) returns (address) envfree
  getIdOfToken(address token) returns (uint256) envfree
  getReserveCount() returns (uint256) envfree
  addReserve(address token, address stableToken, address varToken, uint256 fee) envfree
  removeReserve(address token) envfree
}

invariant mappingCorrelation(uint256 index, address token)
  // Using an equivalent operator (<=>) to allow for F and F to pass the check, otherwise that would fail but it is a valid state
  (( index != 0 && token != 0 ) => (getTokenAtIndex(index) == token <=> getIdOfToken(token) == index)) 
            &&
	(( index == 0 && token !=0 ) => (getTokenAtIndex(index) == token => getIdOfToken(token) == index))
        {
            preserved
            {
                requireInvariant indexLessThanCount(token);
            }
            preserved removeReserve(address t) {
			        require t == token;
		        }
        }

// There should not be a token saved at an index greater or equal to reserve counter.
invariant indexLessThanReserveCounter(address token) 
  (getReserveCount() > 0 => getIdOfToken(token) < getReserveCount()) &&
  (getReserveCount() == 0 => getIdOfToken(token) == 0) {
    preserved removeReserve(address t) {
      require t == token;
    }
  }

// if the number of elements in the list is non-zero,
// the id of an existing asset must not exceed the number of elements
invariant indexLessThanCount(address token)
    (getReserveCount() > 0 => getIdOfToken(token) < getReserveCount()) &&
    (getReserveCount() == 0 => getIdOfToken(token) == 0)
        {
            preserved removeReserve(address t) {
			    require t == token;
		    }
      }

// each reserve in the list has a unique id
invariant indexInjective(address token1, address token2)
    (token1 != token2) && (token1 != 0 ) && (token2 != 0) => 
        (getIdOfToken(token1) == 0 || (getIdOfToken(token1) != getIdOfToken(token2))) 
    {
        preserved
        {
            requireInvariant indexLessThanCount(token1);
            requireInvariant indexLessThanCount(token2);
            requireInvariant mappingCorrelation(getIdOfToken(token1), token1);
            requireInvariant mappingCorrelation(getIdOfToken(token2), token2);
        }
    }
